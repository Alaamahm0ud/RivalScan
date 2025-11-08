
---

## 📄 `docs/deployment/docker.md` — دليل تشغيل RivalScan باستخدام Docker (ثنائي اللغة، منسق بالكامل)

```markdown
# 🐳 Docker Deployment Guide | دليل النشر باستخدام Docker

This guide explains how to run RivalScan using Docker for local development or containerized deployment.

يشرح هذا الدليل كيفية تشغيل RivalScan باستخدام Docker لأغراض التطوير المحلي أو النشر بالحاويات.

---

## 📦 Requirements | المتطلبات

- Docker  
- Docker Compose  
- PostgreSQL image with pgvector extension  
- Optional: `.env` file for secrets and config

---

## 🚀 Quick Start | بدء سريع

### 1. Clone the repository | استنساخ المستودع

```bash
git clone https://github.com/your-username/RivalScan.git
cd RivalScan
```

### 2. Build and run containers | بناء وتشغيل الحاويات

```bash
docker-compose up --build
```

This will start:
- FastAPI backend  
- React frontend  
- PostgreSQL database with pgvector  
- Optional adminer (DB GUI)

سيتم تشغيل:
- خادم FastAPI  
- واجهة React  
- قاعدة بيانات PostgreSQL مع pgvector  
- لوحة إدارة اختيارية (Adminer)

---

## 🗄️ Database Initialization | تهيئة قاعدة البيانات

After containers are running, execute the schema and seed files:

بعد تشغيل الحاويات، نفّذ ملفات الهيكل والبيانات:

```bash
docker exec -i rivalscan-db psql -U postgres -d rivalscan < sql/RivalScan_ERD_and_Schema.sql
docker exec -i rivalscan-db psql -U postgres -d rivalscan < sql/seed_data.sql
```

---

## ⚙️ Environment Variables | متغيرات البيئة

Use a `.env` file to configure secrets and ports:

استخدم ملف `.env` لتحديد الإعدادات السرية والمنافذ:

```env
DB_HOST=rivalscan-db
DB_PORT=5432
DB_USER=postgres
DB_PASS=yourpassword
DB_NAME=rivalscan
```

---

## 🧪 Testing Containers | اختبار الحاويات

```bash
docker ps        # Check running containers
docker logs <container_name>  # View logs
docker exec -it <container_name> bash  # Access shell
```

---

## 🧭 Notes | ملاحظات

- You can scale services using Docker Compose profiles  
  يمكنك توسيع الخدمات باستخدام ملفات تعريف Docker Compose

- For cloud deployment, see `docs/deployment/cloud.md`  
  للنشر على السحابة، راجع `docs/deployment/cloud.md`

- All services are modular and can be replaced independently  
  جميع الخدمات قابلة للاستبدال بشكل مستقل
```

---
