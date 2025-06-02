from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict

from app.domains.users.models import UserRole


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    username: str
    email: EmailStr
    password: str
    role: UserRole

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "testuser05",
                "email": "testemail@mail.com",
                "password": "securePassword!23",
                "role": "admin or student or professor"
            }
        }
    )


class UserLogin(BaseModel):
    username: str
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "testuser05",
                "password": "securePassword!23"
            }
        }
    )


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: str
    role: UserRole
    is_active: bool


class UserWithStudent(BaseModel):
    user: UserResponse
    student: Optional[UserRead] = None


class Token(BaseModel):
    access_token: str
    token_type: str
