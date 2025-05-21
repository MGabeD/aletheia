from fastapi import APIRouter, Depends
from aletheia.backend.core.auth import current_active_user
from aletheia.backend.routers.protected.me import router as me_router

router = APIRouter(
    prefix="/protected", 
    dependencies=[Depends(current_active_user)], 
    tags=["protected"]
)

router.include_router(me_router)