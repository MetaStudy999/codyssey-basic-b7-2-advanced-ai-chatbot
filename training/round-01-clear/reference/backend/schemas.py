from pydantic import BaseModel, Field


class SignupIn(BaseModel):
    email: str = Field(min_length=3, max_length=255)
    username: str = Field(min_length=2, max_length=80)
    password: str = Field(min_length=8, max_length=128)


class LoginIn(BaseModel):
    email: str
    password: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ChatSessionCreate(BaseModel):
    title: str = Field(min_length=1, max_length=160)


class MessageCreate(BaseModel):
    content: str = Field(min_length=1, max_length=8000)


class PostCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1, max_length=20000)


class PostUpdate(PostCreate):
    pass
