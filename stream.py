import streamlit as st
import requests
import json


# URL de l'API FastAPI
API_URL = "http://127.0.0.1:8000/predict"

st.title('Prédiction automatique de tags')

st.write("Cette application utilise l'intelligence artificielle pour suggérer des tags en fonction du titre et du corps de texte que vous entrez.")

# Fonction pour appeler l'API FastAPI
def get_prediction(title, body):
    # Créer le format de données attendu par l'API
    data = json.dumps([{"Title": title, "Body": body}])
    
    try:
        # Appel de l'API FastAPI en GET avec les données formatées
        response = requests.get(API_URL, params={"data": data})
        response.raise_for_status()  # Gérer les erreurs HTTP
        return response.json()  # Extraire la réponse JSON
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de l'appel à l'API : {e}")
        return {"prediction": "Erreur lors de l'appel à l'API"}

# Zone de texte pour le titre
title = st.text_area("Titre", "")

# Zone de texte pour l'imput utilisateur (Body)
body = st.text_area("Corps du texte", "")

if st.button("Générer les tags"):
    if title and body:
        # Appel de l'API pour obtenir les prédictions
        prediction = get_prediction(title, body)
        # Vérifier si des tags ont été retournés
        if prediction["prediction"]:
            st.write("### Tags suggérés :")
            # Afficher les tags sous forme de liste
            for tag in prediction["prediction"]:
                st.markdown(f"- {tag}")
        else:
            st.write("Aucun tag suggéré.")
    else:
        st.warning("Veuillez entrer un titre et un corps du texte.")

st.sidebar.title("Options")
option = st.sidebar.selectbox("Choisissez un modèle :", ("Modèle Basique", "Modèle Avancé"))
