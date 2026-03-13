from unittest.mock import MagicMock, patch
from app.services.storage.s3 import S3Service


def test_generate_upload_url():

    bucket = "test-bucket"
    region = "us-east-1"

    fake_url = "https://signed-url"

    with patch("app.services.storage.s3.boto3.client") as mock_client:

        mock_s3 = MagicMock()
        mock_client.return_value = mock_s3

        mock_s3.generate_presigned_url.return_value = fake_url

        service = S3Service(bucket=bucket, region=region)

        result = service.generate_upload_url(
            filename="file.png",
            content_type="image/png",
        )

        assert result["upload_url"] == fake_url
        assert "uploads/" in result["key"]
        assert result["key"].endswith("file.png")

        mock_s3.generate_presigned_url.assert_called_once()
