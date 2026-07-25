# 🚀 AutoDevAI

> Autonomous Multi-Agent Software Development System built in Python.

AutoDevAI automatically analyzes an existing GitHub repository and performs software engineering tasks using multiple AI agents.

---

## ✨ Features

- Repository Cloning
- Project Planning
- AI Code Review (Gemini)
- Multi-LLM Architecture (Gemini + OpenAI Ready)
- Automated Testing (Pytest)
- Security Analysis (Bandit)
- Documentation Generation
- Final Report Generation
- Shared Memory Between Agents
- Modular Agent Architecture

---

# 🏗 Architecture

```text
                GitHub Repository
                        │
                        ▼
                GitHub Clone Tool
                        │
                        ▼
               Shared Memory System
                        │
                        ▼
               Planner Agent
                        │
                        ▼
              Reviewer Agent (LLM)
                        │
                        ▼
                Tester Agent
                        │
                        ▼
           Documentation Agent
                        │
                        ▼
              Security Agent
                        │
                        ▼
             Final Report Agent
                        │
                        ▼
               Markdown Reports
```

---

# 📁 Project Structure

```text
AutoDevAI/

├── agents/
│   ├── planner.py
│   ├── reviewer.py
│   ├── tester.py
│   ├── documentation.py
│   ├── security.py
│   └── final_report.py
│
├── core/
│   ├── workflow.py
│   ├── shared_memory.py
│   └── review_engine.py
│
├── llm/
│   ├── provider.py
│   ├── gemini_provider.py
│   ├── openai_provider.py
│   ├── base_provider.py
│   └── config.py
│
├── tools/
│   ├── github.py
│   ├── test_runner.py
│   └── security_scanner.py
│
├── workspace/
├── reports/
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙ Workflow

```text
GitHub URL

↓

Clone Repository

↓

Planner Agent

↓

Reviewer Agent

↓

Tester Agent

↓

Documentation Agent

↓

Security Agent

↓

Final Report Agent

↓

Reports
```

---

# 🧰 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Language |
| Gemini API | AI Code Review |
| OpenAI | Multi-Provider Support |
| Pytest | Testing |
| Bandit | Security Analysis |
| Git | Version Control |

---

# 📄 Generated Reports

After execution, AutoDevAI generates:

```
documentation_report.md

testing_report.md

security_report.md

final_report.md
```

---

# 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/AutoDevAI.git

cd AutoDevAI

pip install -r requirements.txt
```

Create a `.env`

```env
GEMINI_API_KEY=YOUR_KEY

OPENAI_API_KEY=YOUR_KEY
```

Run

```bash
python main.py
```

---

# 📌 Current Status

| Sprint | Status |
|---------|--------|
| Sprint 1 | ✅ |
| Sprint 2 | ✅ |
| Sprint 3 | ✅ |
| Sprint 4 | ✅ |
| Sprint 5 | ✅ |
| Sprint 6 | ✅ |
| Sprint 7 | ✅ |
| Sprint 8 | ✅ |
| Sprint 9 | ✅ |
| Sprint 10 | ✅ |

---

# 🗺 Roadmap

### Completed

- Repository Cloning
- Planner Agent
- AI Reviewer
- Testing Engine
- Documentation Generator
- Security Scanner
- Final Report Generator

### Coming Next

- CrewAI Integration
- FastAPI Backend
- React Dashboard
- Docker Support
- GitHub Actions
- CI/CD Pipeline
- Multi-Agent Collaboration
- Multi-Repository Analysis

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Ishan**

AutoDevAI is being developed as a production-grade autonomous software engineering system for portfolio, interviews, and real-world software engineering practices.
