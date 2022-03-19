from app.models.common import BaseModel
from pydantic import EmailStr


class UserOut(BaseModel):
    id: int
    first_name: str
    email: EmailStr
    last_name: str

    class Config(BaseModel.Config):
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "first_name": "Jane",
                "email": "jdoe@example.com",
                "last_name": "Doe"
            }
        }
