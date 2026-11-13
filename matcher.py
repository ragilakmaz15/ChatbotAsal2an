"""TF-IDF + cosine similarity: intent matching dan retrieval konteks."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import config
from knowledge_base import knowledge_base, documents
from preprocessing import preprocess

# Index 1: contoh kalimat per intent
_corpus, _labels = [], []
for _intent, _data in knowledge_base.items():
    for _ex in _data["examples"]:
        _corpus.append(preprocess(_ex))
        _labels.append(_intent)
_intent_vec = TfidfVectorizer()
_intent_matrix = _intent_vec.fit_transform(_corpus)

# Index 2: dokumen untuk konteks RAG
_doc_vec = TfidfVectorizer()
_doc_matrix = _doc_vec.fit_transform([preprocess(d["text"]) for d in documents])


def match_intent_nlp(user_input, threshold=config.HIGH_THRESHOLD):
    """Return (intent atau None, skor tertinggi)."""
    vec = _intent_vec.transform([preprocess(user_input)])
    sims = cosine_similarity(vec, _intent_matrix)[0]
    best = sims.argmax()
    if sims[best] >= threshold:
        return _labels[best], float(sims[best])
    return None, float(sims[best])


def retrieve_context(user_input, k=config.TOP_K):
    """Return list (dokumen, skor) untuk top-k dokumen yang cukup relevan."""
    vec = _doc_vec.transform([preprocess(user_input)])
    sims = cosine_similarity(vec, _doc_matrix)[0]
    top = sims.argsort()[::-1][:k]
    return [(documents[i], float(sims[i])) for i in top
            if sims[i] >= config.CONTEXT_MIN_SCORE]
