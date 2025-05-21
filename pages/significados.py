def render():
    import streamlit as st
    from constants import NOMES_DE_SINAIS
    st.title("📖 Significados dos Sinais")
    for k, v in NOMES_DE_SINAIS.items():
        st.write(f"{k}. {v}")
