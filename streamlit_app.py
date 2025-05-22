import streamlit as st

st.title("🎈 Varick Ganteng 🤩")
st.write(
    "aku gatau kenapa aku ganteng banget 😍"
)
st.image("view/1dce5b82-e46c-4d42-9461-95dac9e542be.jpeg")

st.header ("aplikasi mengecek nilai ganjil/genap")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)
if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
    st.write(f"{angka} adalah bilangan ganjil")
