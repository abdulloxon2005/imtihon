from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.repo.retsept_repo import (
    get_all_retsept,
    create_retsept,
    get_name_retsept,
    delete_retsept as repo_delete_retsept,
    update_retsept as repo_update_retsept,
)
from app.schemas.taomlar_schemas import CreateRetsept, RetseptResponse

router = APIRouter()


@router.get("/recipes", response_model=List[RetseptResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_retsept(db)





@router.delete("/recipes/{retsept_id}")
def delete_retsept(retsept_id: int, db: Session = Depends(get_db)):
    return repo_delete_retsept(db, retsept_id)


@router.put("/recipes/{retsept_id}", response_model=RetseptResponse)
def update_retsept(
    retsept_id: int,
    retsept: CreateRetsept,
    db: Session = Depends(get_db),
):
    return repo_update_retsept(db, retsept_id, retsept)


@router.get("/recipes/search", response_model=List[RetseptResponse])
def get_name(name: str, db: Session = Depends(get_db)):
    return get_name_retsept(db, name)
