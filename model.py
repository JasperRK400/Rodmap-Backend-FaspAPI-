from pydantic import BaseModel

class RoadmapRequest(BaseModel):
    goal: str
    current_level: str
    timeline_months: int

