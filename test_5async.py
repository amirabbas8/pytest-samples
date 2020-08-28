import pytest
async def get():
    return 1 + 2


@pytest.mark.asyncio
async def test_get():
    assert await get() == 3