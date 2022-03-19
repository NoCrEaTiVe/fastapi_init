from fastapi import Depends
from app.db.repositories.users import UserRepository
from app.api.dependencies.database import get_repository
from app.models.schemas.auth import UserLogin, UserCreate
from app.services.auth.authentication import PasswordManager


async def login_validation(
        request: UserLogin,
        user_repo: UserRepository = Depends(get_repository(UserRepository))
):
    user = await user_repo.get_user(email=request.email)
    if user is None:
        raise BaseException  #change
    password_manager = PasswordManager(request.password)
    if not password_manager.verify_password(user.hashed_password):
        raise BaseException  #change


async def registration_validation(
        request: UserCreate,
        user_repo: UserRepository = Depends(get_repository(UserRepository))
):
    is_exists = await user_repo.check_user(email=request.email)
    if is_exists:
        raise BaseException  #change

