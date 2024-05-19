import aiohttp
import asyncio



async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()
    

async def fetch_all_movies_by_year(base_url, year):
    url = base_url
    params = {'year': year}
    movies_titles = []

    async with aiohttp.ClientSession() as session:
        while url:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    for movie in data['results']:
                        movies_titles.append(movie['title'])
                        url = data.get('next')
                        params = {}
                else:
                    print(f"Erreur : {response.status}")
                    break
        return movies_titles

async def main():
    base_url = 'http://127.0.0.1:8000/api/v1/titles/'
    year = 2020
    titles = await fetch_all_movies_by_year(base_url, year)
    for title in titles:
        print(title)

# Lancer le script
asyncio.run(main())
