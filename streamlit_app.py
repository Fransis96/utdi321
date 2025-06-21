import streamlit as st
from login_module import fill_and_submit_form

st.title("🔐 Login Otomatis ke ELA UTDI")

# Bungkus dengan form
with st.form("login_form"):
    username = st.text_input("Masukkan Username")
    password = st.text_input("Masukkan Password", type="password")
    submit = st.form_submit_button("Login Sekarang")

# Submit diproses di luar blok 'with'
if submit:
    if not username or not password:
        st.warning("Harap isi username dan password!")
    else:
        st.info("🚀 Memulai login...")
        success, result = fill_and_submit_form('siakad', username, password)

        if success:
            st.success("✅ Login berhasil.")
            st.image(result, caption="Hasil Screenshot")
        else:
            st.error(f"❌ Gagal login: {result}")
