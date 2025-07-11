import streamlit as st
import subprocess
import base64

# --- Configuration de la page
st.set_page_config(page_title="Détection / Segmentation", layout="centered")

# --- Fonction pour insérer une image de fond animée
def add_background(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()

    css = f"""
    <style>
    /* --- Arrière-plan animé --- */
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: 70% auto;
        background-repeat: repeat-x;
        background-position: 0 0;
        animation: slideBg 40s linear infinite;
    }}

    @keyframes slideBg {{
        0% {{ background-position: 0% 0; }}
        100% {{ background-position: -100% 0; }}
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        z-index: -1;
    }}

    /* --- Titre stylisé --- */
    .stTitle h1 {{
        color: #ffffff;
        font-size: 3em;
        text-shadow: 2px 2px 4px #000;
        text-align: center;
    }}

    /* --- Texte --- */
    .stMarkdown p {{
        color: #00E5FF;
        font-size: 1.2em;
        text-align: center;
    }}

    /* --- Radio boutons --- */
    .stRadio label {{
        color: #ffffff !important;
        font-size: 1.1em;
    }}

    /* --- Bouton stylisé --- */
    div.stButton > button {{
        background-color: #4CAF50;
        color: white;
        padding: 0.75em 2em;
        font-size: 1.1em;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        margin: auto;
        display: block;
    }}

    div.stButton > button:hover {{
        background-color: #45a049;
        transform: scale(1.05);
        cursor: pointer;
    }}

    /* Centrage global */
    .stRadio, .stMarkdown, .stButton {{
        text-align: center;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- Appliquer le fond
add_background(r"C:\Users\ALSAKB\Desktop\BIBDA S3\IA2\Projet IA\Brain Tumor Detection aaroud\images2.jpg")

# --- Interface principale
st.title("Bienvenue 👋")
st.write("Que souhaitez-vous faire ?")

choice = st.radio(
    "Sélectionnez une option :",
    ("Faire la détection d'une tumeur", "Faire la segmentation"),
    index=0
)

if st.button("Continuer"):
    if choice == "Faire la détection d'une tumeur":
        app_path = r"C:\Users\ALSAKB\Desktop\BIBDA S3\IA2\Projet IA\Brain Tumor Detection aaroud\detection\app.py"
        subprocess.Popen([
            r"C:\Users\ALSAKB\Desktop\BIBDA S3\IA2\Projet IA\Brain Tumor Detection aaroud\venv\Scripts\python.exe",
            "-m", "streamlit", "run", app_path
        ])
        st.success("Application de détection en cours de lancement...")
        st.markdown("[Accéder à l'application](http://localhost:8502)")

    elif choice == "Faire la segmentation":
        streamlit_app_path = r"C:\Users\ALSAKB\Desktop\BIBDA S3\IA2\Projet IA\Brain Tumor Detection aaroud\Segmentation\app_segmentation.py"
        subprocess.Popen([
            r"C:\Users\ALSAKB\Desktop\BIBDA S3\IA2\Projet IA\Brain Tumor Detection aaroud\venv\Scripts\python.exe",
            "-m", "streamlit", "run", streamlit_app_path
        ])
        st.success("Application de segmentation en cours de lancement...")
        st.markdown("[Accéder à l'application](http://localhost:8503)")
