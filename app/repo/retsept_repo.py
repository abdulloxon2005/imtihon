from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.retsept import Retsepts
from app.schemas.taomlar_schemas import CreateRetsept, UpdateRetsept

def create_retsept(db:Session,retsept:CreateRetsept):
    db_retsept =Retsepts(name=retsept.name,description=retsept.description,masalliqlar=retsept.masalliqlar)
    db.add(db_retsept)
    db.commit()
    db.refresh(db_retsept)
    return db_retsept

def get_all_retsept(db:Session):
       return db.query(Retsepts).all()


def get_name_retsept(db:Session,name:str):
    retsept = db.query(Retsepts).filter(Retsepts.name == name).first()
    if not retsept:
        raise HTTPException(status_code=404,detail="Malumot topilmadi")
    return retsept

def delete_retsept(db:Session,retsept_id:int):
    db_retseptd = db.query(Retsepts).filter(Retsepts.id == retsept_id).first()
    if not db_retseptd:
        raise HTTPException(status_code=404,detail="Malumot topilmadi")
    db.delete(db_retseptd)
    db.commit()
    db.refresh(db_retseptd)
    return db_retseptd

def retsept_update(db:Session,retsept_id:int,retsept:UpdateRetsept):
    db_retsept = db.query(Retsepts).filter(Retsepts.id ==retsept_id).first()
    if not db_retsept:
        raise HTTPException(status_code=404,detail="Malumot topilmadi")
    db_retsept.name =retsept.name
    db_retsept.description =retsept.description
    db_retsept.masalliqlar = retsept.masalliqlar
    db.commit()
    db.refresh(db_retsept)

    return db_retsept