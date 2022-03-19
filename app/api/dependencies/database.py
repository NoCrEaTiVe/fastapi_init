from typing import Type
from app.db.database import async_session
from app.db.repositories.base import BaseRepository


def get_repository(
    repo_type: Type[BaseRepository],
):
    async def _get_repo() -> BaseRepository:
        async with async_session() as session:
            async with session.begin():
                yield repo_type(session)
    return _get_repo
