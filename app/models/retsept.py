from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,String

from app.db.base import Base


class Retsepts(Base):
    __tablename__ = "retsepts"

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String,nullable=True)
    description:Mapped[str] = mapped_column(String,nullable=True)
    masalliqlar:Mapped[str] = mapped_column(String)


