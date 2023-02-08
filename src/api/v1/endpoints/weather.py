from fastapi import APIRouter, Depends
from fastapi import status, Query
from api.v1.services.weather_service import (
    ExternalWeatherAPIService,
    get_weather_service,
)
from api.v1.schemas.weather import WeatherOut

router = APIRouter(prefix="/weather/m3o", tags=["weather"])


@router.get(
    "/forecast",
    description="This endpoint uses external api!",
    responses={status.HTTP_200_OK: {"model": WeatherOut}},
)
async def get_weather_forecast(
    location: str,
    days: int = Query(default=1, ge=1, le=10),
    weather_service: ExternalWeatherAPIService = Depends(get_weather_service),
):
    return await weather_service.forecast(days, location)


@router.get(
    "/current",
    description="This endpoint uses external api! Get current weather for location",
)
async def get_current_weather(
    location: str,
    weather_service: ExternalWeatherAPIService = Depends(get_weather_service),
):
    return await weather_service.current_weather(location=location)
