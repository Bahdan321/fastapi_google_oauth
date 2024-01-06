#from main import oauth

from fastapi import APIRouter
from starlette.requests import Request

# login_router = APIRouter(prefix="/login")


# @login_router.get("/")
# async def login(request: Request):
#     url = request.url_for("auth")
#     return await oauth.google.authorize_redirect(request,url)