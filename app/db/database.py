
import logging
from typing import AsyncIterator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from app.core.config import get_app_settings


settings = get_app_settings()
logger = logging.getLogger(__name__)


engine = create_async_engine(
    settings.database_url,
    pool_size=0,
    echo=False
)

async_session = sessionmaker(
    bind=engine, autoflush=False, future=True, class_=AsyncSession
)

Base = declarative_base()


async def get_db() -> AsyncIterator[sessionmaker]:
    try:
        yield async_session
    except SQLAlchemyError as e:
        logger.exception(e)
