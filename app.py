import streamlit as st
from streamlit_option_menu import option_menu

def main():
    with st.sidebar:
        selected = option_menu(
            menu_title="Menu Principal",
            options=["Classificador", "Tipos de Sinais", "Significados", "Contato", "Sobre"],
            icons=["camera", "diagram-3", "book", "envelope", "info-circle"],
            menu_icon="cast",
            default_index=0
        )

    if selected == "Classificador":
        from pages import classificador
        classificador.render()
    elif selected == "Tipos de Sinais":
        from pages import tipos
        tipos.render()
    elif selected == "Significados":
        from pages import significados
        significados.render()
    elif selected == "Contato":
        from pages import contato
        contato.render()
    elif selected == "Sobre":
        from pages import sobre
        sobre.render()

if __name__ == "__main__":
    main()
