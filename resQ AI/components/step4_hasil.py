import streamlit as st

def show_step4():
    st.subheader("Tinjau hasil laporan AI")
    st.caption("AI telah memproses laporanmu — tinjau dan kirimkan")

    st.markdown(
        f"<span style='background:#fef0f5;color:#c94f7c;border:1px solid #f7c0d8;"
        f"border-radius:20px;padding:4px 14px;font-size:13px;font-weight:600'>"
        f"Kategori: {st.session_state.jenis}</span>",
        unsafe_allow_html=True
    )
    st.write("")

    with st.expander("🔍 AI Klasifikasi Kekerasan", expanded=True):
        st.markdown(st.session_state.hasil_klasifikasi)

    with st.expander("📄 AI Ringkasan Laporan", expanded=True):
        st.markdown(st.session_state.hasil_ringkasan)

    with st.expander("💡 AI Rekomendasi Bantuan", expanded=True):
        for rec in st.session_state.hasil_rekomendasi:
            col1, col2 = st.columns([1, 8])
            with col1:
                st.markdown(f"<div style='font-size:24px'>{rec['icon']}</div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"**{rec['title']}**")
                st.caption(rec['desc'])

    st.divider()
    col_back, col_next = st.columns(2)
    with col_back:
        if st.button("← Kembali", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
    with col_next:
        if st.button("✅ Kirim Laporan", type="primary", use_container_width=True):
            import random
            st.session_state.id_laporan = f"RQ-2026-{random.randint(1000,9999)}"
            st.session_state.step = 5
            st.rerun()
