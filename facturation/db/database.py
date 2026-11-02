# db/database.py
import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# Remonte de db/ vers la racine du projet, où se trouve facturation.db
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_URL = f"sqlite+aiosqlite:///{os.path.join(BASE_DIR, 'facturation.db')}"

# Engine async
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
    connect_args={"check_same_thread": False},  # spécifique à SQLite
)

# Session maker (SQLAlchemy 2.x)
async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


# Dépendance FastAPI
async def get_session():
    async with async_session() as session:
        yield session
