import aiohttp
import json
from typing import Any
from fastapi import HTTPException


class IMEIChecker:
    
    def __init__(self, token: str, base_url: str = 'https://api.imeicheck.net/v1/checks'):
        
        self.base_url = base_url
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    async def check_imei(self, device_id: str, service_id: int = 12) -> dict[str, Any]:
        
        body = json.dumps({
            'deviceId': device_id,
            'serviceId': service_id
        })
        
        try:
            async with aiohttp.ClientSession() as session:
                
                async with session.post(self.base_url, headers=self.headers, data=body) as response:
                    
                    if response.status == 201:
                        return await response.json()
                    else:
                        error = await response.json()
                        raise HTTPException(
                            status_code=response.status,
                            detail=f'{error}',
                        )
        except aiohttp.ClientError as e:
            
            raise HTTPException(
                status_code=500,
                detail=f'Ошибка сети: {str(e)}',
            )