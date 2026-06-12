import streamlit as st
import random
from utils.ai_simulation import simulate_chat, simulate_klasifikasi, simulate_ringkasan, simulate_rekomendasi

def show_step3():
    st.subheader("Ceritakan kejadian")
    st.caption("Ceritakan sesuai kemampuanmu — AI akan membantu menyusunnya")

    st.session_state.kronologi = st.text_area(
        "📝 Kronologi kejadian",
        value=st.session_state.kronologi,
        placeholder="Contoh: Kemarin sore sekitar jam 5, saya berada di area parkir Fakultas X...",
        height=150
    )

    if st.button("🎤 Simulasi Voice Note (isi otomatis)"):
        samples = [
            "Saya mengalami pelecehan verbal dari seorang senior di kantin kampus saat jam makan siang kemarin.",
            "Teman saya mengalami intimidasi dari dosen saat jam kuliah berlangsung di ruang kelas gedung B.",
            "Saya melihat seorang mahasiswa menjadi korban diskriminasi di lingkungan asrama karena berasal dari suku dan latar belakang budaya yang berbeda."
        ]
        st.session_state.kronologi = random.choice(samples)
        st.rerun()

    st.session_state.waktu_lokasi = st.text_input(
        "📍 Waktu & lokasi kejadian",
        value=st.session_state.waktu_lokasi,
        placeholder="Contoh: Senin 9 Juni 2026, Area Parkir Gedung A"
    )

    st.divider()

    # AI Chat Assistant
    st.markdown("""
    <div class='ai-box'>
        <span class='ai-badge'>AI</span>
        <strong style='color:#c94f7c; margin-left:8px'>AI Chat Assistant</strong>
        <p style='font-size:13px;color:#888;margin-top:4px'>Ceritakan kepadaku, aku akan membantu</p>
    </div>
    """, unsafe_allow_html=True)

    for chat in st.session_state.chat_history:
        if chat["role"] == "ai":
            with st.chat_message("assistant", avatar="🤖"):
                st.write(chat["msg"])
        else:
            with st.chat_message("user", avatar="👤"):
                st.write(chat["msg"])

    chat_input = st.chat_input("Ketik pesanmu di sini...")
    if chat_input:
        st.session_state.chat_history.append({"role": "user", "msg": chat_input})
        with st.spinner("AI sedang membalas..."):
            resp = simulate_chat(chat_input)
        st.session_state.chat_history.append({"role": "ai", "msg": resp})
        st.rerun()

    st.divider()
    col_back, col_next = st.columns(2)
    with col_back:
        if st.button("← Kembali", use_container_width=True):
            st.session_state.step = 2
            st.rerun()
    with col_next:
        if st.button("Proses dengan AI →", type="primary", use_container_width=True):
            if not st.session_state.kronologi.strip():
                st.error("Silakan ceritakan kejadian terlebih dahulu.")
            else:
                with st.spinner("AI sedang memproses laporanmu..."):
                    st.session_state.hasil_klasifikasi = simulate_klasifikasi(
                        st.session_state.jenis, st.session_state.kronologi)
                    st.session_state.hasil_ringkasan = simulate_ringkasan(
                        st.session_state.jenis, st.session_state.mode,
                        st.session_state.kronologi, st.session_state.waktu_lokasi)
                    st.session_state.hasil_rekomendasi = simulate_rekomendasi(
                        st.session_state.jenis)
                st.session_state.step = 4
                st.rerun()
