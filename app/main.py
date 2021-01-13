import json, logging
from fastapi import Depends, FastAPI
from app.dependencies import get_query_token, get_token_header
from app.routes import user_login, user_registration , create_post

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(user_login.router)
app.include_router(user_registration.router)
app.include_router(create_post.router)

# logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.DEBUG)


@app.get("/")
async def root():
    return {"message": "Hello Welcome To"}


