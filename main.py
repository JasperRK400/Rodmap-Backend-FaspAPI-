from fastapi import FastAPI
from app.models import RoadmapRequest
from app.prompts import roadmap_prompt
from app.ai_client import get_ai_roadmap

app = FastAPI()

@app.post("/generate-roadmap")
def generate(data: RoadmapRequest):
    prompt = roadmap_prompt(
        data.goal,
        data.current_level,
        data.timeline_months
    )
    return get_ai_roadmap(prompt)

