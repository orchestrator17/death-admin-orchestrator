import ollama
import time
from ollama import Client

# 1. Initialize the client with a specific timeout (e.g., 60 seconds for 120B reasoning)
client = Client(host='http://localhost:11434', timeout=60)

def robust_parse(text_input, retries=3, delay=5):
    attempt = 0
    while attempt < retries:
        try:
            print(f"--- [Attempt {attempt + 1}] Initiating Reasoning Logic ---")
            
            response = client.chat(
                model='gpt-oss:120b-cloud',
                messages=[{'role': 'user', 'content': f"Extract JSON: {text_input}"}]
            )
            
            return response['message']['content']
            
        except Exception as e:
            attempt += 1
            print(f"⚠️ Error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            
    print("❌ Max retries exceeded. Manual intervention required.")
    return None

# Tests robust engine
sample = "Death Cert: John Doe, DOD 2026-02-25"
result = robust_parse(sample)
print(result)
