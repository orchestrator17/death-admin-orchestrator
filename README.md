# Death Admin Orchestrator 🏛️

A production-grade ingestion engine designed to parse complex, multi-format death certificates with a **95%+ accuracy target** through a hybrid Visual-Reasoning pipeline.

## 🛠️ Architectural Philosophy: The Hybrid Pipeline
To solve the **"Ream of Chaos"** problem (bulk PDF uploads containing mixed administrative noise), this engine utilizes a **Tiered Intelligence** approach. We move beyond probabilistic parsing to deterministic orchestration.



### The Three-Tier Logic
* **Stage 1: The Vision Filter (OpenCV + Tesseract)**
    * **Cost Optimization:** Acts as a low-latency "Bouncer" to identify document types and de-skew/de-noise analog scans.
    * **Semantic Routing:** Filters out "noise" (invoices, medical records) using Tesseract for basic keyword-triggering before high-cost reasoning kicks in.
* **Stage 2: The Reasoning Engine (GPT-OSS 120B)**
    * **Contextual Extraction:** Handles the "Heavy Lifting" of interpreting legal nuances, handwritten notes, and entity relationships that standard OCR fails to capture.
* **Stage 3: State Integrity (Pydantic)**
    * **Schema Enforcement:** Strict validation to ensure SSNs, DODs, and Case Numbers meet institutional standards. LLM output is treated as **Unverified Telemetry** until it passes this deterministic gate.

## 🛡️ Scalability & Platform Governance (Staff-Level Design)
While this POC is currently configured for high-fidelity extraction, the architecture is built for enterprise-grade horizontal scaling:

* **State Persistence:** Designed to transition from local memory to **Redis MULTI/EXEC** distributed locking, ensuring "Exactly-Once" processing across worker clusters.
* **Idempotent Ingestion:** Every document hash is tracked to prevent duplicate processing costs and state-drift in high-volume environments.
* **The "Paved Road" Middleware:** The parser logic is decoupled from the orchestration layer. This allows product teams to drop in new document schemas (Wills, Deeds, Invoices) with 0% refactoring of the core ingestion safety-net.
* **Fault-Tolerant Patterns:** Implements exponential backoff and 60s timeout wrappers to ensure zero-fail ingestion during API or resource contention.

## 🚀 Technical Features
* **Deterministic JSON Output:** Guarantees structured data for downstream ERP/Legal systems.
* **Privacy-Centric:** Designed for local-first or private-cloud inference to protect PII.
* **Observability-Ready:** Structured logging and telemetry hooks designed for Prometheus/Grafana integration to monitor extraction latency and token efficiency.
* **Modular Orchestration:** Clean separation of concerns between the **Orchestrator** (Flow Logic) and the **Parser** (Inference).

## 🚦 Getting Started
1.  **Clone & Install:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configure Ollama:** Ensure `gpt-oss:120b-cloud` is pulled and running locally.
3.  **Execute Orchestrator:**
    ```bash
    python orchestrator.py
    ```

## 📈 Roadmap: The "Founding CTO" Sprint
* **[Sprint Week 1] OpenCV Spatial Mapping:** Automated "Crop & Extract" for physical signatures and official county stamps.
* **[Sprint Week 1] Tesseract Pre-Filter:** Implementing a "cheap" OCR gate to reduce LLM token usage by **60%** on multi-page "Ream" uploads.
* **[Scaling] Redis Distributed Task Queue:** Transitioning local `asyncio` loops to a distributed Celery/Redis architecture to handle 10k+ concurrent document uploads.
* **[Observability] Data Drift Monitoring:** Implementing automated "Golden Set" testing to detect when LLM updates degrade extraction accuracy.
* **[Sprint Week 3] HITL Queue:** Human-in-the-loop dashboard for flagging extraction confidence scores below **0.90**.
