from fastapi import Depends, FastAPI
import uvicorn
from functools import lru_cache
from core import config

app = FastAPI()


@lru_cache
def get_settings():
    return config.Settings()


@app.get("/")
async def info(settings: config.Settings = Depends(get_settings)):  # noqa
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "db_url": settings.db_url,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
