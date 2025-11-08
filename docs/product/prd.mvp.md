# 📘 Product Requirements Document (PRD) — RivalScan Core MVP  
# 📘 وثيقة متطلبات المنتج — RivalScan Core MVP

---

## 1. Basic Information | المعلومات الأساسية

- **Product Name | اسم المنتج:** RivalScan Core MVP  
- **Version | الإصدار:** 1.0  
- **Date | تاريخ التوثيق:** 2025-11-08  
- **Author | المؤلف:** Alaa Mahmoud Mohamed Awadallah

---

## 2. Executive Summary | الملخص التنفيذي

RivalScan Core MVP is a focused product designed to validate the core value of the RivalScan platform. It addresses a critical challenge for SMEs:  
**Difficulty comparing their prices with key competitors and making fast, data-driven pricing decisions.**

RivalScan Core MVP هو منتج مصغّر يهدف إلى إثبات القيمة الأساسية لمنصة RivalScan. يركّز على حل مشكلة جوهرية تواجه الشركات الصغيرة والمتوسطة:  
**صعوبة مقارنة أسعارها بأسعار المنافسين الرئيسيين واتخاذ قرارات تسعير سريعة مبنية على بيانات المبيعات الفعلية.**

---

## 3. Problem & Solution | المشكلة والحل

- **Problem | المشكلة:**  
  Small business owners struggle to track competitor pricing and make informed pricing decisions.  
  أصحاب الأعمال الصغيرة يجدون صعوبة في تتبع أسعار المنافسين واتخاذ قرارات تسعير مبنية على بيانات حقيقية.

- **Solution | الحل:**  
  A simple platform to upload sales data, compare it with competitor prices, and receive actionable suggestions.  
  منصة بسيطة تسمح برفع بيانات المبيعات، ومقارنتها بأسعار المنافسين، وتقديم اقتراحات قابلة للتنفيذ.

---

## 4. Target Audience & User Story | الجمهور المستهدف وقصة المستخدم

- **Persona | الشخصية:**  
  "Sara", a small online store manager.  
  "سارة"، مديرة متجر إلكتروني صغير.

- **User Story | قصة المستخدم:**  
  As Sara, I want to upload my sales file and compare it with competitor prices so I can make faster, smarter pricing decisions.  
  بصفتي "سارة"، أريد أن أرفع ملف مبيعاتي وأقارنه بأسعار المنافسين، حتى أتخذ قرارات تسعير أسرع وأكثر ذكاءً.

---

## 5. Features & Functional Requirements | قائمة الميزات والمتطلبات الوظيفية

| #  | Feature Name | اسم الميزة | Description | الوصف |
|----|--------------|-------------|-------------|-------|
| F1 | User Authentication | مصادقة المستخدم | Secure login via email and password | تسجيل دخول آمن بالبريد الإلكتروني وكلمة المرور |
| F2 | Sales Data Upload | رفع بيانات المبيعات | Upload and validate CSV files | رفع ملف CSV والتحقق من صحته |
| F3 | Competitor Input | إدخال بيانات المنافس | Form to input competitor product prices | نموذج لإدخال أسعار المنتجات لدى المنافس |
| F4 | Dashboard | لوحة التحكم الرئيسية | Show KPIs, comparison table, and suggestions | عرض مؤشرات الأداء، جدول مقارنة، واقتراحات |
| F5 | Rule-Based Engine | محرك الاقتراحات | Generate suggestions based on defined rules | توليد اقتراحات نصية بناءً على قواعد محددة |

---

## 6. Acceptance Criteria | معايير القبول

- User can create an account and upload a CSV file successfully  
- Dashboard displays data and suggestions correctly  
- Experience is smooth and responsive

- يمكن للمستخدم إنشاء حساب ورفع ملف CSV بنجاح  
- تعرض لوحة التحكم البيانات والاقتراحات بشكل صحيح  
- يجب أن تكون التجربة سلسة وسريعة

---

## 7. Non-Functional Requirements | المتطلبات غير الوظيفية

- **Performance | الأداء:** Dashboard loads in under 3 seconds  
- **Security | الأمان:** Passwords and user data must be encrypted  
- **Usability | سهولة الاستخدام:** Interface must be simple and intuitive for non-technical users

- **الأداء:** يجب أن تفتح لوحة التحكم في أقل من 3 ثوانٍ  
- **الأمان:** يجب تشفير كلمات المرور وبيانات المستخدمين  
- **سهولة الاستخدام:** يجب أن تكون الواجهة بسيطة وواضحة للمستخدم غير التقني
