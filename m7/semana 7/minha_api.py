import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

# Crie o app FastAPI
app = FastAPI()

# Carregue o modelo treinado
model = load_model("minha_api")

# Define uma classe Pydantic para entrada/saída de dados
class InputData(BaseModel):
    file: UploadFile

class OutputData(BaseModel):
    predictions: list


@app.post("/predict_csv", response_model=OutputData)
async def predict_csv(data: UploadFile):
    try:
        # Lê o arquivo CSV enviado
        # content = data.file.read()
        # df = pd.read_csv(content)
        df = pd.read_csv(data.filename)
        df.rename(columns={'Annual Income (k$)': 'Income'}, inplace=True)
        df.rename(columns={'Spending Score (1-100)': 'Score'}, inplace=True)
        
        # Faz as previsões
        predictions = predict_model(model, data=df)
        
        # Retorna as previsões em um formato JSON
        response_data = {"predictions": predictions["prediction_label"].tolist()}
        
        # Registra a resposta para depuração
        logging.info(response_data)
        
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
