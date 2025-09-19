from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

engine = create_engine("sqlite:///retsept.db")

class Base(DeclarativeBase):
    pass

Base.metadata.create_all(engine)
