from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    group: str

class StudentCreateSchema(StudentBase):
    pass

class StudentResponseSchema(StudentBase):
    id: int

    class Config:
        orm_mode = True
