from typing import List
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.models.something import SomethingCreate, SomethingPublic, SomethingAll
from app.db.repositories.something import SomethingRepository
from app.api.dependencies.database import get_repository


router = APIRouter()

@router.post("/", response_model=SomethingPublic, name="create-something", status_code=HTTP_201_CREATED)
async def create_new_something(
    new_something: SomethingCreate = Body(..., embed=True),
    something_repo: SomethingRepository = Depends(get_repository(SomethingRepository)),
) -> SomethingPublic:
    created_something = await something_repo.create_something(new_something=new_something)
    return created_something


@router.get("/", response_model=SomethingAll, name="get-all-something", status_code=HTTP_200_OK)
async def get_all_something(
    something_repo: SomethingRepository = Depends(get_repository(SomethingRepository)),
) -> SomethingAll:
    get_all_something = await something_repo.get_all_something()
    return get_all_something

