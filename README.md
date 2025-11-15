# 🛡️ RivalScan — The Intelligent Business Advisor

RivalScan is an intelligent platform for business data analysis and cybersecurity compliance. It transforms raw company data into actionable insights using AI-powered diagnostics and semantic search.

## 🚀 Quick Overview
RivalScan integrates internal sources (CSV, databases) and external OSINT feeds to deliver:
- Operational diagnostics
- Profitability and efficiency recommendations
- Cyber maturity scoring

## 🧩 Key Features
- Upload CSV/Excel files for instant analysis
- API connectors for stores and networks (Shopify, WooCommerce)
- Rule-based recommendation engine + ML forecasting
- Semantic search via pgvector or Milvus
- Printable PDF reports with full explainability

## 🛠 Tech Stack
- Backend: Python + **FastAPI**
- Frontend: **React** + Tailwind
- Database: **PostgreSQL** + pgvector
- Storage: S3
- Containers: **Docker** + **Kubernetes**
- CI/CD: **GitHub Actions**

---

## 💻 Installation & Local Setup (Secure Deployment)

RivalScan is containerized using **Docker** and **Docker Compose** for easy, secure deployment. Follow these steps to get the platform running locally.

### Prerequisites

* **Docker:** Installed and running (Docker Engine or Docker Desktop).
* **Git:** To clone the repository.

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/RivalScan.git](https://github.com/YourUsername/RivalScan.git)
    cd RivalScan
    ```

2.  **Configure Environment Variables:**
    Create a new `.env` file in the root directory by copying the example:
    ```bash
    cp .env.example .env
    # IMPORTANT: Edit the .env file and replace the secret keys (especially JWT_SECRET_KEY) with strong, random values.
    ```

3.  **Start the Services (Secure Build):**
    The command below will build the backend image securely (using the multi-stage `Dockerfile`) and start all services (Backend, Frontend, DB) simultaneously.
    ```bash
    docker-compose up --build -d
    ```

4.  **Access the Application:**
    The services should now be running in the background:
    * **Frontend (App):** Open your browser to `http://localhost:3000`
    * **Backend (API Docs):** View the secured API documentation at `http://localhost:8000/docs`

---
---

# 🛡️ RivalScan — المستشار الذكي للأعمال

RivalScan هي منصة تحليل ذكية وامتثال أمني، تُحوّل بيانات الشركات إلى توصيات قابلة للتنفيذ باستخدام تقنيات الذكاء الاصطناعي والبحث الدلالي.

## 🚀 نظرة سريعة
تقوم RivalScan بدمج مصادر داخلية (مثل CSV وقواعد البيانات) مع مصادر خارجية (OSINT) لتقديم:
- تشخيصات تشغيلية دقيقة
- توصيات لتحسين الربحية والكفاءة
- تقييم لنضج البنية الأمنية والتقنية

## 🧩 الميزات الأساسية
- رفع ملفات **CSV** / **Excel** وتحليل آمن
- موصلات **APIs** للمتاجر والشبكات (**Shopify**، **WooCommerce**)
- محرك اقتراحات قائم على قواعد + نماذج تعلّم آلي
- بحث دلالي باستخدام **pgvector** أو **Milvus**
- تقارير **PDF** قابلة للطباعة مع توثيق مصدر كل توصية

## 🛠 التقنيات المستخدمة
- الواجهة الخلفية: **Python** + **FastAPI**
- الواجهة الأمامية: **React** + **Tailwind**
- قاعدة البيانات: **PostgreSQL** + **pgvector**
- التخزين: **S3**
- الحاويات: **Docker** + **Kubernetes**
- التكامل المستمر: **GitHub Actions**

---

## 💻 التثبيت والإعداد المحلي (نشر آمن)

تم تغليف RivalScan بالكامل باستخدام **Docker** و **Docker Compose** لضمان سهولة النشر وتشغيل آمن. اتبع هذه الخطوات لتشغيل المنصة على جهازك المحلي.

### المتطلبات الأساسية

* **Docker:** مثبت ويعمل (Docker Engine أو Docker Desktop).
* **Git:** لاستنساخ المستودع.

### الخطوات

1.  **استنساخ المستودع:**
    ```bash
    git clone [https://github.com/YourUsername/RivalScan.git](https://github.com/YourUsername/RivalScan.git)
    cd RivalScan
    ```

2.  **إعداد متغيرات البيئة:**
    أنشئ ملف `.env` جديد في المجلد الجذري عن طريق نسخ الملف النموذجي:
    ```bash
    cp .env.example .env
    # هام: قم بتحرير ملف .env واستبدل المفاتيح السرية (خاصة JWT_SECRET_KEY) بقيم عشوائية وقوية جداً.
    ```

3.  **تشغيل الخدمات (بناء آمن):**
    سيقوم هذا الأمر ببناء صورة الواجهة الخلفية بشكل آمن (باستخدام `Dockerfile` متعدد المراحل) وسحب الصور الأخرى، وبدء تشغيل الخدمات الثلاث في نفس الوقت.
    ```bash
    docker-compose up --build -d
    ```

4.  **الوصول إلى التطبيق:**
    الخدمات تعمل الآن في الخلفية:
    * **الواجهة الأمامية (التطبيق):** افتح متصفحك على `http://localhost:3000`
    * **الواجهة الخلفية (توثيق API):** اطلع على توثيق **API** الآمن على `http://localhost:8000/docs`
