from fastapi import FastAPI

app = FastAPI()

# Root
@app.get('/')
async def read_root():
    return { "Hello" : "World" }
