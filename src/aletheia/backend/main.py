import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

import aletheia.backend.models as models
from aletheia.backend.core.db import create_db_and_tables
from aletheia.backend.routers.auth import router as auth_router
from aletheia.backend.routers.protected import router as protected_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(protected_router)


if __name__ == "__main__":
    uvicorn.run("aletheia.backend.main:app", host="0.0.0.0", log_level="info")