import boto3
from botocore.client import Config
import uuid


class S3Service:

    def __init__(self, bucket: str, region: str):
        self.bucket = bucket

        self.client = boto3.client(
            "s3",
            region_name=region,
            config=Config(signature_version="s3v4"),
        )

    def generate_upload_url(self, filename: str, content_type: str):

        key = f"uploads/{uuid.uuid4()}-{filename}"

        url = self.client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": self.bucket,
                "Key": key,
                "ContentType": content_type,
            },
            ExpiresIn=300,
        )

        return {
            "upload_url": url,
            "key": key,
        }
