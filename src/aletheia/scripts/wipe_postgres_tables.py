import asyncio
import asyncpg
from aletheia.utils import get_postgres_asyncpg_url
from aletheia.utils.logger import get_logger

logger = get_logger(__name__)

async def wipe_all_tables():
    url = get_postgres_asyncpg_url()
    logger.info(f"Connecting to {url}")
    
    try:
        conn = await asyncpg.connect(url)
        logger.info("Connected to database")

        rows = await conn.fetch("""
            SELECT tablename
            FROM pg_tables
            WHERE schemaname = 'public';
        """)

        table_names = [row["tablename"] for row in rows]

        if not table_names:
            logger.info("No tables found to drop.")
        else:
            for table in table_names:
                logger.info(f"Dropping table: {table}")
                await conn.execute(f'DROP TABLE IF EXISTS "{table}" CASCADE;')

            logger.info("All tables dropped.")

        await conn.close()
    except Exception as e:
        logger.error(f"Failed to wipe tables: {e}")

if __name__ == "__main__":
    asyncio.run(wipe_all_tables())
