# Death Admin Orchestrator 🏛️

A production-grade ingestion engine designed to parse complex, multi-format death certificates with a **95%+ accuracy target** through a hybrid Visual-Reasoning pipeline.

## 🛠️ Architectural Philosophy: The Hybrid Pipeline
To solve the **"Ream of Chaos"** problem (bulk PDF uploads containing mixed administrative noise), this engine utilizes a **Tiered Intelligence** approach. We move beyond probabilistic parsing to deterministic orchestration:

* **Stage 1: The Vision Filter (OpenCV + Tesseract)**
    * **Cost Optimization:** Acts as a low-latency "Bouncer" to identify document types and de-skew/de-noise analog scans.
    * **Semantic Routing:** Filters out "noise" (invoices, medical records) using Tesseract for basic keyword-triggering before high-cost reasoning kicks in.
* **Stage 2: The Reasoning Engine (GPT-OSS 120B)**
    * **Contextual Extraction:** Handles the "Heavy Lifting" of interpreting legal nuances, handwritten notes, and entity relationships that standard OCR fails to capture.
* **Stage 3: State Integrity (Pydantic)**
    * **Schema Enforcement:** Strict validation to ensure SSNs, DODs, and Case Numbers meet institutional standards before database injection.

## 🚀 Technical Features
* **Deterministic JSON Output:** Guarantees structured data for downstream ERP/Legal systems.
* **Privacy-Centric:** Designed for local-first or private-cloud inference to protect PII.
* **Fault-Tolerant:** Exponential backoff and 60s timeout wrappers to ensure zero-fail ingestion.
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
* **[Sprint Week 2] Institutional Templates:** Native mapping for 15+ state-specific death certificate layouts.
* **[Sprint Week 3] HITL Queue:** Human-in-the-loop dashboard for flagging extraction confidence scores below **0.90**.
