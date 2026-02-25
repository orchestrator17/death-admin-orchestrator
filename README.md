# Death Admin Orchestrator 🏛️

A production-grade ingestion engine designed to parse complex, multi-format death certificates with a **95%+ accuracy target** through a hybrid Visual-Reasoning pipeline.

## 🛠️ Architectural Philosophy: The Hybrid Pipeline
To solve the "Ream of Chaos" problem (50+ page uploads with analog anomalies), this engine utilizes a **Tiered Intelligence** approach. We don't just "read" text; we orchestrate it:

* **Stage 1: The Vision Filter (OpenCV + Tesseract):** * **Cost Optimization:** Acts as a low-latency "Bouncer" to identify document types and de-skew/de-noise analog scans.
    * **Semantic Routing:** Filters out "noise" (invoices, medical records) using Tesseract for basic keyword-triggering before high-cost reasoning kicks in.
* **Stage 2: The Reasoning Engine (GPT-OSS 120B):** * **Contextual Extraction:** Handles the "Heavy Lifting" of interpreting legal nuances, handwritten notes, and entity relationships that standard OCR misses.
* **Stage 3: State Integrity (Pydantic):** * Enforces strict schemas to ensure DODs, SSNs, and Case Numbers meet institutional standards.

## 🚀 Technical Features
- **Deterministic JSON Output:** Guarantees structured data for downstream ERP/Legal systems.
- **Privacy-Centric:** Designed for local-first or private-cloud inference to protect PII.
- **Fault-Tolerant:** Exponential backoff and 60s timeout wrappers to ensure zero-fail ingestion.
- **Pre-Processing Logic:** OpenCV integration points for spatial coordinate mapping and "Handwriting-First" de-noising.

## 🚦 Getting Started
1. **Clone & Install:** `pip install -r requirements.txt`
2. **Configure Ollama:** Ensure `gpt-oss:120b-cloud` is pulled and running.
3. **Execute:** `python parser.py`

## 📈 Roadmap: The "Alpha" Build
- **[Q2 2026] OpenCV Spatial Mapping:** Automated "Crop & Extract" for signature and stamp verification.
- **[Q2 2026] Tesseract Pre-Filter:** Implementing a "cheap" OCR gate to reduce LLM token usage by 60% on multi-page uploads.
- **[Q3 2026] HITL Queue:** Human-in-the-loop flagging for confidence scores < 0.90.
