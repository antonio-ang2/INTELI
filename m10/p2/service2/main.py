from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/service2")
async def read_root():
    return {"message": "Murilo, isso é um pedido de socorro, se você não quiser ver minha cara mais um módulo aqui, me dá um 10, por favor? Te amo!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)