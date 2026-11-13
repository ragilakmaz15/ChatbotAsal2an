"""Normalisasi teks input pengguna."""
import re


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()
