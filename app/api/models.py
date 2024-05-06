from pydantic import BaseModel
from typing import List, Optional

class LanguageIn(BaseModel):
    name: str
    description: str
    count_users: str
    year: str


class LanguageOut(LanguageIn):
    id: int
