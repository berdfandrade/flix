from fastapi import APIRouter

from .health import router as api_health_router
from .upload import router as api_upload_router

api_router = APIRouter(prefix="/api")

api_router.include_router(api_health_router)
api_router.include_router(api_upload_router)
