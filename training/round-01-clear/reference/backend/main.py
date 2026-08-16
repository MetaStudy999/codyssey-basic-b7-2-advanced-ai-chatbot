from fastapi import FastAPI
from fastapi.responses import FileResponse

from backend import models  # noqa: F401 - register ORM metadata
from backend.database import Base, engine
from backend.routers import auth, chat, posts

app = FastAPI(title="B7-2 Advanced AI Chatbot Reference")
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(posts.router)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse("frontend/index.html")


@app.get("/app.js", include_in_schema=False)
def frontend_script():
    return FileResponse("frontend/app.js", media_type="application/javascript")
