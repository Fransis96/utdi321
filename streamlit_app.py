from login_module import fill_and_submit_form  # Import fungsi dari file

...

if submit and username and password:
    st.info("🚀 Memulai login...")
    success, result = fill_and_submit_form('siakad', username, password)

    if success:
        st.success("✅ Login berhasil.")
        st.image(result)
    else:
        st.error(f"❌ Gagal login: {result}")
