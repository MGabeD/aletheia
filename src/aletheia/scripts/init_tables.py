# aletheia/scripts/init_db.py
import asyncio
from aletheia.backend import models   # auto‑imports every model -> registers tables
from aletheia.backend.core.db import engine, Base
from aletheia.utils.logger import get_logger

logger = get_logger(__name__)

async def main() -> None:
    logger.info("Initializing tables...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Tables initialized successfully")

if __name__ == "__main__":
    asyncio.run(main())
