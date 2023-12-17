# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("minha_api")

# Create input/output pydantic models
class InputData(BaseModel):
    Gender: str
    Age: int
    Income: int

class OutputData(BaseModel):
    prediction: float

# Define predict function
@app.post("/predict", response_model=OutputData)
def predict(data: InputData):
    data_dict = data.dict()
    data_df = pd.DataFrame([data_dict])
    predictions = predict_model(model, data=data_df)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
