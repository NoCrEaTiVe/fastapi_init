from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordManager:
    def __init__(self, password):
        self.password = password

    def verify_password(self, hashed_password):
        return pwd_context.verify(self.password, hashed_password)

    def get_password_hash(self):
        return pwd_context.hash(self.password)


