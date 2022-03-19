from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.api.dependencies.database import get_repository
from app.db.repositories.users import UserRepository
from app.db.repositories.authentication import AuthRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)


def register_verify():
    async def get_current_user(
            token: str = Depends(oauth2_scheme),
            user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):
        if token is None:
            raise BaseException #change
        auth_repo = AuthRepository()
        user_email = await auth_repo.decode_register_verify(token)
        if user_email is None:
            raise BaseException #change
        is_already_exists = await user_repo.check_user(user_email)
        if is_already_exists:
            raise BaseException #change
        exists = await auth_repo.check_user_exists(user_email)
        if not exists:
            raise BaseException #change
        return user_email
    return get_current_user


def register_finish():
    async def get_current_user(
            token: str = Depends(oauth2_scheme),
            user_repo: UserRepository = Depends(get_repository(UserRepository))
    ):
        if token is None:
            raise BaseException  # change
        auth_repo = AuthRepository()
        user_email = await auth_repo.decode_register_finish(token)
        if user_email is None:
            raise BaseException  # change
        is_already_exists = await user_repo.check_user(user_email)
        if is_already_exists:
            raise BaseException  # change
        exists = await auth_repo.check_user_exists(user_email)
        if not exists:
            raise BaseException  # change
        return user_email
    return get_current_user
