from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from pathlib import Path
from ..deps import get_current_active_user

router = APIRouter(prefix="/backup", tags=["backup"])

@router.get("/download")
def download(current = Depends(get_current_active_user)):
    base = Path(__file__).resolve().parent.parent.parent.parent.parent
    db_path = base / "rita_jean.db"
    if not db_path.exists():
        from fastapi import HTTPException
        raise HTTPException(404, "Banco não encontrado")
    return FileResponse(path=db_path, filename="rita_jean.db")
