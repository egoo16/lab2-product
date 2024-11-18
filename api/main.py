from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from shared.preprocess import preprocess_data
from shared.predict import make_predictions
from shared.utils import load_model
import os
import pandas as pd

app = FastAPI()

DATASET = os.getenv("DATASET")
MODEL_PATH = "./shared/models/trained_model.pkl"  

class PredictionRequest(BaseModel):
    data: list

@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        input_data = pd.DataFrame(request.data)
        processed_data = preprocess_data(input_data)
        model = load_model(MODEL_PATH)
        predictions = make_predictions(model, processed_data)
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
