import requests
import config

print("Model :", config.MODEL)
print("Key   :", "terbaca" if config.API_KEY else "KOSONG (cek file .env)")

r = requests.post(
    config.API_URL,
    headers={"x-goog-api-key": config.API_KEY or "",
             "Content-Type": "application/json"},
    json={"contents": [{"role": "user", "parts": [{"text": "Balas satu kata: halo"}]}]},
    timeout=config.TIMEOUT,
)
print("Status:", r.status_code)
print(r.text[:600])