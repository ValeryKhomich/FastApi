from pydantic import BaseModel


class User(BaseModel):
    name: str
    message: str
    age: int