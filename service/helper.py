from typing import Any
from fastapi.responses import JSONResponse
from models.model import ResponseModel

def create_response(status: bool, data: Any, status_code: int = 200):
    return JSONResponse(
        status_code=status_code,
        content=ResponseModel(status=status, data=data).model_dump()
    )