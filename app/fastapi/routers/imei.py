from typing import Annotated, Any

from dishka.integrations.fastapi import FromDishka as Depends
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Query, status

from app.config import Config
from app.fastapi.exception import InvalidTokenException
from app.ioc import IMEIChecker
from app.fastapi.schemas.imei import IMEIOut, converter_to_imei_schema


router: APIRouter = APIRouter(tags=['Проверка IMEI устройств'])


@router.post(
    '/check-imei',
    status_code=status.HTTP_201_CREATED,
    description='Эндпоинт для проверки IMEI устрйоств',
)
@inject
async def check_imei_handler(
    imei: Annotated[
        str, 
        Query(
            min_length=8,
            max_length=15,
            description='IMEI должен быть от 8 до 15 символов',
        )
    ],
    token: Annotated[str, Query()],
    config: Depends[Config],
    imei_checker: Depends[IMEIChecker],
) -> IMEIOut | None:
    
    if token != config.api_token:
        raise InvalidTokenException()
    
    res: dict[str, Any] = await imei_checker.check_imei(device_id=imei)
    
    if res:
        return converter_to_imei_schema(data=res)
    return None