from fastapi import APIRouter, Depends
from ....schemas.user import UserResponse
from ..deps import get_current_active_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
def read_me(current_user = Depends(get_current_active_user)):
    return current_user
