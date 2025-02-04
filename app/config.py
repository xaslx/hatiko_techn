from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    bot_token: str = Field(alias='BOT_TOKEN')
    api_token: str = Field(alias='API_TOKEN')
    imei_api_service_token: str = Field(alias='IMEI_API_SERVICE_TOKEN')