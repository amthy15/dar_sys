import fastapi as fa

app = FastAPI()

# Root
@app.get('/')
async def read_root():
    return { "Hello" : "World" }
