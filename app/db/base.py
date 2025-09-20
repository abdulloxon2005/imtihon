from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///retsept.db")

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine)
