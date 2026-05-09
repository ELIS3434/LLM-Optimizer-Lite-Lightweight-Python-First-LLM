from fastapi import APIRouter

from backend.schemas.experiment import ExperimentCreate, ExperimentOut

router = APIRouter(prefix="/experiments", tags=["experiments"])
_EXPERIMENTS: list[ExperimentOut] = []


@router.get("", response_model=list[ExperimentOut])
async def list_experiments() -> list[ExperimentOut]:
    return _EXPERIMENTS


@router.post("", response_model=ExperimentOut)
async def create_experiment(payload: ExperimentCreate) -> ExperimentOut:
    item = ExperimentOut(id=len(_EXPERIMENTS) + 1, name=payload.name, split=payload.split)
    _EXPERIMENTS.append(item)
    return item
