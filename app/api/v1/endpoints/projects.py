from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_projects():
    return [{"name": "Lava Terrain"}, {"name": "Winter Snow Terrain"}]
