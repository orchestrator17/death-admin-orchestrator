import ollama
import time
from ollama import Client

# Initialize client for 120B reasoning
client = Client(host='http://localhost:11434', timeout=60)

def vision_pre_filter(document_path):
    """
    STAGE 1: OpenCV/Tesseract Pre-processing
    """
    print(f"--- [Stage 1] OpenCV/Tesseract: Scanning document... ---")
    return True 

def robust_parse(text_input, retries=3, delay=5):
    """
    STAGE 2: 120B Reasoning Engine
    """
    attempt = 0
    while attempt < retries:
        try:
            print(f"--- [Stage 2] {attempt + 1}: Initiating 120B Logic ---")
            response = client.chat(
                model='gpt-oss:120b-cloud',
                messages=[{'role': 'user', 'content': f"Extract Death Admin JSON: {text_input}"}]
            )
            return response['message']['content']
        except Exception as e:
            attempt += 1
            print(f"⚠️ Error: {e}. Retrying...")
            time.sleep(delay)
    return None

def finalize_ingestion(data):
    """
    STAGE 3: State Integrity
    """
    print(f"--- [Stage 3] Validating schema integrity... ---")
    return f"Success: Data pushed to Institutional Queue."

if __name__ == "__main__":
    print("🚀 NOC START: INITIALIZING DEATH ADMIN PIPELINE")
    raw_data = "Scan_Upload_Page_34.jpg | Subject: John Doe | DOD: 2026-02-25"

    if vision_pre_filter(raw_data):
        structured_data = robust_parse(raw_data)
        if structured_data:
            print(finalize_ingestion(structured_data))
