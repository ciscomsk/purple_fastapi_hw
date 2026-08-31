from fastapi import APIRouter, Depends

from purple_fastapi_hw.posts.schema import PostPath, PostCreateRequest, PostUpdateRequest

router = APIRouter(prefix="/posts")


@router.get("/{post_id}")
def get_post(path: PostPath = Depends()):
    pass


@router.post("/")
async def create_post(data: PostCreateRequest):
    pass


@router.put("/{post_id}")
def update_post(
        data: PostUpdateRequest,
        path: PostPath = Depends()
):
    pass


@router.delete("/{post_id}")
async def delete_post(path: PostPath = Depends()):
    pass
