from sqlalchemy import Column, String
from src.app_core.db import Base
from sqlalchemy import Integer, String, Column

class FileMapping(Base):
    __tablename__ = "file_mappings"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, nullable=False)
    file_name = Column(String, unique=True, nullable=False) 
