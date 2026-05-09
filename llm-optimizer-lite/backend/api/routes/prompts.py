from fastapi import APIRouter

from backend.schemas.prompt import PromptCreate, PromptOut, PromptVersionCreate

router = APIRouter(prefix="/prompts", tags=["prompts"])
_PROMPTS: list[PromptOut] = []


@router.get("", response_model=list[PromptOut])
async def list_prompts() -> list[PromptOut]:
    return _PROMPTS


@router.post("", response_model=PromptOut)
async def create_prompt(payload: PromptCreate) -> PromptOut:
    item = PromptOut(id=len(_PROMPTS) + 1, name=payload.name, active_version=1)
    _PROMPTS.append(item)
    return item


@router.post("/{prompt_id}/versions")
async def create_prompt_version(prompt_id: int, payload: PromptVersionCreate) -> dict[str, str | int]:
    return {"prompt_id": prompt_id, "version": payload.version, "status": "created"}
