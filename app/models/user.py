from pydantic import BaseModel, EmailStr, Field, validator
from typing import List
from uuid import UUID, uuid4
from datetime import datetime
import re

class Phone(BaseModel):
    number: str
    citycode: str
    contrycode: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phones: List[Phone]

    @validator("password")
    def validate_password(cls, v):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=(.*\d.*\d))[A-Za-z\d]+$', v):
            raise ValueError("La contraseña debe tener una mayúscula, letras minúsculas y al menos dos números")
        return v

class UserInDB(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    email: EmailStr
    password: str

