from typing import Any
from pydantic import BaseModel, HttpUrl


class IMEIOut(BaseModel):
    imei: str
    device_name: str
    imei2: str
    serial: str
    image_url: HttpUrl
    
    
def converter_to_imei_schema(data: dict[str, Any]) -> IMEIOut:
    
    return IMEIOut(
        imei=data['properties']['imei'],
        device_name=data['properties']['deviceName'],
        imei2=data['properties']['imei2'],
        serial=data['properties']['serial'],
        image_url=data['properties']['image'],
    )