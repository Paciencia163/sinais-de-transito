# 🚦 Classificação de Sinais de Trânsito com Deep Learning

Aplicação web desenvolvida com [Streamlit](https://streamlit.io) para detectar e classificar sinais de trânsito com base em imagens, utilizando redes neurais convolucionais (CNN).

🎯 O objetivo é facilitar o reconhecimento de sinais rodoviários a partir de fotos ou da câmera, com explicações acessíveis sobre cada sinal.

---

## 🖼 Funcionalidades

- Upload ou captura de imagem com a câmera
- Classificação automática com modelo treinado
- Interface intuitiva e organizada por páginas
- Informações sobre os tipos e significados dos sinais
- Página de contato e descrição do projeto

---

## 🧠 Modelo

O modelo treinado está localizado em:

```
app/model/Traffic_Sign_Classifier_CNN.hdf5
```

Formato de entrada: imagens 32x32 em escala de cinza.

---

## 📁 Estrutura do Projeto

```
app/
├── app.py                 # Arquivo principal com menu lateral
├── constants.py           # Dicionário de sinais
├── classify.py            # Predição com TensorFlow
├── utils.py               # Manipulação de imagem
├── assets/                # Imagens e ilustrações
│   └── ilustracao.jpg
├── model/                 # Modelo treinado (.hdf5)
│   └── Traffic_Sign_Classifier_CNN.hdf5
└── pages/                 # Páginas da aplicação
    ├── __init__.py
    ├── classificador.py
    ├── tipos.py
    ├── significados.py
    ├── contato.py
    └── sobre.py

requirements.txt           # Dependências da aplicação
README.md
```

---

## 🚀 Executar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app/app.py
```

---

## ☁️ Deploy no Streamlit Cloud

1. Crie uma conta em https://streamlit.io/cloud
2. Conecte ao seu repositório GitHub
3. Escolha o arquivo de entrada: `app/app.py`
4. Pronto! Sua aplicação estará acessível por uma URL pública

---

## 📬 Contato

- GitHub: [seu-usuario](https://github.com/Paciencia163)
- Email: paciencia@gmail.com

---

Desenvolvido com ❤️ usando Python e Streamlit.

© 2025 - Licença MIT
