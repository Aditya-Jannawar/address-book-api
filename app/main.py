from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.api.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running 🚀"}