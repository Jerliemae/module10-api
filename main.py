from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Module 10 Part A API", version="1.0")

@app.get("/")
def read_root():
    return JSONResponse(content={
        "message": "Hello from Module 10 Part A API!",
        "status": "success",
        "deployed": True
    })

@app.get("/hello/{name}")
def say_hello(name: str):
    return JSONResponse(content={
        "greeting": f"Hello, {name}!",
        "note": "This is your deployed FastAPI on Vercel"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)