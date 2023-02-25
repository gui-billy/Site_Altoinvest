from fastapi import FastAPI

app = FastAPI()


@app.get("/mt5/")
async def root():
    return {"message": "Hello World"}



