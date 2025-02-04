from fastapi import HTTPException, status
from dataclasses import dataclass


@dataclass
class InvalidTokenException(HTTPException):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    detail: str = 'Невалидный API токен'