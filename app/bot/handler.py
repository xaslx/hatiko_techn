from typing import Any

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka, inject

from app.fastapi.infrastructure.imei_checker import IMEIChecker
from app.fastapi.schemas.imei import IMEIOut, converter_to_imei_schema


router: Router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(text='Отправьте IMEI')
    

@router.message()
@inject
async def check_imei(message: Message, imei_checker: FromDishka[IMEIChecker]):
    
    if not (8 <= len(message.text) <= 15):
        return await message.answer(text='IMEI должен быть от 8 до 15 символов')
    
    try:
        res: dict[str, Any] = await imei_checker.check_imei(device_id=message.text)
        imei_schema: IMEIOut = converter_to_imei_schema(data=res)
        return await message.answer(
            text=(
                f'🔢 IMEI: {imei_schema.imei}\n'
                f'🔢 IMEI2: {imei_schema.imei2}\n'
                f'📱 Device: {imei_schema.device_name}\n'
                f'🔑 Seria: {imei_schema.serial}\n'
                f'🖼️ Image: {imei_schema.image_url}'
            ),
        )
    except Exception:
        return await message.answer(text='Возможно вы ввели неверный IMEI')
