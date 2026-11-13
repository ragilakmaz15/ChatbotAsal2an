"""Orkestrasi alur: KB langsung -> RAG terbatas -> fallback."""
import random

import config
from knowledge_base import knowledge_base
from matcher import match_intent_nlp, retrieve_context
from llm_client import ask_llm


def get_response(user_input):
    """Return (jawaban, mode) dengan mode: 'kb' | 'rag' | 'unknown'."""
    intent, _ = match_intent_nlp(user_input)
    if intent is not None:                                  # skor tinggi
        return random.choice(knowledge_base[intent]["responses"]), "kb"

    context = retrieve_context(user_input)                  # skor rendah
    if not context:                                         # konteks tidak relevan
        return config.FALLBACK_RESPONSE, "unknown"

    reply = ask_llm(user_input, context)
    if reply is None or config.NO_ANSWER_TOKEN in reply.upper():
        return config.FALLBACK_RESPONSE, "unknown"          # API gagal / LLM tidak tahu
    return reply, "rag"
