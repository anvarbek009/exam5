import requests
import asyncio

async def fetch_data():
    url = "https://dummyjson.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Ma'lumotlar olinmadi")

asyncio.run(fetch_data())