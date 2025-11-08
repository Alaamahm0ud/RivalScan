# 🧬 Database Schema Overview

RivalScan uses a relational database (PostgreSQL) enhanced with vector search capabilities via pgvector. The schema is designed to support structured business data, semantic embeddings, and audit trails.

## 🗂️ Core Tables

### 1. `companies`
Stores metadata about each business entity.

| Column         | Type        | Description                     |
|----------------|-------------|---------------------------------|
| id             | UUID        | Unique company identifier       |
| name           | TEXT        | Company name                    |
| industry       | TEXT        | Sector or vertical              |
| created_at     | TIMESTAMP   | Registration date               |

### 2. `datasets`
Tracks uploaded files and their processing status.

| Column         | Type        | Description                     |
|----------------|-------------|---------------------------------|
| id             | UUID        | Unique dataset ID               |
| company_id     | UUID        | Linked company                  |
| filename       | TEXT        | Original file name              |
| status         | TEXT        | Processing status               |
| uploaded_at    | TIMESTAMP   | Upload timestamp                |

### 3. `insights`
Stores generated recommendations and diagnostics.

| Column         | Type        | Description                     |
|----------------|-------------|---------------------------------|
| id             | UUID        | Insight ID                      |
| dataset_id     | UUID        | Source dataset                  |
| type           | TEXT        | Insight category                |
| score          | FLOAT       | Relevance or risk score         |
| explanation    | TEXT        | Justification or traceability   |

### 4. `embeddings`
Semantic vectors for search and matching.

| Column         | Type        | Description                     |
|----------------|-------------|---------------------------------|
| id             | UUID        | Vector ID                       |
| dataset_id     | UUID        | Source dataset                  |
| vector         | VECTOR(768) | pgvector embedding              |
| label          | TEXT        | Semantic label or tag           |

---

# 🧬 نظرة على هيكل قاعدة البيانات

يعتمد RivalScan على قاعدة بيانات علائقية (PostgreSQL) مدعومة بإمكانيات البحث الدلالي باستخدام pgvector. تم تصميم الهيكل لدعم بيانات الأعمال المنظمة، التضمينات الدلالية، وسجلات التتبع.

## 🗂️ الجداول الأساسية

### 1. `companies`
تخزن بيانات تعريفية عن كل شركة.

| العمود         | النوع        | الوصف                            |
|----------------|--------------|----------------------------------|
| id             | UUID         | معرف فريد للشركة                 |
| name           | TEXT         | اسم الشركة                       |
| industry       | TEXT         | القطاع أو المجال                 |
| created_at     | TIMESTAMP    | تاريخ التسجيل                    |

### 2. `datasets`
تتابع الملفات المرفوعة وحالة معالجتها.

| العمود         | النوع        | الوصف                            |
|----------------|--------------|----------------------------------|
| id             | UUID         | معرف فريد للملف                  |
| company_id     | UUID         | الشركة المرتبطة                  |
| filename       | TEXT         | اسم الملف الأصلي                 |
| status         | TEXT         | حالة المعالجة                    |
| uploaded_at    | TIMESTAMP    | وقت الرفع                        |

### 3. `insights`
تخزن التوصيات والتشخيصات الناتجة.

| العمود         | النوع        | الوصف                            |
|----------------|--------------|----------------------------------|
| id             | UUID         | معرف التوصية                     |
| dataset_id     | UUID         | الملف المصدر                     |
| type           | TEXT         | نوع التوصية                      |
| score          | FLOAT        | درجة الأهمية أو الخطورة          |
| explanation    | TEXT         | التبرير أو مصدر التوصية          |

### 4. `embeddings`
تضمينات دلالية للبحث والمطابقة
