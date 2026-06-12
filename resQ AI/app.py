# Anggota Kelompok:
# 1. Aswalila Adha Putri Telaumbanua  (24060123120014)
# 2. Alodia Evelyn Pratikno           (24060124130087)
# 3. Arini Latifatul Qalbiah          (24060124140136)
# 4. Aprillia Abel Cleodora           (24060124140176)

import streamlit as st
from components.step1_jenis import show_step1
from components.step2_mode import show_step2
from components.step3_kronologi import show_step3
from components.step4_hasil import show_step4
from components.step5_selesai import show_step5

st.set_page_config(
    page_title="resQ AI - Platform Pelaporan Kekerasan Kampus",
    page_icon="🆘",
    layout="centered"
)

st.markdown("""
<style>
    .main { background-color: #FDF6F9; }
    .stButton > button {
        background-color: #c94f7c;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-size: 14px;
    }
    .stButton > button:hover { background-color: #a83d66; }
    .ai-box {
        background: #fff0f7;
        border: 1px solid #f7c0d8;
        border-radius: 12px;
        padding: 18px;
        margin: 12px 0;
    }
    .ai-badge {
        background: #c94f7c;
        color: white;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: bold;
    }
    .darurat-box {
        background: #fff0f7;
        border: 1.5px solid #f7c0d8;
        border-radius: 10px;
        padding: 14px 18px;
        margin-bottom: 20px;
    }
    .status-done { color: #c94f7c; font-weight: 600; }
    .status-pending { color: #aaa; }
</style>
""", unsafe_allow_html=True)

# inisialisasi session state
defaults = {
    "step": 1,
    "jenis": "",
    "mode": "",
    "kronologi": "",
    "waktu_lokasi": "",
    "chat_history": [
        {"role": "ai", "msg": "Halo, aku di sini untuk membantu. Ceritakan kejadian yang kamu alami, dan aku akan bantu menyusunnya. Kamu aman di sini 💙"}
    ],
    "hasil_klasifikasi": "",
    "hasil_ringkasan": "",
    "hasil_rekomendasi": [],
    "id_laporan": ""
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# header
st.markdown("""
<div style='display:flex; align-items:center; gap:10px; margin-bottom:8px'>
    <span style='font-size:26px; font-weight:700; color:#c94f7c'>resQ</span>
    <span style='font-size:18px; color:#c94f7c; font-weight:600'>AI</span>
    <span style='font-size:13px; color:#888; margin-left:4px'>Platform Pelaporan Kekerasan Kampus</span>
</div>
""", unsafe_allow_html=True)

# progress bar
step_labels = ["Jenis Laporan", "Mode", "Kronologi", "Hasil AI", "Selesai"]
st.progress((st.session_state.step - 1) / 4)
st.caption(f"Langkah {st.session_state.step} dari 5 — {step_labels[st.session_state.step - 1]}")
st.divider()

# routing ke step yang aktif
if st.session_state.step == 1:
    show_step1()
elif st.session_state.step == 2:
    show_step2()
elif st.session_state.step == 3:
    show_step3()
elif st.session_state.step == 4:
    show_step4()
elif st.session_state.step == 5:
    show_step5()