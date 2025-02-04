from aiogram import Bot, Dispatcher
from dishka import AsyncContainer, make_async_container
from dishka.integrations.aiogram import setup_dishka
from app.ioc import AppProvider
import asyncio
from app.config import Config
from app.bot.handler import router
from app.bot.middleware import AccessMiddleware


async def main() -> None:
    
    config = Config()
    
    whitelist: list[int] = [340906161]

    bot_container: AsyncContainer = make_async_container(
        AppProvider(), context={Config: config}
    )
    dp: Dispatcher = await bot_container.get(Dispatcher)
    bot: Bot = await bot_container.get(Bot)
    dp.include_router(router=router)
    dp.update.middleware.register(AccessMiddleware(whitelist=whitelist))
    setup_dishka(router=dp, container=bot_container)

    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())