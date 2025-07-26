from sqlalchemy.orm import Session
from app.schemas.workflow import WorkflowCreate
from app.db.models.workflow import Workflow

def create_workflow(db: Session, data: WorkflowCreate) -> Workflow:
    workflow = Workflow(**data.dict())
    db.add(workflow)
    db.commit()
    db.refresh(workflow)
    return workflow

def get_all_workflows(db: Session) -> list[Workflow]:
    return db.query(Workflow).order_by(Workflow.last_edited.desc()).all()
