from app.api.models import LanguageIn, LanguageOut
from app.api.db import languages, database


async def add_language(payload: LanguageIn):
    query = languages.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_language():
    query = languages.select()
    return await database.fetch_all(query=query)


async def get_language(id):
    query = languages.select().where(languages.c.id == id)
    return await database.fetch_one(query=query)


async def delete_language(id: int):
    query = languages.delete().where(languages.c.id == id)
    return await database.execute(query=query)

