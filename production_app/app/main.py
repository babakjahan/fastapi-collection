from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI(
    title="FastAPI Production App",
    description="A FastAPI application designed for production use",
    version="1.0.0")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """<!DOCTYPE html><html><head><title>Production FastAPI App</title></head>
    <body><h1>Welcome to the Production FastAPI App!</h1><p>This app is designed for production use.</p>
    </body></html>"""
    

@app.get("/status")
def read_status():
    return JSONResponse(content={"status": "Production app is ready"})