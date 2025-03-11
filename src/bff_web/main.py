# import asyncio
# import datetime
# import time
# import traceback
# import uuid
from typing import Any

import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseSettings
from starlette.responses import JSONResponse

# from . import utils
from .api.v1.router import router as v1

# from .despachadores import Despachador


class Config(BaseSettings):
    APP_VERSION: str = "1"


settings = Config()
app_configs: dict[str, Any] = {"title": "BFF-Web SaludTech"}

app = FastAPI(**app_configs)


@app.get("/health")
async def health(request: Request):
    return JSONResponse({"status": "ok"})


app.include_router(v1, prefix="/v1")
