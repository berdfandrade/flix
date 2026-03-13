import pytest


@pytest.mark.asyncio
async def test_database_connection(test_db):

    result = await test_db.command("ping")

    assert result["ok"] == 1
