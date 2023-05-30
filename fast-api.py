from fastapi.responses import StreamingResponse
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import base64
import aiofiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Model(BaseModel):
    name: str


class Message(BaseModel):
    sender: str
    text: str
    model: Optional[str] = None
    end: Optional[bool] = None


class Conversation(BaseModel):
    messages: List[Message]


models = [
    Model(name="GPT-1"),
    Model(name="GPT-2"),
    Model(name="GPT-3"),
]


def convert_to_base64_chunk(s: str) -> str:
    return base64.b64encode(s.encode()).decode() + "\n"


@app.get("/api/models")
async def get_models():
    print("got models request")
    return {"models": models}


@app.post("/api/summaries")
async def get_summary(message: List[Message]):
    print("got summary request")
    if not message or not message[0].text:
        print("no messages")
        raise HTTPException(status_code=400, detail="Message is required")
    return {"summary": message[0].text[:20]}


@app.post("/api/models/{model}/conversations")
async def create_conversation(model: str, conversation: Conversation):
    print("got conversations request")
    if not conversation.messages or not conversation.messages[0]:
        raise HTTPException(status_code=400, detail="Message is required")

    file = f"./stories/story{len(conversation.messages[-1].text) % 4}.md"
    async with aiofiles.open(file, mode='r') as f:
        story = await f.read()
    words = story.split(" ")

    async def generate():
        while words:
            await asyncio.sleep(0.1)  # Simulate delay
            yield base64.b64encode(words.pop(0).encode()).decode() + "\n"

    return StreamingResponse(generate(), media_type="text/plain")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)
