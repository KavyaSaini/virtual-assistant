"""
Course      : AIP203 - Artificial Intelligence Lab
Experiment  : Build a Virtual Assistant
Module      : server.py
Description : FastAPI web server hosting the EDITH Virtual Assistant on localhost.
"""

import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response
from pydantic import BaseModel
from dotenv import load_dotenv

from assistant import VirtualAssistant
from config import BASE_DIR, ENV_PATH
import llm_engine

app = FastAPI(title="EDITH Virtual Assistant")

# Initialize assistant instance
assistant = VirtualAssistant(voice_enabled=False)

# Data models
class ChatRequest(BaseModel):
    message: str

class KeyRequest(BaseModel):
    api_key: str


@app.get("/favicon.ico")
async def favicon():
    """Avoid 404 error when browser requests favicon."""
    return Response(status_code=204)


@app.get("/api/status")
async def get_status():
    """Return backend status."""
    try:
        load_dotenv(dotenv_path=ENV_PATH, override=True)
        return {
            "assistant_name": assistant.name,
            "llm_active": llm_engine.is_llm_configured(),
            "model": os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    """Processes user query and returns assistant response with error protection."""
    try:
        query = req.message.strip()
        if not query:
            return {"reply": "Please enter a valid question or command."}
        
        reply = assistant.process_command(query)
        return {
            "reply": reply,
            "llm_active": llm_engine.is_llm_configured()
        }
    except Exception as e:
        return {
            "reply": f"An error occurred while processing your request: {e}",
            "llm_active": False
        }


@app.post("/api/set_key")
async def set_key_endpoint(req: KeyRequest):
    """Saves Gemini API key to .env file."""
    try:
        key = req.api_key.strip()
        if not key:
            return JSONResponse({"status": "error", "message": "API key cannot be empty."}, status_code=400)
        
        env_content = f"# Virtual Assistant Configuration\nGEMINI_API_KEY={key}\nGEMINI_MODEL=gemini-2.5-flash\n"
        with open(ENV_PATH, "w", encoding="utf-8") as f:
            f.write(env_content)
        
        os.environ["GEMINI_API_KEY"] = key
        load_dotenv(dotenv_path=ENV_PATH, override=True)

        return {"status": "success", "message": "API key configured successfully!"}
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)


@app.get("/", response_class=HTMLResponse)
async def serve_home():
    """Serves the EDITH single-page web UI."""
    try:
        html_path = BASE_DIR / "web" / "index.html"
        if html_path.exists():
            with open(html_path, "r", encoding="utf-8") as f:
                return HTMLResponse(content=f.read())
        return HTMLResponse("<h1>EDITH is loading...</h1>")
    except Exception as e:
        return HTMLResponse(f"<h1>Error loading interface: {e}</h1>")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 EDITH Virtual Assistant Server running on http://localhost:{port}")
    uvicorn.run("server:app", host="127.0.0.1", port=port, reload=False)
