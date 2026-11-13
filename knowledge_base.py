"""Data chatbot. Tambah intent/dokumen di sini TANPA mengubah file lain.

PENTING: isi di bawah adalah CONTOH. Verifikasi dan lengkapi dari unp.ac.id.
"""

# Intent -> contoh kalimat (untuk TF-IDF) + jawaban langsung
knowledge_base = {
    "greeting": {
        "examples": ["halo", "hai", "selamat pagi", "selamat siang", "assalamualaikum"],
        "responses": ["Halo! Saya chatbot informasi UNP. Ada yang bisa saya bantu?"],
    },
    "lokasi_kampus": {
        "examples": ["lokasi kampus", "alamat kampus unp", "dimana letak kampus",
                     "kampus air tawar ada di mana"],
        "responses": ["Kampus utama UNP berada di Air Tawar, Padang, Sumatera Barat. "
                      "[VERIFIKASI alamat lengkap di unp.ac.id]"],
    },
    "jadwal_kuliah": {
        "examples": ["jadwal kuliah", "jadwal kelas", "kapan kuliah dimulai",
                     "jam kuliah hari ini"],
        "responses": ["Jadwal kuliah dapat dilihat di portal akademik UNP "
                      "pada menu jadwal/KRS. [VERIFIKASI nama portal]"],
    },
    "kontak_admin": {
        "examples": ["kontak admin", "hubungi admin", "nomor telepon admin",
                     "email admin akademik"],
        "responses": ["Kontak resmi UNP dapat dilihat di website unp.ac.id. "
                      "[ISI email/telepon resmi]"],
    },
    "terima_kasih": {
        "examples": ["terima kasih", "makasih", "thanks"],
        "responses": ["Sama-sama! Senang bisa membantu."],
    },
    "goodbye": {
        "examples": ["bye", "sampai jumpa", "keluar", "exit"],
        "responses": ["Sampai jumpa! Semoga harimu menyenangkan."],
    },
}

# Dokumen lebih panjang: sumber KONTEKS untuk LLM (RAG)
documents = [
    {"id": "doc_profil",
     "text": "Universitas Negeri Padang (UNP) adalah perguruan tinggi negeri di Padang, "
             "Sumatera Barat. [ISI: sejarah singkat, akreditasi, visi misi]"},
    {"id": "doc_fakultas",
     "text": "Fakultas di UNP antara lain FIP, FBS, FMIPA, FT, FIK, FEB, FISIP, dan FPsi. "
             "[VERIFIKASI daftar fakultas terbaru]"},
    {"id": "doc_pendaftaran",
     "text": "Pendaftaran mahasiswa baru UNP dilakukan melalui jalur seleksi nasional "
             "dan mandiri. [ISI: jalur, jadwal, syarat dari sumber resmi]"},
    {"id": "doc_ukt",
     "text": "Biaya kuliah mahasiswa PTN menggunakan skema UKT (Uang Kuliah Tunggal) "
             "yang dibagi per kelompok. [ISI: besaran UKT UNP resmi]"},
    {"id": "doc_beasiswa",
     "text": "Mahasiswa UNP dapat mengajukan beasiswa seperti KIP Kuliah. "
             "[ISI: jenis beasiswa dan prosedur dari sumber resmi]"},
    {"id": "doc_perpustakaan",
     "text": "Perpustakaan UNP melayani peminjaman buku dan akses koleksi digital. "
             "[ISI: jam operasional resmi]"},
]

# Jawaban KB ikut menjadi dokumen agar bisa dipakai sebagai konteks
for _intent, _data in knowledge_base.items():
    for _i, _resp in enumerate(_data["responses"]):
        documents.append({"id": f"kb_{_intent}_{_i}", "text": _resp})
