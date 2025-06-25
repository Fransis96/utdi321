import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model_dnn = load_model('./model/dnn_model_v1.keras')

tokenizer_dnn = joblib.load('./model/tokenizer_dnn_v1.joblib')
label_encoder_dnn = joblib.load('./model/label_encoder_v1.joblib')

maxlen = 100  # Panjang input teks

# ======== UI STREAMLIT ========
st.title("🧠 Prediksi Sentimen (Model DNN)")

teks_input = st.text_area("Masukkan teks untuk dianalisis:")

if st.button("Prediksi"):
    if not teks_input.strip():
        st.warning("Teks tidak boleh kosong 😅")
    else:
        teks_bersih = teks_input.lower().strip()
        seq = tokenizer_dnn.texts_to_sequences([teks_bersih])
        padded = pad_sequences(seq, maxlen=maxlen)
        prob = model_dnn.predict(padded, verbose=0)[0][0]
        label = 1 if prob > 0.5 else 0
        prediksi = label_encoder_dnn.inverse_transform([label])[0]
        st.success(f"Hasil Prediksi: **{prediksi.upper()}**")
