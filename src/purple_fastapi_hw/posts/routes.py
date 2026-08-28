from fastapi import APIRouter, Request

router = APIRouter(prefix="/posts")


@router.get("/{post_id}")
def get_post(post_id: int):
    pass


@router.post("/")
async def create_post(request: Request):
    pass


@router.put("/")
async def update_post(request: Request):
    pass


@router.delete("/")
async def delete_post(request: Request):
    pass
