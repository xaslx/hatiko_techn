from dishka import AsyncContainer, make_async_container
from fastapi import FastAPI
from app.ioc import AppProvider
from app.fastapi.routers.imei import router
from dishka.integrations import fastapi as fastapi_integration
from app.config import Config


def create_app() -> FastAPI:
    
    config: Config = Config()
    container: AsyncContainer = make_async_container(AppProvider(), context={Config: config})
    
    app: FastAPI = FastAPI()
    app.include_router(router=router, prefix='/api/v1')
    

    fastapi_integration.setup_dishka(container=container, app=app)
    
    return app