import time
import aiohttp
import asyncio

async def fetch_user(session):
    response = await session.get(f"https://jsonplaceholder.typicode.com/users")
    response_json = await response.json()
    return response_json
         

async def main():
    time_start=time.time()
    async with aiohttp.ClientSession() as session:

        lista_korutina=[fetch_user(session) for i in range(5)]
        rezultat = await asyncio.gather(*lista_korutina)

        user_names=[user["name"] for user in rezultat[0]]
        user_usernames=[user["username"] for user in rezultat[0]]
        user_email=[user["email"] for user in rezultat[0]]
        print("Imena: ", user_names)
        print("Usernames: ", user_usernames)
        print("E-mails: ", user_email)
    time_end=time.time()
    total_time=time_end-time_start
    print(f"Vrijeme izvrsavanja:{total_time}")
asyncio.run(main())