from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Optional: Define another endpoint
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}