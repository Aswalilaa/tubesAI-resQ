import streamlit as st

def show_step1():
    st.markdown("""
    <div class='darurat-box'>
        🚨 <strong style='color:#c94f7c'>Tombol Darurat</strong><br>
        <span style='font-size:13px;color:#888'>Hubungi Satgas PPKPT: (024) 7460012 | ppkpt@undip.ac.id</span>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Pilih jenis laporan")
    st.caption("Pilih kategori yang paling sesuai dengan pengalaman kamu")

    jenis_options = [
        "🤜 Kekerasan Fisik",
        "🧠 Kekerasan Psikis",
        "⚠️ Kekerasan Seksual",
        "👥 Perundungan",
        "🚫 Diskriminasi & Intoleransi",
        "📋 Lainnya"
    ]

    cols = st.columns(2)
    for i, opt in enumerate(jenis_options):
        with cols[i % 2]:
            if st.button(opt, key=f"jenis_{i}", use_container_width=True):
                st.session_state.jenis = opt.split(" ", 1)[1]

    if st.session_state.jenis:
        st.success(f"✅ Dipilih: **{st.session_state.jenis}**")
        if st.button("Lanjut →", type="primary", use_container_width=True):
            st.session_state.step = 2
            st.rerun()
