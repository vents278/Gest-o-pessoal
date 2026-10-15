from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from ....core.database import get_db
from ..deps import get_current_active_user

router = APIRouter(prefix="/imports", tags=["imports"])

@router.post("/preview")
async def preview(file: UploadFile = File(...), db: Session = Depends(get_db), current = Depends(get_current_active_user)):
    return {"arquivo": file.filename, "total_itens": 0, "itens": []}
