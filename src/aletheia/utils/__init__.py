import os

def get_postgres_connection_base() -> str:
    user = os.getenv("DATABASE_USER")
    password = os.getenv("DATABASE_PASSWORD")
    host = os.getenv("DATABASE_HOST")  
    return f"://{user}:{password}@{host}"

def get_postgres_asyncpg_url() -> str:
    """
    Generates a PostgreSQL connection URL from environment variables.
    """
    return f"postgresql{get_postgres_connection_base()}"

def get_postgres_url() -> str:
    """
    Generates a PostgreSQL connection URL from environment variables.

    Expects the following environment variables:
    - DB_USER: PostgreSQL username
    - DB_PASSWORD: PostgreSQL password
    - DB_HOST: Hostname and database name (e.g., "localhost/aletheia")

    Returns:
        str: The full asyncpg-compatible PostgreSQL URL.
    """
    return f"postgresql+asyncpg{get_postgres_connection_base()}"