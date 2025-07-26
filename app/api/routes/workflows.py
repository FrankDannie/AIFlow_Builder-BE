from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.workflow import WorkflowCreate, WorkflowOut
from app.db.session import get_db
from app.db.crud import workflow as crud

router = APIRouter(prefix="/api/v1", tags=["Workflows"])

@router.post("/workflows", response_model=WorkflowOut)
def create_workflow(data: WorkflowCreate, db: Session = Depends(get_db)):
    return crud.create_workflow(db, data)

@router.get("/workflows", response_model=list[WorkflowOut])
def get_workflows(db: Session = Depends(get_db)):
    return crud.get_all_workflows(db)
