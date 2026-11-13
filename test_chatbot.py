"""Pengujian akurasi intent matching (seperti Percobaan 6)."""
from matcher import match_intent_nlp

# (input, intent yang diharapkan)
test_cases = [
    ("halo", "greeting"),
    ("kapan jadwal kuliah semester ini", "jadwal_kuliah"),
    ("dimana letak kampus unp", "lokasi_kampus"),
    ("saya mau hubungi admin", "kontak_admin"),
    ("terima kasih banyak", "terima_kasih"),
    ("sampai jumpa", "goodbye"),
    ("fakultas apa saja yang ada di unp", None),   # harus lewat RAG
    ("bagaimana cara daftar beasiswa", None),      # harus lewat RAG
    ("bagaimana cuaca hari ini", None),            # di luar cakupan
]

benar = 0
for teks, expected in test_cases:
    hasil, skor = match_intent_nlp(teks)
    ok = hasil == expected
    benar += ok
    print(f"[{'BENAR' if ok else 'SALAH'}] '{teks}' -> {hasil} "
          f"(skor {skor:.2f}), seharusnya {expected}")

print(f"\nAkurasi intent matching: {benar / len(test_cases) * 100:.1f}% "
      f"({benar}/{len(test_cases)})")
