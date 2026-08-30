from fastapi import FastAPI

from purple_fastapi_hw.posts import routes as posts_routes

app = FastAPI()
app.include_router(posts_routes.router)
