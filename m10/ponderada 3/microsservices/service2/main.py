from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/service2")
async def read_root():
    return {"message": "Hello, world! from service 2"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)