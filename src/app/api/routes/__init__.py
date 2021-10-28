from fastapi import APIRouter
from app.api.routes.something import router as something_router

router = APIRouter()

router.include_router(something_router, prefix="/something", tags=["something"])
