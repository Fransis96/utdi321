import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ======== LOAD MODEL & OBJEK ========
# Load model sklearn
model_lr = joblib.load('./model/lr_model_v1.joblib')
vectorizer_lr = joblib.load('./model/tfidf_v1.joblib')

model_svc = joblib.load('./model/svc_model_v3.joblib')
svc_vectorizer = joblib.load('./model/tfidf_svc_v3.joblib')

# Load model DNN (.keras safer than .h5)
try:
    model_dnn = load_model('./model/dnn_model_v1.keras')
except Exception as e:
    st.error("❌ Gagal memuat model DNN. Pastikan file `.keras` valid.")
    st.stop()

# Load tokenizer & label encoder
tokenizer_dnn = joblib.load('./model/tokenizer_dnn_v1.joblib')
label_encoder_dnn = joblib.load('./model/label_encoder_v1.joblib')  # pastikan ini hasil dari LabelEncoder()

maxlen = 100  # Panjang input DNN

# ======== UI STREAMLIT ========
st.title("🕵️ Klasifikasi Sentimen Teks")

model_choice = st.selectbox("Pilih model yang akan digunakan:", ["Logistic Regression", "SVC", "DNN"])
teks_input = st.text_area("Masukkan teks untuk dianalisis:")

if st.button("Prediksi Sentimen"):
    if not teks_input.strip():
        st.warning("Teks tidak boleh kosong 😏")
    else:
        teks_bersih = teks_input.lower().strip()

        # ========== LOGISTIC REGRESSION ==========
        if model_choice == "Logistic Regression":
            X = vectorizer_lr.transform([teks_bersih])
            prediksi = model_lr.predict(X)[0]

        # ========== SVC ==========
        elif model_choice == "SVC":
            X = svc_vectorizer.transform([teks_bersih])
            prediksi = model_svc.predict(X)[0]

        # ========== DNN ==========
        elif model_choice == "DNN":
            seq = tokenizer_dnn.texts_to_sequences([teks_bersih])
            padded = pad_sequences(seq, maxlen=maxlen)
            prob = model_dnn.predict(padded, verbose=0)[0][0]
            label = 1 if prob > 0.5 else 0
            prediksi = label_encoder_dnn.inverse_transform([label])[0]

        # Tampilkan hasil
        st.success(f"Hasil Prediksi: **{prediksi.upper()}**")
