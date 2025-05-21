from fastapi import APIRouter
from aletheia.backend.routers.protected.me import router as users_router


protected_router = APIRouter(prefix="/protected", tags=["protected"])

