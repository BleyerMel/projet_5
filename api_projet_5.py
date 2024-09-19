# API projet_5

from fastapi import FastAPI
import joblib
import mlflow

app = FastAPI()

# Charger la pipeline à partir de MLflow
model_uri =  'file:///C:/Users/bleye/Documents/GitHub/projet_5/mlruns/f456f5602e9648d98bed7f4729ccd337/artifacts/model'
model = mlflow.sklearn.load_model(model_uri)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

@app.post("/predict/")
def predict(data: dict):
    text = data['text']
    prediction = model.predict([text])
    return {"prediction": prediction[0]}