import aiohttp

class AsyncConnection:
    async def connect(self): 
        self.is_open = True
        
    async def close(self): 
        self.is_open = False


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://weather.com') as response:
            response = await response.json()
            return response

async def read_timetable():
    response = await main()
    return response["weather"] == "sunny"