---

## 📄 `docs/setup-guide.md` — دليل التثبيت والتشغيل (ثنائي اللغة، منسق بالكامل)

```markdown
# ⚙️ Setup Guide | دليل التثبيت

This guide walks you through installing and running RivalScan locally for development and testing.

يشرح هذا الدليل كيفية تثبيت وتشغيل RivalScan محليًا لأغراض التطوير والاختبار.

---

## 🧱 Prerequisites | المتطلبات الأساسية

- Python 3.10+  
- Node.js 18+  
- PostgreSQL with pgvector extension  
- Docker (optional for containerized setup)  
- Git

---

## 🖥️ Local Installation | التثبيت المحلي

### 1. Clone the repository | استنساخ المستودع

```bash
git clone https://github.com/your-username/RivalScan.git
cd RivalScan
```

### 2. Set up the backend | إعداد الخادم (FastAPI)

```bash
cd src/backend
python -m venv venv
source venv/bin/activate  # أو venv\Scripts\activate على ويندوز
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Set up the frontend | إعداد الواجهة (React)

```bash
cd ../../frontend
npm install
npm run dev
```

---

## 🗄️ Database Setup | إعداد قاعدة البيانات

1. Create a PostgreSQL database  
   أنشئ قاعدة بيانات PostgreSQL

2. Enable pgvector extension  
   فعّل امتداد pgvector:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

3. Run schema and seed files  
   نفّذ ملفات الهيكل والبيانات:
   ```bash
   psql -U your_user -d your_db -f sql/RivalScan_ERD_and_Schema.sql
   psql -U your_user -d your_db -f sql/seed_data.sql
   ```

---

## 🧪 Testing | الاختبار

```bash
cd tests/backend
pytest

cd ../../frontend
npm run test
```

---

## 🧭 Notes | ملاحظات

- You can use `.env` files to manage secrets and config  
  يمكنك استخدام ملفات `.env` لإدارة الإعدادات السرية

- For Docker setup, see `docs/deployment/docker.md`  
  لمزيد من التفاصيل حول Docker، راجع `docs/deployment/docker.md`

- All modules are designed to be modular and replaceable  
  جميع الوحدات مصممة لتكون قابلة للتعديل والاستبدال

---
