"""Pemanggilan Gemini (endpoint native) dengan prompt yang membatasi jawaban hanya dari konteks."""
import requests

import config

SYSTEM_PROMPT = f"""Kamu adalah asisten informasi Universitas Negeri Padang (UNP).
ATURAN KETAT:
1. Jawab HANYA berdasarkan KONTEKS yang diberikan.
2. Dilarang memakai pengetahuan di luar konteks, dilarang menebak.
3. Jika konteks tidak memuat jawaban, balas persis dengan satu kata: {config.NO_ANSWER_TOKEN}
4. Jawab singkat dalam bahasa Indonesia."""


def build_prompt(question, context_docs):
    ctx = "\n".join(f"[{d['id']}] {d['text']}" for d, _ in context_docs)
    return f"KONTEKS:\n{ctx}\n\nPERTANYAAN: {question}\n\nJAWABAN:"


def build_payload(question, context_docs):
    return {
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": [
            {"role": "user", "parts": [{"text": build_prompt(question, context_docs)}]}
        ],
        "generationConfig": {"temperature": 0},
    }


def ask_llm(question, context_docs):
    """Return teks jawaban LLM, atau None jika API tidak tersedia/gagal."""
    if not config.API_KEY:
        return None
    try:
        r = requests.post(
            config.API_URL,
            headers={"x-goog-api-key": config.API_KEY,
                     "Content-Type": "application/json"},
            json=build_payload(question, context_docs),
            timeout=config.TIMEOUT,
        )
        r.raise_for_status()
        return r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except (requests.exceptions.RequestException, ValueError, KeyError, IndexError):
        return None