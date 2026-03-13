from fastapi import APIRouter

router = APIRouter()


@router.get("/check-health")
async def check_health():
    return {"message": "Api Alive!"}
