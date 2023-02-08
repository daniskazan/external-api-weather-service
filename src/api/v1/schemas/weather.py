from pydantic import BaseModel as Base
from pydantic import HttpUrl
from humps import camelize
from typing import List
import datetime


class BaseModel(Base):
    class Config:
        orm_mode = True
        alias_generator = camelize
        allow_population_by_field_name = True


class Forecast(BaseModel):
    date: datetime.date
    max_temp_c: float
    max_temp_f: float
    min_temp_c: float
    min_temp_f: float
    avg_temp_c: float
    avg_temp_f: float
    will_it_rain: bool
    chance_of_rain: int
    condition: str
    icon_url: HttpUrl
    sunrise: str
    sunset: str
    max_wind_mph: float
    max_wind_kph: float


class WeatherOut(BaseModel):
    country: str
    forecast: List[Forecast]
    latitude: float
    local_time: str
    location: str
    longitude: float
    region: str
    timezone: str
