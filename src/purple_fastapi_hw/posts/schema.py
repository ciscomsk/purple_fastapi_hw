from pydantic import BaseModel


class PostCreateRequest(BaseModel):
    content: str

class PostPath(BaseModel):
    post_id: int