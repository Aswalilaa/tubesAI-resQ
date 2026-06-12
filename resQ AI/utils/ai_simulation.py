import time
import random

def simulate_klasifikasi(jenis, kronologi):
    time.sleep(1.2)
    return (
        f"Berdasarkan deskripsi yang diberikan, kasus ini termasuk dalam kategori **{jenis}**.\n\n"
        f"**Indikator utama:** Terdapat tindakan yang bersifat merugikan dan tidak menyenangkan "
        f"bagi korban, dilakukan secara sengaja, dan terjadi di lingkungan akademik kampus.\n\n"
        f"**Relevansi regulasi:** Kasus ini relevan dengan Permendikbudristek No. 30 Tahun 2021 "
        f"tentang Pencegahan dan Penanganan Kekerasan di Lingkungan Perguruan Tinggi."
    )

def simulate_ringkasan(jenis, mode, kronologi, waktu_lokasi):
    time.sleep(1.0)
    return (
        f"**Ringkasan Laporan resQ AI**\n\n"
        f"- **Jenis Kasus:** {jenis}\n"
        f"- **Mode Pelaporan:** {mode}\n"
        f"- **Waktu & Lokasi:** {waktu_lokasi if waktu_lokasi else 'Tidak disebutkan'}\n\n"
        f"**Kronologi Singkat:**\n{kronologi}\n\n"
        f"Laporan ini telah disusun ulang secara terstruktur untuk memudahkan "
        f"proses tindak lanjut oleh Satgas PPKPT Universitas Diponegoro."
    )

def simulate_rekomendasi(jenis):
    time.sleep(0.8)
    return [
        {"icon": "🧠", "title": "Konsultasi Psikologi", "desc": "Hubungi layanan konseling kampus untuk pendampingan emosional"},
        {"icon": "⚖️", "title": "Konsultasi Hukum", "desc": "Dapatkan informasi tentang hak-hak hukummu sebagai korban"},
        {"icon": "📞", "title": "Satgas PPKPT Undip", "desc": "ppkpt@undip.ac.id · (024) 7460012"},
        {"icon": "🆘", "title": "SAPA 129 — KEMENPPPA", "desc": "Hotline nasional perlindungan perempuan dan anak"},
    ]

def simulate_chat(pesan):
    time.sleep(0.8)
    responses = [
        "Terima kasih sudah mau bercerita. Kamu sangat berani. Apakah kamu bisa menceritakan lebih detail mengenai waktu dan lokasi kejadian?",
        "Aku dengar kamu. Pengalaman seperti ini memang berat. Apakah ada saksi yang melihat kejadian tersebut?",
        "Kamu tidak sendirian. Apakah kamu mengenal pelaku tersebut? Misalnya teman, senior, atau dosen?",
        "Informasi yang kamu berikan sangat membantu. Apakah ada bukti seperti pesan, foto, atau rekaman yang bisa dilampirkan?",
    ]
    return random.choice(responses)