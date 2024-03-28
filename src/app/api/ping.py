from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong():
    # Some async operation could happen here
    # Example: `notes = await get_all_notes()`
    return {"ping": "pong!"}
