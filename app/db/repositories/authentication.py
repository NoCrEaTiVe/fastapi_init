from app.services.redis import redis_manager
from app.models.schemas.auth import UserCreate
from app.services.auth.jwt import create_jwt_token, decode_jwt_token
from datetime import timedelta


class AuthRepository:
    async def register(self, user_schema: UserCreate):
        key_name = "user:"+user_schema.email
        data = [user_schema.first_name, user_schema.last_name]
        await redis_manager.lpush(key_name, data)
        await redis_manager.expire_key(key_name, 60*60)
        access_token_expires = timedelta(minutes=60*60)
        return create_jwt_token(jwt_content={'email': user_schema.email}, secret_key="REGISTER_VERIFY", expires_delta=access_token_expires)

    async def register_verify(self, email, code: str):
        key_name = "user:" + email
        await redis_manager.expire_key(key_name, 60 * 60)
        access_token_expires = timedelta(minutes=60 * 60)
        return create_jwt_token(jwt_content={'email': email}, secret_key="PASSWORD_VALIDATION", expires_delta=access_token_expires)

    async def decode_register_verify(self, token):
        payload = decode_jwt_token(token, secret_key="REGISTER_VERIFY")
        return payload.get('email', None)

    async def decode_register_finish(self, token):
        payload = decode_jwt_token(token, secret_key="PASSWORD_VALIDATION")
        return payload.get('email', None)

    async def check_user_exists(self, email):
        key_name = "user:"+email
        is_exists = await redis_manager.is_exists(key_name)
        return is_exists

    async def access_token(self, user_id):
        access_token_expires = timedelta(minutes=60 * 60 * 60)
        return create_jwt_token(jwt_content={'id': user_id}, secret_key="ACCESS_TOKEN",
                                expires_delta=access_token_expires)
