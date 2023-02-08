import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "local")
    M3O_API_TOKEN: str = os.environ.get("M3O_API_TOKEN", "fill_me")
    BASE_WEATHER_URL = "https://api.m3o.com/v1/weather"

    CI_COMMIT_SHA: str = os.environ.get("CI_COMMIT_SHA", "unknown")
    CI_COMMIT_REF_NAME: str = os.environ.get("CI_COMMIT_REF_NAME", "unknown")
    GITLAB_USER_NAME: str = os.environ.get("GITLAB_USER_NAME", "unknown")


app_config = Config()
