# Death Admin Orchestrator 🏛️

A production-grade ingestion engine designed to parse complex, multi-format death certificates with a **95%+ accuracy target**.

## 🛠️ Architectural Philosophy
This engine is built to solve the "messy data" problem in institutional death administration. It moves away from simple OCR and utilizes a **Reasoning-First** approach:

* **Inference Engine:** Uses **GPT-OSS 120B** (Open-weight) to interpret context, not just text.
* **State Integrity:** Implements strict **Pydantic schemas** to ensure that extracted data (SSNs, Licenses, DODs) meets legal formatting standards before being saved.
* **Fault-Tolerance:** Built-in **timeout (60s)** and **exponential backoff retry logic** to handle high-volume API throughput without data loss.

## 🚀 Technical Features
- **Deterministic JSON Output:** Guarantees structured data for downstream ERP/Legal systems.
- **Privacy-Centric:** Designed for local-first or private-cloud inference to protect PII.
- **Resilient Pipeline:** Handles network latency and inference delays via a custom wrapper.

## 🚦 Getting Started
1. **Clone & Install:** `pip install -r requirements.txt`
2. **Configure Ollama:** Ensure `gpt-oss:120b-cloud` is pulled and running.
3. **Execute:** `python parser.py`

## 📈 Roadmap
- **Vision Integration:** Implementing local Vision-Language Models (Llama 3.2-Vision) for spatial coordinate mapping of physical stamps.
- **Quality Assurance:** Human-in-the-loop (HITL) flagging for any extraction confidence scores below 0.90.
- **Institutional Mapping:** Native export filters for standard funeral home management software.
