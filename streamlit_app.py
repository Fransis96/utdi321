import streamlit as st
import joblib

# Load semua model dan vectorizer
model_lr = joblib.load('./model/lr_model_v1.joblib')
vectorizer_lr = joblib.load('./model/tfidf_v1.joblib')

model_svc = joblib.load('./model/svc_model_v2.joblib')
svc_vectorizer = joblib.load('./model/tfidf_scv_v2.joblib')

# Judul halaman
st.title("🕵️ Klasifikasi Sentimen Teks")

# Pilihan model
model_choice = st.selectbox("Pilih model yang akan digunakan:", ["Logistic Regression", "SVC"])

# Input dari user
teks_input = st.text_area("Masukkan teks untuk dianalisis:")

# Tombol prediksi
if st.button("Prediksi Sentimen"):
    if not teks_input.strip():
        st.warning("Teks tra boleh kosong!!!")
    else:
        teks_bersih = teks_input.lower()

        # Tentukan model & vectorizer
        if model_choice == "Logistic Regression":
            X = vectorizer_lr.transform([teks_bersih])
            prediksi = model_lr.predict(X)[0]
        else:
            X = svc_vectorizer.transform([teks_bersih])
            prediksi = model_svc.predict(X)[0]

        # Tampilkan hasil
        st.success(f"Hasil Prediksi: **{prediksi.upper()}**")
