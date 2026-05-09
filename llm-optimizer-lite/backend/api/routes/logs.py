from fastapi import APIRouter, Query

from backend.services.request_tracker import list_logs

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("")
async def logs(limit: int = Query(default=100, ge=1, le=1000)) -> list[dict[str, int | float | str]]:
    return list_logs(limit)
