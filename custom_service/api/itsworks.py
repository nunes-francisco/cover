from fastapi import APIRouter

router = APIRouter(tags=['Health'])


@router.get('/itsworks')
async def itsworks():
    return "It's works"
