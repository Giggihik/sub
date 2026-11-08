import pytest
import pytest_asyncio
from unittest.mock import patch, AsyncMock
from connection import AsyncConnection, read_timetable 

@pytest_asyncio.fixture
async def connection():
    conn = AsyncConnection()
    await conn.connect()
    yield conn 
    await conn.close()

@pytest.mark.asyncio
async def test_connection_is_open(connection):
    assert connection.is_open is True


@pytest.mark.asyncio
@patch('connection.main', new_callable=AsyncMock) 
async def test_read_timetable(mock_main):
    mock_main.return_value = {"weather": "Любая погода"}
    
    result = await read_timetable()
    mock_main.assert_called_once()
    

    assert result is False

    mock_main.return_value = {"weather": "sunny"}
    assert await read_timetable() is True