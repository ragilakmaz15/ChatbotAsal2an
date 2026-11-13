"""Konfigurasi: threshold, parameter RAG, dan pembacaan environment variable."""
import os

try:
    from dotenv import load_dotenv
    load_dotenv()          # baca file .env (jika ada)
except ImportError:
    pass                   # tanpa python-dotenv, pakai variabel sistem saja

# --- Kredensial LLM (Gemini native API; dari environment, bukan ditulis di kode) ---
API_KEY = os.environ.get("LLM_API_KEY")
MODEL = os.environ.get("LLM_MODEL", "gemini-2.5-flash")
API_URL = os.environ.get("LLM_API_URL") or (
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
)
TIMEOUT = 15

# --- Parameter pencocokan & RAG ---
HIGH_THRESHOLD = 0.5       # skor >= ini: jawab langsung dari knowledge base
CONTEXT_MIN_SCORE = 0.08   # skor dokumen < ini: dianggap tidak relevan (LLM tidak dipanggil)
TOP_K = 3                  # jumlah dokumen konteks yang dikirim ke LLM
NO_ANSWER_TOKEN = "TIDAK_TAHU"

FALLBACK_RESPONSE = (
    "Maaf, saya tidak tahu jawabannya berdasarkan informasi yang saya miliki. "
    "Silakan cek unp.ac.id atau hubungi admin kampus."
)