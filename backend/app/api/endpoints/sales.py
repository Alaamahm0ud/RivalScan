import pandas as pd
from io import StringIO
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from pathlib import PurePath
import re 
from ...db.database import get_db
from ...db.models import Product
from .auth import get_current_user, required_role # تم التعديل
from ...core.config import UserRole # (افتراض: تحتاج إضافة UserRole إلى config.py)

router = APIRouter()

# --- Security Functions ---

# 1. Sanitization Function for CSV Injection
def sanitize_cell(cell):
    """Prevents CSV Injection by neutralizing formula-starting characters."""
    if isinstance(cell, str) and cell.startswith(('/', '=', '+', '-', '@')):
        # Prepend a single quote to neutralize the formula
        return "'" + cell
    return cell

# 2. Filename Sanitization for Path Traversal
def secure_filename(filename: str):
    """Sanitizes filename to prevent directory traversal attacks."""
    # Ensure only the base filename is used, and strip dangerous characters
    path = PurePath(filename)
    name = path.name # Get only the file name part
    
    # Remove dangerous characters (used to access other directories or system files)
    name = re.sub(r'[\\/|:*"<>?]', '', name) 
    
    # Ensure it's not trying to traverse directories
    if '..' in name:
        name = name.replace('..', '')

    return name

# --- API Endpoint ---

# Enforce RBAC: Only Analyst or Admin can upload data
@router.post("/upload", 
             dependencies=[Depends(required_role(UserRole.Analyst))]) # 3. RBAC ENFORCEMENT
async def upload_sales_data(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user) # get_current_user is still needed inside required_role
):
    # --- Input Validation & Size Limit ---
    MAX_FILE_SIZE_MB = 10 
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

    # Check File Size Limit (part of Input Validation)
    if file.size > MAX_FILE_SIZE_BYTES:
        raise HTTPException(status_code=400, detail=f"File size exceeds {MAX_FILE_SIZE_MB}MB limit.")
        
    # Check Content-Type (Basic check - can be spoofed)
    if file.content_type not in ['text/csv', 'application/vnd.ms-excel']: # Added support for .xlsx type
        raise HTTPException(status_code=400, detail="Only CSV/Excel files are allowed (text/csv or application/vnd.ms-excel)")

    # Sanitize filename (even if not saving it, good practice to prevent logging malicious names)
    secure_name = secure_filename(file.filename) 
    # (Note: In this specific code, the file is not saved to disk, but the check is necessary)

    contents = await file.read()
    try:
        # Read the file content safely
        df = pd.read_csv(StringIO(contents.decode('utf-8')))
        
        # 1. APPLY CSV INJECTION SANITIZATION
        # Apply cleaning to all string/object columns that might be exported and opened by an analyst
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(sanitize_cell)

        # Basic validation
        required_columns = ['name', 'quantity_sold', 'our_price']
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(status_code=400, detail=f"CSV must contain columns: {', '.join(required_columns)}")

        # Clear old data for this user
        db.query(Product).filter(Product.user_id == current_user.id).delete()

        # Insert new data
        for index, row in df.iterrows():
            product = Product(
                user_id=current_user.id,
                # Use the sanitized name from the dataframe
                name=row['name'], 
                # Ensure numerical columns are correctly casted before insertion
                quantity_sold=int(row['quantity_sold']), 
                our_price=float(row['our_price'])
            )
            db.add(product)
        
        db.commit()
        return {"message": f"Successfully uploaded {len(df)} products. Filename: {secure_name}"}

    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File decoding error. Ensure the file is UTF-8 encoded.")
    except Exception as e:
        # Avoid showing raw internal errors (500)
        print(f"File processing error: {e}")
        raise HTTPException(status_code=500, detail="Error processing file. Check file format and encoding.")


@router.get("/analysis")
# This endpoint also needs RBAC to ensure only Analysts/Viewers can access it
def get_sales_analysis(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    products = db.query(Product).filter(Product.user_id == current_user.id).all()
    
    total_revenue = sum(p.our_price * p.quantity_sold for p in products)
    top_products = sorted(products, key=lambda p: p.quantity_sold, reverse=True)[:3]
    
    return {
        "total_revenue": total_revenue,
        "top_products": [{"name": p.name, "quantity": p.quantity_sold} for p in top_products],
        "all_products": [{"name": p.name, "our_price": p.our_price} for p in products]
    }
