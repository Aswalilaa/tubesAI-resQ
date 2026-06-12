# resQ — Platform Pelaporan Kekerasan dan Pelecehan di Kampus
> *Laporkan. Aman. Terstruktur.*

Platform pelaporan kekerasan dan pelecehan di lingkungan kampus berbasis AI.

## Anggota Kelompok resQ
1. Aswalila Adha Putri Telaumbanua  (24060123120014)
2. Alodia Evelyn Pratikno           (24060124130087)
3. Arini Latifatul Qalbiah          (24060124140136)
4. Aprillia Abel Cleodora           (24060124140176)

## Deskripsi Proyek
Banyak korban kekerasan kampus yang akhirnya memilih diam, bukan karena tidak mau melapor, tapi karena prosesnya membingungkan, terasa tidak aman, atau tidak tahu harus mulai dari mana. resQ AI dibuat untuk menjawab masalah itu. Aplikasi ini membantu korban maupun saksi untuk melaporkan kejadian secara lebih mudah dan terstruktur, dengan bantuan AI yang mendampingi dari awal sampai laporan terkirim. Hasil laporan kemudian bisa langsung ditindaklanjuti oleh Satgas PPKPT Undip. Prototype ini dibuat dengan **Streamlit (Python)**, dengan alur 5 langkah yang dibuat sesederhana mungkin supaya tidak memberatkan pengguna.

---

## Fitur Utama

## Fitur AI
- AI Chat Assistant untuk membantu pengguna menyusun kronologi kejadian 
- AI Klasifikasi Kekerasan untuk mengidentifikasi jenis kekerasan secara otomatis 
- AI Ringkasan Laporan untuk merangkum laporan menjadi terstruktur 
- AI Rekomendasi Bantuan untuk memberikan rekomendasi bantuan yang sesuai 
- AI Speech-to-Text untuk mensimulasi input via voice note 

### Fitur Non-AI
- **Tombol Darurat** — Menampilkan kontak Satgas PPKPT Undip secara langsung
- **Mode Anonim / Terbuka** — Pengguna dapat memilih apakah identitasnya diketahui pihak Satgas atau tidak
- **Tracking Status Laporan** — Menampilkan tahapan penanganan laporan setelah dikirim
- **ID Laporan Unik** — Setiap laporan yang dikirim mendapatkan ID unik sebagai bukti penerimaan

---

## Alur Aplikasi
```
Langkah 1 — Pilih Jenis Laporan
    ↓
Langkah 2 — Pilih Mode Pelaporan (Anonim / Terbuka)
    ↓
Langkah 3 — Input Kronologi + AI Chat Assistant
    ↓
Langkah 4 — Tinjau Hasil AI (Klasifikasi + Ringkasan + Rekomendasi)
    ↓
Langkah 5 — Kirim Laporan + Tracking Status
```

---

## Struktur File

```
resQ AI/
├── app.py                      # Entry point & routing utama antar langkah
├── requirements.txt            # Daftar library yang dibutuhkan
├── README.md                   # Dokumentasi proyek
├── components/
│   ├── __init__.py
│   ├── step1_jenis.py          # Langkah 1: Pilih jenis laporan
│   ├── step2_mode.py           # Langkah 2: Pilih mode pelaporan
│   ├── step3_kronologi.py      # Langkah 3: Input kronologi + AI Chat Assistant
│   ├── step4_hasil.py          # Langkah 4: Tinjau hasil AI + konfirmasi laporan
│   └── step5_selesai.py        # Langkah 5: Konfirmasi pengiriman + tracking status
└── utils/
    ├── __init__.py
    └── ai_simulation.py        # Fungsi simulasi AI: klasifikasi, ringkasan,
                                #   rekomendasi, dan chat assistant
```

---

## Cara Menjalankan

### Prasyarat
- Python 3.8 atau lebih baru
- pip (Python package manager)

### Langkah Instalasi
**1. Clone atau ekstrak repository ini** : cd "resQ AI"
**2. Install library yang dibutuhkan** : pip install streamlit
**3. Jalankan aplikasi** : streamlit run app.py
**4. Buka di browser** : 
Streamlit otomatis buka browser dan langsung ke aplikasinya. Kalau tidak kebuka sendiri, buka manual di:
```
http://localhost:8501
```

## Teknologi yang Digunakan

- **Python 3** — bahasa pemrograman utama
- **Streamlit** — framework untuk bikin tampilan web-nya
- **Figma** — buat desain wireframe dan mockup UI
- **ChatGPT & AI coding assistant** — dipakai selama proses pengembangan untuk eksplorasi ide dan bantu nulis kode

---
