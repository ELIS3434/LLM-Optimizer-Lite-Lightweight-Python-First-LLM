# LLM Optimizer Lite 🚀

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Gateway-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Free%20Public%20Release-success)

**Lightweight Python-first LLM gateway + prompt optimization toolkit for indie developers.**

</div>

---

## 🌟 Why this exists
Most teams building with LLM APIs need three things quickly:
- Better quality from prompts
- Better visibility into cost and latency
- A setup that does not require enterprise platform engineering

LLM Optimizer Lite provides this as a pragmatic open-source core.

## 🆓 Free public release model
This repo is published as a **free OSS core** (MIT).
- Build, run, and extend locally
- Use as a base for your own product stack
- Keep your deployment lightweight and transparent

## 👥 Who this is for
- Solo founders shipping AI features
- Startup teams without dedicated platform engineers
- Developers who want prompt versioning + experiments fast

---

## ✨ Core features
- OpenAI-compatible completion API
- Prompt registry with versions
- Request logging (cost, latency, trace ID)
- Basic experiment routing hooks
- Streamlit analytics dashboard
- Docker + Railway + Fly.io deployment files

## 🔌 Top 5 integrations already wired
1. **Multi-provider gateway** (`openai`, `anthropic`, `groq`, `ollama`)
2. **Provider fallback path** (`DEFAULT_PROVIDER` -> `FALLBACK_PROVIDER`)
3. **API key protection toggle** (`API_KEY_ENABLED`, `INTERNAL_API_KEY`)
4. **Request tracking pipeline** (`trace_id`, `latency_ms`, `estimated_cost_usd`)
5. **Live analytics + logs endpoints** (`/analytics/summary`, `/analytics/timeseries`, `/logs`)

---

## 🖼️ Demo and screenshots
> Add your visuals before launch for better conversion.

- Demo GIF: `assets/demo.gif`
- Dashboard screenshot: `assets/dashboard-overview.png`
- Logs screenshot: `assets/dashboard-logs.png`

Example markdown once files are added:
```md
![Demo](assets/demo.gif)
![Overview](assets/dashboard-overview.png)
```

## 💡 Use cases
- Optimize customer support prompts and track latency/cost changes
- Run A/B prompt variants for a lead qualification flow
- Compare provider behavior behind one API interface
- Add lightweight observability to an existing LLM feature

---

## 🏗️ Project architecture
- `backend/` -> FastAPI API, services, schemas, and models
- `dashboard/` -> Streamlit UI pages and components
- `docs/` -> architecture, workflow, deployment, competition, release checklist
- `tests/` -> API and service tests

### 🧠 Runtime flow
`Client` -> `FastAPI /v1/chat/completions` -> `Prompt/Experiment routing` -> `Provider adapter` -> `Request tracker` -> `Analytics + Dashboard`

---

## ⚡ Quickstart (Windows PowerShell)
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn backend.main:app --reload
```

In a second terminal:
```bash
streamlit run dashboard/app.py
```

Open:
- Backend docs: `http://localhost:8000/docs`
- Dashboard: `http://localhost:8501`

## 🐳 Quickstart (Docker)
```bash
docker-compose up --build
```

---

## ☁️ Deployment
- **Railway**: `railway.json` + `Dockerfile.backend`
- **Fly.io**: `fly.toml` + `fly deploy`

## 🔐 Environment variables (key ones)
- `DATABASE_URL`
- `DEFAULT_PROVIDER`
- `DEFAULT_MODEL`
- `FALLBACK_PROVIDER`
- `FALLBACK_MODEL`
- `API_KEY_ENABLED`
- `INTERNAL_API_KEY`

---

## 🧪 API example
```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Hello"}]}'
```

---

## 🗺️ Roadmap
- Human feedback labels
- Batch evaluations
- LLM-as-judge module
- Optional Redis cache
- Webhook alerts
- Lightweight Python SDK

## ❓ FAQ
**Is this production-ready?**
- It is a strong scaffold for production use, but you should add persistent storage hardening, auth strategy, and monitoring for your environment.

**Can I add another provider?**
- Yes. Add a new adapter in `backend/services/providers/` and wire it in `provider_registry.py`.

**Is this free to use?**
- Yes. Core repository is MIT licensed.

## 🛠️ Troubleshooting
- If backend does not start, verify `.env` exists and dependencies are installed.
- If dashboard cannot load data, confirm backend is running on `BACKEND_BASE_URL`.
- If provider responses fail, switch to fallback provider and check API keys.

## 📚 Documentation
- `docs/architecture.md`
- `docs/workflow.md`
- `docs/deployment.md`
- `docs/competitive-landscape.md`
- `docs/public-release-checklist.md`

---

## 🧾 Suggested GitHub metadata
- **Description**: Lightweight Python-first LLM gateway, prompt registry, and experiment dashboard for indie developers.
- **Topics**: `llm`, `fastapi`, `streamlit`, `prompt-engineering`, `ai-gateway`, `python`, `observability`, `llmops`, `indie-hackers`, `openai-compatible`

## 🤝 Contributing
See `CONTRIBUTING.md`.

## 🛡️ Security
See `SECURITY.md`.

## 📄 License
MIT
