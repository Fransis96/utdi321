import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load semua model dan vectorizer
model_lr = joblib.load('./model/lr_model_v1.joblib')
vectorizer_lr = joblib.load('./model/tfidf_v1.joblib')

model_svc = joblib.load('./model/svc_model_v3.joblib')
svc_vectorizer = joblib.load('./model/tfidf_svc_v3.joblib')

model_dnn = load_model('./model/model_dnn.h5')
tokenizer_dnn = joblib.load('./model/tokenizer_dnn.joblib')
maxlen = 100  # ganti dengan panjang maksimum saat kamu latih model

# Judul halaman
st.title("🕵️ Klasifikasi Sentimen Teks")

# Pilihan model
model_choice = st.selectbox("Pilih model yang akan digunakan:", ["Logistic Regression", "SVC", "DNN"])

# Input dari user
teks_input = st.text_area("Masukkan teks untuk dianalisis:")

# Tombol prediksi
if st.button("Prediksi Sentimen"):
    if not teks_input.strip():
        st.warning("Teks tidak boleh kosong 😏")
    else:
        teks_bersih = teks_input.lower().strip()

        if model_choice == "Logistic Regression":
            X = vectorizer_lr.transform([teks_bersih])
            prediksi = model_lr.predict(X)[0]

        elif model_choice == "SVC":
            X = svc_vectorizer.transform([teks_bersih])
            prediksi = model_svc.predict(X)[0]

        elif model_choice == "DNN":
            seq = tokenizer_dnn.texts_to_sequences([teks_bersih])
            padded = pad_sequences(seq, maxlen=maxlen)
            pred = model_dnn.predict(padded)
            prediksi = "non-negative" if pred[0][0] > 0.5 else "negative"

        # Tampilkan hasil
        st.success(f"Hasil Prediksi: **{prediksi.upper()}**")
