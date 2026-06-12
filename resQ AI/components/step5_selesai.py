import streamlit as st
from datetime import datetime

def show_step5():
    st.markdown("""
    <div style='text-align:center; padding:20px 0'>
        <div style='font-size:52px'>✅</div>
        <div style='font-size:22px; font-weight:600; color:#2c1a24; margin:10px 0 6px'>Laporan Terkirim!</div>
        <div style='font-size:14px; color:#888'>Suaramu sudah kami terima dan akan ditindaklanjuti</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"<div style='background:#fef0f5;border:1px solid #f7c0d8;border-radius:8px;"
        f"padding:10px 20px;text-align:center;font-size:15px;font-weight:600;"
        f"color:#c94f7c;margin-bottom:20px'>ID Laporan: {st.session_state.id_laporan}</div>",
        unsafe_allow_html=True
    )

    st.markdown("#### 📋 Ringkasan")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Jenis Kekerasan", st.session_state.jenis)
        st.metric("Mode Pelaporan", st.session_state.mode)
    with col2:
        st.metric("Waktu & Lokasi", st.session_state.waktu_lokasi or "Tidak disebutkan")
        st.metric("Dikirim pada", datetime.now().strftime("%d/%m/%Y %H:%M"))

    st.divider()
    st.markdown("#### 📊 Status Laporan")

    statuses = [
        ("✅", "Laporan Diterima", datetime.now().strftime("%d/%m/%Y %H:%M"), True),
        ("⏳", "Laporan Diverifikasi", "Menunggu tindakan Satgas PPKPT", False),
        ("⏳", "Laporan dalam Penanganan", "—", False),
        ("⏳", "Laporan Selesai", "—", False),
    ]
    for icon, label, waktu, done in statuses:
        col1, col2 = st.columns([1, 8])
        with col1:
            st.markdown(f"<div style='font-size:20px;text-align:center'>{icon}</div>", unsafe_allow_html=True)
        with col2:
            if done:
                st.markdown(f"<span class='status-done'>{label}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"<span class='status-pending'>{label}</span>", unsafe_allow_html=True)
            st.caption(waktu)

    st.divider()
    st.markdown("#### 💙 Butuh Dukungan?")
    for icon, title, desc in [
        ("🧠", "Konsultasi Psikologi Online", "Bicara dengan psikolog kampus secara anonim"),
        ("📞", "Satgas PPKPT Undip", "ppkpt@undip.ac.id · (024) 7460012"),
        ("🆘", "SAPA 129 — KEMENPPPA", "Hotline nasional kekerasan terhadap perempuan dan anak"),
    ]:
        col1, col2 = st.columns([1, 8])
        with col1:
            st.markdown(f"<div style='font-size:22px'>{icon}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"**{title}**")
            st.caption(desc)

    st.divider()
    if st.button("🔄 Buat Laporan Baru", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
