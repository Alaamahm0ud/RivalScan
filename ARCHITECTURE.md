

````markdown
# 🧱 RivalScan Architecture
RivalScan is a modular, scalable platform for cyber-aware business analytics.

# 🧱 بنية RivalScan
RivalScan هو نظام مرن وقابل للتوسع لتحليلات الأعمال المعززة بالوعي الأمني.

---

## 🧩 System Overview | نظرة عامة على النظام

```mermaid
graph TD
  UI[React + Tailwind UI] --> API[FastAPI Backend]
  API --> DB[(PostgreSQL + pgvector)]
  API --> AI[AI Recommendation Engine]
  API --> Storage[S3-compatible Storage]
  API --> Auth[JWT Auth + RBAC]
````

---

## 🧠 Core Components | المكونات الأساسية

### 1. Frontend (React)

* Built with Vite + TailwindCSS.
* Handles file uploads, dashboards, previews.
* Communicates with backend via REST APIs.

### 1. الواجهة الأمامية (React)

* مبنية باستخدام Vite و TailwindCSS.
* تدير رفع الملفات ولوحة التحكم والمعاينات.
* تتواصل مع الواجهة الخلفية عبر REST APIs.

---

### 2. Backend (FastAPI)

* Provides APIs for ingesting, analyzing, reporting.
* Integrates AI engine + rules engine.
* Handles JWT authentication & authorization.

### 2. الواجهة الخلفية (FastAPI)

* توفر واجهات برمجة لجمع البيانات والتحليل وإنشاء التقارير.
* تدمج محرك الذكاء الاصطناعي والمنطق القائم على القواعد.
* تدير المصادقة والتحكم بالوصول عبر JWT.

---

### 3. Database (PostgreSQL + pgvector)

* Stores users, metadata, analysis results.
* pgvector enables embeddings + semantic search.

### 3. قاعدة البيانات

* تخزن المستخدمين وملفات الميتاداتا ونتائج التحليل.
* pgvector توفر تخزين embeddings وبحث دلالي.

---

### 4. AI Engine | محرك الذكاء الاصطناعي

* Rules (heuristics + thresholds)
* ML/LLM models (optional)
* Generates actionable recommendations

### محرك الذكاء الاصطناعي

* قواعد واستدلالات
* نماذج تعلم آلي أو LLM (اختياري)
* يولد توصيات تنفيذية قابلة للتطبيق

---

### 5. Storage (S3-compatible)

Stores uploaded CSV/Excel files & generated PDFs.

### التخزين (متوافق S3)

يخزن ملفات CSV/Excel والتقارير PDF.

---

## 🔐 Security | الأمان

* JWT-based authentication

* Role-based access control (Admin / Analyst / Viewer)

* File sanitization + input validation

* مصادقة JWT

* أدوار RBAC

* تنظيف الملفات والتحقق من المدخلات

---

## ⚙️ DevOps

* Dockerized services

* GitHub Actions CI/CD

* Kubernetes-ready

* خدمات Docker

* خطوط CI/CD

* جاهز لـ Kubernetes

````

---

# ✅ **INSTALL.md — النسخة النهائية الجاهزة للرفع**

```markdown
# ⚙️ Installation Guide — RivalScan
This guide explains how to run RivalScan locally using Docker or manual setup.

# ⚙️ دليل التثبيت — RivalScan
هذا الدليل يوضح كيفية تشغيل RivalScan محليًا باستخدام Docker أو الإعداد اليدوي.

---

## 🐳 Option 1: Run with Docker (Recommended)
Prerequisites:
- Docker
- Docker Compose

### Steps:
```bash
git clone https://github.com/Alaamahm0ud/RivalScan.git
cd RivalScan
cp .env.example .env
docker-compose up --build
````

Frontend → [http://localhost:3000](http://localhost:3000)
Backend API → [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Option 2: Manual Setup

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🧬 Database Setup

* Create PostgreSQL DB with pgvector extension
* Run SQL files in `/sql/`

---

## ✅ Test Accounts

Admin: `admin@rivalscan.io / admin123`
Analyst: `analyst@rivalscan.io / analyst123`

---

## 🧯 Troubleshooting

* Verify `.env`
* Ensure ports 3000/8000 are not used
* Use `docker-compose logs` for debugging

```


