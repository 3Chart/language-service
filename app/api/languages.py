from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import LanguageIn, LanguageOut
from app.api import db_manager

languages = APIRouter()

@languages.post('/', response_model=LanguageIn, status_code=201)
async def create_language(payload: LanguageOut):
    language_id = await db_manager.add_language(payload)

    response = {
        'id': language_id,
        **payload.dict()
    }

    return response


@languages.get('/', response_model=List[LanguageIn])
async def get_languages():
    return await db_manager.get_all_language()


@languages.get('/{id}/', response_model=LanguageIn)
async def get_language(id: int):
    company = await db_manager.get_language(id)
    if not company:
        raise HTTPException(status_code=404, detail="language not found")
    return company


@languages.delete('/{id}/', response_model=None)
async def delete_language(id: int):
    company = await db_manager.get_language(id)
    if not company:
        raise HTTPException(status_code=404, detail="language not found")
    return await db_manager.delete_language(id)