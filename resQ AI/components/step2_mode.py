import streamlit as st

def show_step2():
    st.subheader("Pilih mode pelaporan")
    st.caption("Identitasmu sepenuhnya terlindungi jika memilih anonim")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔒 Anonim")
        st.write("Identitasmu tidak akan diketahui siapapun, termasuk Satgas PPKPT")
        if st.button("Pilih Anonim", use_container_width=True):
            st.session_state.mode = "Anonim"
            st.rerun()

    with col2:
        st.markdown("### 👤 Terbuka")
        st.write("Identitasmu diketahui oleh Satgas PPKPT untuk keperluan tindak lanjut")
        if st.button("Pilih Terbuka", use_container_width=True):
            st.session_state.mode = "Terbuka"
            st.rerun()

    if st.session_state.mode:
        st.success(f"✅ Mode dipilih: **{st.session_state.mode}**")
        if st.session_state.mode == "Terbuka":
            st.text_input("Nama lengkap kamu:", placeholder="Masukkan nama lengkap...")

    st.divider()
    col_back, col_next = st.columns(2)
    with col_back:
        if st.button("← Kembali", use_container_width=True):
            st.session_state.step = 1
            st.rerun()
    with col_next:
        if st.session_state.mode:
            if st.button("Lanjut →", type="primary", use_container_width=True):
                st.session_state.step = 3
                st.rerun()
