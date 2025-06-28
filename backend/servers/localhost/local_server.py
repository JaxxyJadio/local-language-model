from fastapi import FastAPI
from backend.servers.localhost.routes import llm_routes

app = FastAPI(
    title="Local LLM Server",
    version="0.1",
    description="Serves local LLM completions"
)

app.include_router(llm_routes.router, prefix="/llm")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.servers.localhost.local_server:app", host="127.0.0.1", port=8000, reload=True)
