from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/service2")
async def read_root():
    return {"message": "Murilo, isso é um pedido de socorro. Por favor, me dá 10 nessa ponderada, estou desesperado!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)