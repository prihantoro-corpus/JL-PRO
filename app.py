import streamlit as st

# Pengaturan Konfigurasi Halaman
st.set_page_config(
    page_title="JL-PRO: Japanese Lexical Profiler",
    page_icon="🇯🇵",
    layout="centered"
)

# Judul Utama
st.title("JL-PRO")
st.markdown("### Model Automatic Japanese Lexical Profiler Pemelajar Bahasa Jepang berbasiskan Artificial Intelligence")

st.markdown("---")

# Status Pengembangan
st.warning("⚠️ **Status:** Akan tersedia di sini. Saat ini dalam pengembangan.")

st.write("""
Selamat datang di **JL-PRO**. Sistem ini dirancang untuk menganalisis profil leksikal 
bahasa Jepang menggunakan kecerdasan buatan guna membantu pemelajar memahami 
tingkat kosa kata secara otomatis.
""")

st.write("---")

# Bagian Clickable Labels (Dokumentasi)
st.markdown("### Dokumentasi Proyek")
col1, col2 = st.columns(2)

with col1:
    # Ganti URL di dalam tanda kurung dengan link file Anda yang sebenarnya
    st.link_button("📄 DOKUMEN FEASIBILITY STUDY", "https://github.com/username/repo/blob/main/feasibility-study.pdf", use_container_width=True)

with col2:
    # Ganti URL di dalam tanda kurung dengan link file Anda yang sebenarnya
    st.link_button("📘 USERS MANUAL", "https://github.com/username/repo/blob/main/users-manual.pdf", use_container_width=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2024 JL-PRO Development Team")
