def render():
    import streamlit as st
    from PIL import Image
    from classify import predict
    from constants import NOMES_DE_SINAIS
    from utils import convert_to_rgb, image_to_byte_stream

    st.title("🚦 Classificador de Sinais de Trânsito")
    st.image("assets/ilustracao.jpg", caption='Classificação de Sinais', use_container_width=True)

    option = st.selectbox("Método de entrada:", ["Upload de Imagem", "Captura com Câmera"])
    image = None

    if option == "Upload de Imagem":
        uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            image = Image.open(uploaded_file)
    else:
        camera_image = st.camera_input("Capture uma imagem")
        if camera_image:
            image = Image.open(camera_image)

    if image:
        st.image(image, caption="Imagem Selecionada", use_container_width=True)
        if st.button("Classificar"):
            with st.spinner("Classificando..."):
                rgb_image = convert_to_rgb(image)
                img_bytes = image_to_byte_stream(rgb_image)
                label = predict(img_bytes)
                nome = NOMES_DE_SINAIS.get(label, "Sinal desconhecido")
                st.success(f"Sinal detectado: {nome}")
