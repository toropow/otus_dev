from tortoise import Tortoise, run_async
from dataclasses import dataclass
from aiohttp import ClientSession
import asyncio
import models
from config import TORTOISE_ORM

ALBUMS = 'albums'
PHOTOS = 'photos'


@dataclass
class Source:
    name: str
    url: str


sources = [
    Source(name=ALBUMS, url='https://jsonplaceholder.typicode.com/albums'),
    Source(name=PHOTOS, url='https://jsonplaceholder.typicode.com/photos')

]


async def init():
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()


async def fetch(session: ClientSession, url) -> dict:
    async with session.get(url) as response:
        result = await response.json()
        return result


async def fetch_data(url):
    async with ClientSession() as session:
        result = await fetch(session, url)
    return result


async def get_data_from_src(src: Source):
    result = await asyncio.wait([fetch_data(src.url)], timeout=10)
    return src.name, result


async def albums_write(albums: list):
    for album in albums:
        await models.Album.create(
            user_id=album['userId'],
            id=album['id'],
            title=album['title']
        )


async def photos_write(photos: list):
    for photo in photos:
        await models.Photo.create(
            album_id_id=photo['albumId'],
            id=photo['id'],
            title=photo['title'],
            url=photo['url'],
            thumbnail_url=photo['thumbnailUrl']
        )


async def run():
    await init()
    tasks = [get_data_from_src(src) for src in sources]
    done, _ = await asyncio.wait(tasks)
    for res in done:
        name, data = res.result()
        if name == ALBUMS:
            albums_data = list(data[0])[0].result()
            await albums_write(albums_data)
        elif name == PHOTOS:
            photos_data = list(data[0])[0].result()
            await photos_write(photos_data)
        else:
            Exception("Unknown source!!!!")


if __name__ == '__main__':
    run_async(run())
