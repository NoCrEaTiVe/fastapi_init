from fastapi import APIRouter, Depends, status
from app.models.schemas.auth import UserCreate, Password, UserLogin
from app.db.repositories.authentication import AuthRepository
from app.db.repositories.users import UserRepository
from app.api.dependencies.auth import register_verify, register_finish
from app.api.dependencies.database import get_repository
from app.models.schemas.users import UserOut
from app.api.dependencies.users import login_validation, registration_validation


router = APIRouter(tags=['User'])


@router.post(
    "/register",
    dependencies=[Depends(registration_validation)],
    status_code=200,
)
async def register(
       request: UserCreate,
):
    auth_repo = AuthRepository()
    access_token = await auth_repo.register(request)

    return access_token


@router.post(
    "/register/verify",
    status_code=200,
)
async def verify_register(
        code: str,
        email: str = Depends(register_verify())

):
    auth_repo = AuthRepository()
    access_token = await auth_repo.register_verify(email, code)
    return access_token


@router.post(
    "/register/finish",
    response_model=UserOut,
    status_code=200,
)
async def finish_register(
        request: Password,
        email: str = Depends(register_finish()),
        user_repo: UserRepository = Depends(get_repository(UserRepository))
):
    result = await user_repo.create_user(request.password, email)
    return result


@router.post(
    "/login",
    dependencies=[Depends(login_validation)],
    status_code=200,
)
async def login(
        request: UserLogin,
        user_repo: UserRepository = Depends(get_repository(UserRepository))
):
    user = await user_repo.get_user(request.email)
    auth_repo = AuthRepository()
    access_token = await auth_repo.access_token(user.id)
    return access_token




