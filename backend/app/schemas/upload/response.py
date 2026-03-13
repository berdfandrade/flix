from pydantic import BaseModel


class UploadResponse(BaseModel):
    upload_url: str
    key: str
