from fastapi import APIRouter
from api.v1.endpoints import weather


router = APIRouter()

router.include_router(weather.router)
