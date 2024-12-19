from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from temperature.crud import update_temperature_for_cities, get_list_of_all_temperature_records, \
    get_temperature_by_city_id
from dependencies import get_db
from temperature.schemas import Temperature, OnlineResponse

router = APIRouter()

@router.post("/temperature/updates", response_model=OnlineResponse, tags=["Temperature CRUD"])
async def update_all_temperature_for_cities(db: Session = Depends(get_db)):
    result = await update_temperature_for_cities(db)
    return result

@router.get("/temperatures", response_model=list[Temperature] , tags=["Temperature CRUD"])
async def get_all_temperature(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_list_of_all_temperature_records(db, skip, limit)


@router.get("/temperature/{city_id}", response_model=list[Temperature], tags=["Temperature CRUD"])
async def get_all_temperature_by_city_id(city_id: int, db: Session = Depends(get_db)):
    return get_temperature_by_city_id(db, city_id)