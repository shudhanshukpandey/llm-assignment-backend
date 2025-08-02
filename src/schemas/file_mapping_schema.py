from pydantic import BaseModel

class FileMappingSchema(BaseModel):
    uuid: str
    file_name: str

    class Config:
        orm_mode = True