import requests

api_url = "https://api-inference.huggingface.co/models/bigscience/bloom"
api_token = "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"  # Replace with your actual token
headers = {"Authorization": f"Bearer {api_token}"}
payload = {"inputs": "Write a professional email about a project update."}

response = requests.post(api_url, headers=headers, json=payload)

if response.status_code == 200:
    print("✅ API is working:", response.json())
else:
    print(f"❌ Error {response.status_code}: {response.text}")
