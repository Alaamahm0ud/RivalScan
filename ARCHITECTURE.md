---
📐
# 🧱 RivalScan Architecture | بنية مشروع RivalScan

RivalScan is a modular, scalable platform for cyber-aware business analytics.  
RivalScan هو منصة مرنة وقابلة للتوسع لتحليلات الأعمال مع التركيز على الأمن السيبراني.

---

## 🧩 System Overview | نظرة عامة على النظام

```mermaid
graph TD
  UI[React + Tailwind UI] --> API[FastAPI Backend]
  API --> DB[(PostgreSQL + pgvector)]
  API --> AI[Recommendation Engine]
  API --> Storage[S3-compatible Storage]
  API --> Auth[JWT Auth + Role-based Access]


---

🧠 Core Components | المكونات الأساسية

1. Frontend (React) | الواجهة الأمامية (React)

Built with Vite + TailwindCSS. | مبنية باستخدام Vite و TailwindCSS

Handles file uploads, dashboard rendering, and report previews. | تدير رفع الملفات، عرض لوحة التحكم، ومعاينة التقارير

Communicates with backend via RESTful APIs. | تتواصل مع الواجهة الخلفية عبر RESTful APIs



2. Backend (FastAPI) | الواجهة الخلفية (FastAPI)

Serves APIs for data ingestion, analysis, and report generation. | توفر واجهات برمجة التطبيقات لجمع البيانات، التحليل، وإنشاء التقارير

Integrates AI engine and rule-based logic. | تدمج محرك الذكاء الاصطناعي والمنطق القائم على القواعد

Handles authentication and authorization. | تدير المصادقة والتحكم بالوصول



3. Database (PostgreSQL + pgvector) | قاعدة البيانات (PostgreSQL + pgvector)

Stores user data, uploaded files metadata, and analysis results. | تخزن بيانات المستخدم، ميتاداتا الملفات المرفوعة، ونتائج التحليل

pgvector enables semantic search and embedding storage. | توفر pgvector البحث الدلالي وتخزين embeddings



4. AI Engine | محرك الذكاء الاصطناعي

Combines: | يجمع بين:

Rule-based logic (thresholds, heuristics) | منطق قائم على القواعد (حدود، استدلالات)

ML/LLM-based models (optional) | نماذج تعلم الآلة / النماذج اللغوية الكبيرة (اختياري)


Generates actionable recommendations. | يولد توصيات قابلة للتنفيذ



5. Storage (S3-compatible) | التخزين (متوافق مع S3)

Stores uploaded CSV/Excel files and generated PDF reports. | يخزن ملفات CSV/Excel المرفوعة والتقارير PDF الناتجة





---

🔐 Security | الأمان

JWT-based authentication | مصادقة مبنية على JWT

Role-based access control (Admin, Analyst, Viewer) | تحكم بالوصول حسب الدور (مسؤول، محلل، مشاهد)

Input validation and file sanitization | التحقق من صحة البيانات وتنظيف الملفات



---

⚙️ DevOps

Dockerized services | خدمات معزولة بواسطة Docker

GitHub Actions for CI/CD | GitHub Actions لتكامل ونشر مستمر

Kubernetes-ready deployment (optional) | نشر جاهز على Kubernetes (اختياري)


---

🛠️ **INSTALL.md**

```markdown
# ⚙️ Installation Guide – RivalScan | دليل تثبيت RivalScan

This guide helps you run RivalScan locally using Docker or manually.  
هذا الدليل يوضح كيفية تشغيل RivalScan محليًا باستخدام Docker أو الإعداد اليدوي.

---

## 🐳 Option 1: Run with Docker (Recommended) | الخيار 1: التشغيل عبر Docker (موصى به)

Prerequisites | المتطلبات
- Docker & Docker Compose installed | تثبيت Docker و Docker Compose

Steps | الخطوات
```bash
git clone https://github.com/Alaamahm0ud/RivalScan.git
cd RivalScan
cp .env.example .env
docker-compose up --build

Frontend: http://localhost:3000 | الواجهة الأمامية
Backend API: http://localhost:8000/docs | واجهة برمجة التطبيقات الخلفية


---

🧪 Option 2: Manual Setup | الخيار 2: الإعداد اليدوي

Prerequisites | المتطلبات

Python 3.10+ | بايثون 3.10+

Node.js 18+ | Node.js 18+

PostgreSQL 14+ | PostgreSQL 14+

Redis (optional) | Redis (اختياري)


Backend Setup | إعداد الواجهة الخلفية

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

Frontend Setup | إعداد الواجهة الأمامية

cd frontend
npm install
npm run dev


---

🧬 Database Setup | إعداد قاعدة البيانات

Create PostgreSQL DB with pgvector extension | إنشاء قاعدة بيانات PostgreSQL مع امتداد pgvector

Run SQL files in /sql/ to seed test data | تشغيل ملفات SQL في /sql/ لإدخال بيانات اختبارية



---

✅ Test Accounts | حسابات اختبار

Admin: admin@rivalscan.io / admin123 | مسؤول

Analyst: analyst@rivalscan.io / analyst123 | محلل



---

🧯 Troubleshooting | استكشاف الأخطاء

Check .env variables | تحقق من متغيرات .env

Ensure ports 3000 and 8000 are free | تأكد أن المنافذ 3000 و 8000 غير مستخدمة

Use docker-compose logs for debugging | استخدم docker-compose logs للتصحيح


---

