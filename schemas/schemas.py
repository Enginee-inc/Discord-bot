# build a schema using pydantic
from pydantic import BaseModel
from pydantic.schema import Optional


class Schema_Discord(BaseModel):
    relation: str
    sum: int

    class Config:
        orm_mode = True