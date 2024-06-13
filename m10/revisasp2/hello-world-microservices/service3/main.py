from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/service3")
async def read_root():
    return {"message": "Hello, world! from service 3"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)