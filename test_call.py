import requests

data = {"text": "I feel like I'm failing at everything."}
res = requests.post("http://127.0.0.1:8000/cbt/analyze", json=data)

print("✅ Status:", res.status_code)
print("📦 Response:", res.text)
