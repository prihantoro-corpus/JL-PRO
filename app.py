import streamlit as st

# Pengaturan Konfigurasi Halaman
st.set_page_config(
    page_title="JL-PRO: Japanese Lexical Profiler",
    page_icon="🇯🇵",
    layout="centered"
)

# Bagian Header/Judul
st.title("JL-PRO")
st.subheader("Model Automatic Japanese Lexical Profiler Pemelajar Bahasa Jepang berbasiskan Artificial Intelligence")

# Garis Pembatas
st.markdown("---")

# Pesan Status Pengembangan
st.info("Aplikasi akan tersedia di sini. Saat ini dalam pengembangan.")

# Deskripsi Singkat (Opsional)
st.write("""
Selamat datang di **JL-PRO**. Sistem ini dirancang untuk menganalisis profil leksikal 
bahasa Jepang menggunakan kecerdasan buatan guna membantu pemelajar memahami 
tingkat kesulitan dan distribusi kosakata dalam teks.
""")

# Footer
st.caption("© 2024 JL-PRO Development Team")
