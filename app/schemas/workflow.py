from pydantic import BaseModel
from datetime import datetime

class WorkflowCreate(BaseModel):
    title: str
    description: str | None = None

class WorkflowOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    last_edited: datetime

    class Config:
        orm_mode = True
