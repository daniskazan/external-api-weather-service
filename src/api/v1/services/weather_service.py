from functools import lru_cache
from core.config import app_config
import aiohttp
from typing import Dict


class ExternalWeatherAPIService:
    def __init__(self, **kwargs):
        self.base_url: str = app_config.BASE_WEATHER_URL
        self.headers: dict = {
            "Authorization": f"Bearer {app_config.M3O_API_TOKEN}",
            "Content-Type": "application/json",
        }

    async def _process_request(self, **kwargs):
        url = (
            self.base_url + "/Forecast"
            if kwargs.get("days")
            else self.base_url + "/Now"
        )
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(url=url, json=kwargs) as resp:
                return await resp.json()

    async def forecast(self, days: int, location: str) -> Dict:
        return await self._process_request(days=days, location=location)

    async def current_weather(self, location: str) -> Dict:
        return await self._process_request(location=location)


@lru_cache()
def get_weather_service():
    return ExternalWeatherAPIService()
