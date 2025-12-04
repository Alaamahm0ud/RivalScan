# Contribution Guidelines

Thanks for your interest in contributing to **RivalScan**.

### 📌 Development Flow
1. Fork the repository
2. Create feature branch:

___

git checkout -b feature/new-module

___

3. Commit with clear messages:

____

git commit -m "feat: add csv sanitization layer"

____

4. Push and open Pull Request.

### 📌 Coding Standards
- Linting enforced via GitHub Actions
- Python formatting: `black`, `isort`, `flake8`
- Typing level: mypy (strict mode)

### 📌 Security Notes
⚠️ Any feature touching:
- Authentication
- File handling
- Upload / decode / parse
- Data exports

must include:
- Threat scenario
- Validation
- Sanitization test case

### 📌 Tests
Every PR **must** include passing tests:

___

pytest --maxfail=1 --disable-warnings

____


### 📌 Branch Naming Rules
Feature: `feature/xxx`
Fix: `fix/xxx`
Docs: `docs/xxx`
Security patch: `sec/xxx`


---

Thanks for helping make RivalScan better!
