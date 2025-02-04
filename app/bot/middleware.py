from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class AccessMiddleware(BaseMiddleware):
    
    def __init__(self, whitelist: list[int]):
        self.whitelist = whitelist

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        
        user_id: int = event.message.from_user.id
        
        if user_id not in self.whitelist:
            return await event.message.answer('У вас нет доступа')
        
        return await handler(event, data)