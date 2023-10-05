# How to lauch uvicorn programmatically (although using CLI is overally better)
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hi Sam"}


if __name__ == "__main__":
    uvicorn.run("example-1:app", host="127.0.0.2", port=8000, reload=True)
