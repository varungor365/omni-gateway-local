import json
import os

import litellm
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse

app = FastAPI(
    title="Omni Gateway Local",
    description="Unified API gateway for all LLMs",
    version="1.0.0"
)

# Optional: set default model if none provided
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o-mini")

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    try:
        body = await request.json()
    except Exception:  # noqa: BLE001
        raise HTTPException(status_code=400, detail="Invalid JSON body")
        
    messages = body.get("messages", [])
    model = body.get("model", DEFAULT_MODEL)
    stream = body.get("stream", False)
    
    # Configure LiteLLM
    # E.g., if model is "ollama/llama3", litellm handles it automatically
    
    try:
        response = litellm.completion(
            model=model,
            messages=messages,
            stream=stream,
            **{k: v for k, v in body.items() if k not in ["messages", "model", "stream"]}
        )
        
        if stream:
            async def generate():
                for chunk in response:
                    yield f"data: {json.dumps(chunk.model_dump())}\n\n"
                yield "data: [DONE]\n\n"
            return StreamingResponse(generate(), media_type="text/event-stream")
        else:
            return response.model_dump()
            
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok"}
