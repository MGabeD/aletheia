import asyncio
import asyncpg
from aletheia.utils import get_postgres_asyncpg_url
from aletheia.utils.logger import get_logger

logger = get_logger(__name__)

async def test_connection():
    url = get_postgres_asyncpg_url()
    logger.info(f"Testing connection to {url}")
    try:
        conn = await asyncpg.connect(url)
        logger.info("Connection successful!")
        await conn.close()
    except Exception as e:
        logger.error(f"Connection failed: {e}")

asyncio.run(test_connection())