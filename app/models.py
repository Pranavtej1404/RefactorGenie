from pydantic import BaseModel
from typing import List, Literal

class CodeInput(BaseModel):
    language: Literal['python', 'javascript']
    code: str

class Suggestion(BaseModel):
    line: int
    type: str
    message: str

class SuggestionsOutput(BaseModel):
    suggestions: List[Suggestion]
