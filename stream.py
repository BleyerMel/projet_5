import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model


# Charger le modèle
model = load_model('tags_predicts.h5')

st.title('Prediction de tags automatique')

st.write("Cette application utilise l'intelligence artificielle pour suggérer des tags en fonction de la questions que vous entrez.")

# st.image("ia.gif", use_column_width=True)


# Exemple de fonction pour générer des tags grace à l'ia
def generate_tags(text):

    # Exemple simple de génération de tags basé sur la présence de certains mots
    tags = []
    if "machine learning" in text.lower():
        tags.append("Machine Learning")
    if "python" in text.lower():
        tags.append("Python")
    if "data" in text.lower():
        tags.append("Data Science")
    if "web" in text.lower():
        tags.append("Web Development")
    if "ai" in text.lower():
        tags.append("Artificial Intelligence")
    return tags



# Zone de texte pour l'entrée utilisateur
user_input = st.text_area("Tapez un paragraphe ou une phrase ci-dessous pour obtenir des suggestions de tags pertinents.")

# Générer des tags automatiques en fonction de l'entrée
if user_input:
    tags = generate_tags(user_input)
    st.write("Tags suggérés:")
    st.write(", ".join(tags) if tags else "Aucun tag suggéré.")


if user_input:
    tags = generate_tags(user_input)
    selected_tags = st.multiselect("Sélectionnez ou ajustez les tags proposés :", tags, tags)
    st.write("Tags sélectionnés : ", ", ".join(selected_tags) if selected_tags else "Aucun tag sélectionné.")


if user_input:
    st.write(f"**Nombre de mots :** {len(user_input.split())}")
    st.write(f"**Nombre de caractères :** {len(user_input)}")


if st.button("Générer les tags"):
    if user_input:
        tags = generate_tags(user_input)
        st.write("Tags suggérés : ", ", ".join(tags) if tags else "Aucun tag suggéré.")


st.sidebar.title("Options")
option = st.sidebar.selectbox("Choisissez un modèle :", ("Modèle Basique", "Modèle Avancé"))
