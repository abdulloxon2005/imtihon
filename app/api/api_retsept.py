from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.repo.retsept_repo import get_all_retsept, create_retsept, get_name_retsept
from app.schemas.taomlar_schemas import CreateRetsept, RetseptResponse

router = APIRouter()

@router.get("/recipes",response_model=RetseptResponse)
def get_all(db:Session = Depends(get_db)):
    return get_all_retsept(db)


@router.post("/create",response_model=RetseptResponse)
def add_retsept(retsept:CreateRetsept,db:Session=Depends(get_db)):
    return create_retsept(db,retsept)


@router.delete("/{retsept_id}")
def delete_retsept(retsept_id:int):
    return delete_retsept(retsept_id)


@router.put("recipes/{id}")
def update_retsept(retsept_id:int,db:Session=Depends(get_db)):
    return update_retsept(retsept_id, db)


@router.get("/recipes/search?name=")
def get_name(name:str,db:Session = Depends(get_db)):
    return get_name_retsept(db,name)