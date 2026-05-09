from pydantic import BaseModel, Field


class ExperimentCreate(BaseModel):
    name: str
    split: int = Field(default=50, ge=0, le=100)


class ExperimentOut(BaseModel):
    id: int
    name: str
    split: int
