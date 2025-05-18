from uuid import uuid4
from pydantic import BaseModel, Field


class AnswerResponse(BaseModel):
    text: str = Field(examples=["HI, how are you?"])


class LoginRequest(BaseModel):
    username: str = Field(examples=["admin"])
    password: str = Field(examples=["admin"])


class UserMetadataSchemas(BaseModel):
    ...

class LoginResponse(BaseModel):
    id: str = Field(examples=[str(uuid4())])
    display_name: str = Field(examples=["Admin"])
    metadata: UserMetadataSchemas
