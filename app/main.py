from app.db.session import Base
from fastapi import FastAPI
from app.api.routes import auth
from app.db.session import engine
from fastapi.middleware.cors import CORSMiddleware
from app.db.models import user
from app.api.routes import workflows


app = FastAPI()
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(workflows.router)

origins = [
    "http://localhost:5173",  # or your frontend domain
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)