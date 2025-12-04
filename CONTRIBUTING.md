````markdown
# Contribution Guidelines

Thank you for your interest in contributing to **RivalScan** 🎯  
This document outlines the standards and workflow required for all contributions.

---

## 📌 Development Workflow

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/new-module
````

3. **Commit with clear, conventional messages**

   ```bash
   git commit -m "feat: add csv sanitization layer"
   ```
4. **Push and open a Pull Request (PR)**

---

## 📌 Coding Standards

* Formatting: `black` & `isort`
* Linting: `flake8`
* Typing level: `mypy` (strict mode)
* Security gates enforced via CI

---

## 📌 Test Requirements

All PRs must pass full test execution before review:

```bash
pytest --maxfail=1 --disable-warnings -q
```

🔹 Any PR without tests **will not be merged**
🔹 Any CI failure = automatic refusal

---

## 📌 Security Notes (Critical)

Any modification involving:

* Authentication
* File parsing / uploads
* CSV / Excel intake
* Data exports
* API authorization
* RBAC

must include:

* Threat scenario description
* Input validation layer
* Sanitization logic
* Abuse-case handling

---

## 📌 Branch Naming Rules

| Type           | Format        |
| -------------- | ------------- |
| Feature        | `feature/xxx` |
| Fix            | `fix/xxx`     |
| Documentation  | `docs/xxx`    |
| Security Patch | `sec/xxx`     |

---

## 📌 PR Approval Policy

* Minimum **1 review approval** (internal)
* Passing CI is **mandatory**
* Security PRs require **security reviewer signature**

---

## 🙌 Final Note

Thanks for helping make RivalScan stronger and more secure.
Professionalism, clarity, and security-first design are our core values.

```
```
