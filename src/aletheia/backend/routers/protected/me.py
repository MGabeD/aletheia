from fastapi import Depends, APIRouter
from aletheia.backend.core.auth import current_active_user
from aletheia.backend.models.users import User


router = APIRouter(tags=["users"])

@router.get("/me")
async def get_me(user: User = Depends(current_active_user)):
    return {"self": user}

