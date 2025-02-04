from aiogram import Bot, Dispatcher
from dishka import Provider, Scope, from_context, provide

from app.config import Config
from app.fastapi.infrastructure.imei_checker import IMEIChecker


class AppProvider(Provider):
    
    config: Config = from_context(provides=Config, scope=Scope.APP)
    
    @provide(scope=Scope.REQUEST)
    def get_imei_checker(self, config: Config) -> IMEIChecker:
        return IMEIChecker(
            token=config.imei_api_service_token
        )
    
    @provide(scope=Scope.APP)
    def get_bot(self, config: Config) -> Bot:
        return Bot(token=config.bot_token)

    @provide(scope=Scope.APP)
    def get_dispatcher(self) -> Dispatcher:
        return Dispatcher()