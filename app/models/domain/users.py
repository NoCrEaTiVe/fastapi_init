from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    Enum,
    BigInteger
)

from app.db.database import Base


class User(Base):
    __tablename__ = 'Users'
    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(100), nullable=True)
    hashed_password = Column(Text, nullable=False)
    # status = Column(Enum(UserStatus), default=None, nullable=True)