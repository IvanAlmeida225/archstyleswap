import streamlit as st
import requests

st.set_page_config(page_title="ArchStyleSwap 🏛️🤖", layout="centered")
st.title("🏛️ ArchStyleSwap")
st.write("Transforme o estilo arquitetônico de qualquer ambiente com IA!")

uploaded_file = st.file_uploader("📤 Faça upload de uma imagem do ambiente", type=["jpg", "jpeg", "png"])
style = st.selectbox("🎨 Escolha o estilo arquitetônico desejado", ["Moderno", "Clássico", "Minimalista", "Futurista"])

if uploaded_file and st.button("Transformar"):
    files = {"image": uploaded_file.getvalue()}
    response = requests.post("http://localhost:8000/transform", files=files, data={"style": style})

    if response.status_code == 200:
        st.success("✅ Transformação concluída!")
        st.image(response.content, caption="Imagem transformada", use_column_width=True)
    else:
        st.error("❌ Erro ao processar a imagem. Tente novamente.")
