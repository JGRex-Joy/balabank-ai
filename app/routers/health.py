from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["health"]
)

@router.get("/", summary="Check API health")
def health():
    return {"status": "ok"}
