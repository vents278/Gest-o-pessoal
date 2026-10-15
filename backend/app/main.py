from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .api.v1.api import api_router
from .core.config import settings

app = FastAPI(title=settings.APP_NAME, version="0.4.0")

origins = ["http://127.0.0.1:8000", "http://localhost:8000", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base = Path(__file__).resolve().parent.parent.parent
(frontend_path := base / "frontend").mkdir(exist_ok=True)
(static_exports := base / "static" / "exports").mkdir(parents=True, exist_ok=True)
(static_backups := base / "static" / "backups").mkdir(parents=True, exist_ok=True)

if frontend_path.exists():
    app.mount("/", StaticFiles(directory=str(frontend_path), html=True), name="frontend")
app.mount("/static", StaticFiles(directory=str(base / "static")), name="static")

app.include_router(api_router, prefix="/api/v1")
