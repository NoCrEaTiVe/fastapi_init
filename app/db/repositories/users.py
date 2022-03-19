from .base import BaseRepository
from app.services.redis import redis_manager
from app.services.auth.authentication import PasswordManager
from app.models.domain.users import User

from sqlalchemy.sql.expression import exists
from sqlalchemy import update, desc, delete
from sqlalchemy.future import select


class UserRepository(BaseRepository):
    async def create_user(self, password, email):
        password_manager = PasswordManager(password)
        user_data = await redis_manager.lrange("user:"+email)
        new_user = User(
            first_name=user_data[0],
            last_name=user_data[1],
            hashed_password=password_manager.get_password_hash(),
            email=email
        )
        self.connection.add(new_user)
        await self.connection.flush()
        return new_user

    async def check_user(self, email):
        query_is_user_exists = await self.connection.execute(
            exists(select(User.id).filter_by(email=email)).select()
        )
        return query_is_user_exists.scalar()

    async def get_user(self, email):
        user = await self.connection.execute(
            select(User).filter(
                User.email == email,
            )
        )
        return user.scalars().first()
