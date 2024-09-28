from fastapi import FastAPI
import pandas as pd
import json
import uvicorn
import mlflow
from pydantic import BaseModel 
from typing import List  

app = FastAPI()

mlflow.set_tracking_uri("http://localhost:5000")
logged_model = 'runs:/6c686c44df6543fca8617db1579e135b/model'
loaded_pipeline = mlflow.pyfunc.load_model(logged_model)

with open('labels.txt', 'r') as f:
    classes = [line.strip() for line in f]

# test de pydantic
class PredictionRequest(BaseModel):
    Title: List[str]
    Body: List[str]

# Inverser la transformation manuellement
def inverse_transform(encoded_labels, classes):
    return [classes[i] for i in encoded_labels]

@app.get('/')
def Alive():
    return 'Im Alive !'

@app.post('/predict')  
def Prediction(data: PredictionRequest): 
    
    df = pd.DataFrame({
        'Title': data.Title,
        'Body': data.Body
    })
    
    # Faire une prédiction avec la pipeline
    X_transformed = loaded_pipeline.predict(df)

    original_labels = inverse_transform(X_transformed, classes)

    return {"prediction": original_labels}
