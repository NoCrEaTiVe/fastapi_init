from datetime import datetime, timedelta
from typing import Optional, Dict
from jose import jwt
from app.models.schemas.jwt import JWTMeta


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24
JWT_SUBJECT = "access"


def create_jwt_token(
    *,
    jwt_content: Dict[str, str],
    secret_key: str,
    expires_delta: Optional[timedelta] = None,
) -> str:
    to_encode = jwt_content.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update(JWTMeta(exp=expire, sub=JWT_SUBJECT).dict())
    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)


def decode_jwt_token(
    token, secret_key: str,
):
    return jwt.decode(token, secret_key, algorithms=[ALGORITHM])
