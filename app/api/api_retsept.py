from typing import List

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.repo.retsept_repo import get_all_retsept, create_retsept, get_name_retsept, retsept_update, delete_retsept, \
    search_retsept_masalliq
from app.schemas.taomlar_schemas import CreateRetsept, RetseptResponse, UpdateRetsept

router = APIRouter()

@router.get("/recipes",response_model=List[RetseptResponse])
def get_all(db:Session = Depends(get_db)):
    return get_all_retsept(db)


@router.post("/create")
def add_retsept(retsept:CreateRetsept,db:Session=Depends(get_db)):
    return create_retsept(db,retsept)


@router.delete("/{retsept_id}")
def delete_retsep(retsept_id:int,db:Session = Depends(get_db)):
    return delete_retsept(db,retsept_id)


@router.put("/recipes/{retsept_id}")
def update_retse(retsept_id: int, retsept: UpdateRetsept, db: Session = Depends(get_db)):
    return retsept_update(db, retsept_id, retsept)

@router.get("/recipes/search")
def search_recipes(masalliq: str, db: Session = Depends(get_db)):
    return search_retsept_masalliq(db, masalliq)


@router.get("/recipes/name=")
def get_name(name:str,db:Session = Depends(get_db)):
    return get_name_retsept(db,name)