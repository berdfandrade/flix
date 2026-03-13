import pytest
from app.services.users import UserService
from app.services.security.hash import HashService
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User


@pytest.fixture
def user_service():
    return UserService(HashService())


@pytest.mark.asyncio
async def test_create_user(user_service, test_db):

    data = UserCreate(
        name="Bernardo",
        email="bernardo@email.com",
        password="12345678",
    )

    user = await user_service.create_user(data)

    assert user.id is not None
    assert user.email == data.email
    assert user.password_hash != "12345678"


@pytest.mark.asyncio
async def test_email_must_be_unique(user_service, test_db):

    data = UserCreate(
        name="Bernardo",
        email="bernardo@email.com",
        password="12345678",
    )

    await user_service.create_user(data)

    with pytest.raises(ValueError):
        await user_service.create_user(data)


@pytest.mark.asyncio
async def test_get_user(user_service, test_db):

    data = UserCreate(
        name="Bernardo",
        email="bernardo@email.com",
        password="12345678",
    )

    created = await user_service.create_user(data)

    found = await user_service.get_user(created.id)

    assert found is not None
    assert found.id == created.id


@pytest.mark.asyncio
async def test_get_user_by_email(user_service, test_db):

    data = UserCreate(
        name="Bernardo",
        email="bernardo@email.com",
        password="12345678",
    )

    await user_service.create_user(data)

    found = await user_service.get_user_by_email("bernardo@email.com")

    assert found is not None
    assert found.email == "bernardo@email.com"


@pytest.mark.asyncio
async def test_update_user_name(user_service, test_db):

    data = UserCreate(
        name="Bernardo",
        email="bernardo@email.com",
        password="12345678",
    )

    created = await user_service.create_user(data)

    update = UserUpdate(name="Bernardo Silva", password="")

    updated = await user_service.update_user(created.id, update)

    assert updated.name == "Bernardo Silva"


@pytest.mark.asyncio
async def test_update_user_password(user_service, test_db):

    data = UserCreate(
        name="Bernardo",
        email="bernardo@email.com",
        password="12345678",
    )

    created = await user_service.create_user(data)

    update = UserUpdate(name="", password="newpassword")

    updated = await user_service.update_user(created.id, update)

    assert updated.password_hash != created.password_hash


@pytest.mark.asyncio
async def test_delete_user(user_service, test_db):

    data = UserCreate(
        name="Bernardo",
        email="bernardo@email.com",
        password="12345678",
    )

    created = await user_service.create_user(data)

    result = await user_service.delete_user(created.id)

    assert result is True

    user = await User.get(created.id)

    assert user is None
