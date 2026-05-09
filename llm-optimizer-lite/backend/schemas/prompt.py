from pydantic import BaseModel


class PromptCreate(BaseModel):
    name: str


class PromptVersionCreate(BaseModel):
    version: int
    content: str


class PromptOut(BaseModel):
    id: int
    name: str
    active_version: int
