from fastapi import APIRouter
from app.schemas.upload import UploadRequest, UploadResponse
from app.services.storage.s3 import S3Service
from app.core.config import settings

router = APIRouter()

s3_service = S3Service(bucket=settings.bucket, region=settings.region)


@router.post("/upload-movie", response_model=UploadResponse)
async def generate_upload_url(data: UploadRequest):

    result = s3_service.generate_upload_url(
        filename=data.filename, content_type=data.content_type
    )

    return result
