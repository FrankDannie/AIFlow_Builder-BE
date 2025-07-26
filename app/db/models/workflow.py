from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.session import Base

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    last_edited = Column(DateTime, default=func.now(), onupdate=func.now())
