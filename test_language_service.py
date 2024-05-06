import pytest
from app.api.models import LanguageIn, LanguageOut

languages = LanguageIn(
    name='Bitcoin',
    description='Это высокоуровневый язык программирования, который появился в конце 80-х годов благодаря программисту Гвидо ван Россуму',
    count_users='10000000',
    year='1991'
)


def test_create_language(languages: LanguageIn = languages):
    assert dict(languages) == {'name': languages.name,
                               'description': languages.description,
                               'count_users': languages.count_users,
                               'year': languages.year
                               }


def test_update_language_age(languages: LanguageIn = languages):
    language_upd = LanguageOut(
        name='Bitcoin',
        description='Это высокоуровневый язык программирования, который появился в конце 80-х годов благодаря программисту Гвидо ван Россуму',
        count_users='10000000',
        year='1991',
        id=1
    )
    assert dict(language_upd) == {'name': languages.name,
                                  'description': languages.description,
                                  'count_users': languages.count_users,
                                  'year': languages.year,
                                  'id': language_upd.id
                                  }


def test_update_language_genre(languages: LanguageIn = languages):
    language_upd = LanguageOut(
        name='Bitcoin',
        description='Это высокоуровневый язык программирования, который появился в конце 80-х годов благодаря программисту Гвидо ван Россуму',
        count_users='10000000',
        year='1991',
        id=1
    )
    assert dict(language_upd) == {'name': languages.name,
                                  'description': languages.description,
                                  'count_users': languages.count_users,
                                  'year': languages.year,
                                  'id': language_upd.id
                                  }
