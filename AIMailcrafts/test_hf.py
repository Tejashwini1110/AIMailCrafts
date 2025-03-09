import requests
api_url = "https://api-inference.huggingface.co/models/bigscience/bloom"
api_token = "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"  # Replace with your actual token
headers = {"Authorization": f"Bearer {api_token}"}
payload = {"inputs": "Write a professional email about a project update."}

response = requests.post(api_url, headers=headers, json=payload)
print(response.status_code, response.text)
