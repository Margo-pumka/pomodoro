import sqlite3

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from settings import Settings

settings = Settings()

engine = create_async_engine(settings.db_url(), future=True, echo=True, pool_pre_ping=True)

AsyncSessionFactory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


async def get_db_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session


#
#
# def get_db_connection() -> sqlite3.Connection:
#     return sqlite3.connect(settings.SQLITE_DB_NAME)
