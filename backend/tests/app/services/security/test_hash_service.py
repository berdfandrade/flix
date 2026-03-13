import pytest
from app.services.security.hash import HashService


@pytest.fixture
def hash_service():
    return HashService()


def test_hash_password_returns_string(hash_service):
    password = "123456"

    hashed = hash_service.hash_password(password)

    assert isinstance(hashed, str)
    assert hashed != password


def test_verify_password_success(hash_service):
    password = "123456"

    hashed = hash_service.hash_password(password)

    result = hash_service.verify_password(password, hashed)

    assert result is True


def test_verify_password_failure(hash_service):
    password = "123456"

    hashed = hash_service.hash_password(password)

    result = hash_service.verify_password("wrong_password", hashed)

    assert result is False


def test_hash_is_random(hash_service):
    password = "123456"

    hash1 = hash_service.hash_password(password)
    hash2 = hash_service.hash_password(password)

    assert hash1 != hash2
    assert hash_service.verify_password(password, hash1)
    assert hash_service.verify_password(password, hash2)
