import streamlit as st
import requests

# URL de l'API FastAPI
API_URL = "http://127.0.0.1:8000/predict/"

st.title('Prediction de tags automatique')

st.write("Cette application utilise l'intelligence artificielle pour suggérer des tags en fonction de la question que vous entrez.")

# Fonction pour appeler l'API FastAPI
def get_prediction(title, body):
    try:
        response = requests.post(API_URL, json={"text": title + ' ' + body})
        response.raise_for_status()  # Lève une exception pour les réponses d'erreur HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de l'appel à l'API : {e}")
        return {"prediction": "Erreur lors de l'appel à l'API"}

# Zone de texte pour le titre
title = st.text_area("Title", "")

# Zone de texte pour l'entrée utilisateur
body = st.text_area("Body of texte", "")

if st.button("Générer les tags"):
    if title and body:
        prediction = get_prediction(title, body)
        st.write("Tags suggérés :")
        st.write(prediction.get("prediction", "Aucun tag suggéré."))
    else:
        st.warning("Veuillez entrer un titre et un corps du texte.")

st.sidebar.title("Options")
option = st.sidebar.selectbox("Choisissez un modèle :", ("Modèle Basique", "Modèle Avancé"))
