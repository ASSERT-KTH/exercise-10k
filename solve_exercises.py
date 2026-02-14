import os
import json
import glob
import requests
import re
from datetime import datetime

def get_model_name():
    serve_sh_path = "kth-inference/serve.sh"
    if not os.path.exists(serve_sh_path):
        return "RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic"
    
    with open(serve_sh_path, "r") as f:
        content = f.read()
        match = re.search(r'MODEL_NAME=\$\{1:-"([^"]+)"\}', content)
        if match:
            return match.group(1)
    return "RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic"

def call_vllm(prompt, model_name, url="http://localhost:8000/v1/chat/completions"):
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1024,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, json=payload, timeout=300)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error calling vLLM: {e}")
        return None

def main():
    model_name = get_model_name()
    print(f"Using model: {model_name}")
    
    output_dir = "answers/model"
    os.makedirs(output_dir, exist_ok=True)
    
    exercise_files = sorted(glob.glob("exercises/exercise_*.json"))
    
    for file_path in exercise_files:
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
                description = data.get("description")
                uniqid = data.get("id")
                
                if not uniqid:
                    # Fallback to extracting ID from filename if missing in JSON
                    match = re.search(r'exercise_(\d+)\.json', file_path)
                    uniqid = match.group(1) if match else os.path.basename(file_path)

                output_file = os.path.join(output_dir, f"{uniqid}.json")
                
                # Skip if already processed
                if os.path.exists(output_file):
                    print(f"Skipping {file_path}, already processed.")
                    continue

                if description:
                    print(f"--- Processing {file_path} (ID: {uniqid}) ---")
                    answer = call_vllm(description, model_name)
                    
                    if answer:
                        result = {
                            "prompt": description,
                            "answer": answer,
                            "timestamp": datetime.now().isoformat(),
                            "model": model_name
                        }
                        
                        with open(output_file, "w") as out_f:
                            json.dump(result, out_f, indent=2)
                        print(f"Saved to {output_file}")
                    else:
                        print(f"Failed to get answer for {file_path}")
                else:
                    print(f"No description found in {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    main()