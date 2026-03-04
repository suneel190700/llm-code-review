"""
FastAPI server for LLM Code Review Assistant
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI(title="LLM Code Review API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8001)
