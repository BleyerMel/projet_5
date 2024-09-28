from fastapi.testclient import TestClient
from app import app  

client = TestClient(app)

def test_alive():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"Im Alive !"'

def test_prediction():
   
    data = {
        'Title': ['help ! my function not working'],
        'Body': ['i need help with my python function']
    }

    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()
