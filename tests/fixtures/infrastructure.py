import pytest
import pytest_asyncio
from sqlalchemy import NullPool

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.settings import Settings
from app.infrastructure.database.database import Base


@pytest.fixture
def settings():
    return Settings()


engine = create_async_engine(url="postgresql+asyncpg://postgres:password@0.0.0.0:5432/pomodoro", future=True, echo=True, pool_pre_ping=False, poolclass=NullPool)


AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)

# conftest.py — ОСТАВИ ТОЛЬКО ЭТО
@pytest_asyncio.fixture(scope="function")
async def db_session():
    # 1. Создаём таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # 2. Даём чистую сессию
    async with AsyncSessionFactory() as session:
        yield session

    # 3. Удаляем таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
