from main import oauth, OAuthError

from fastapi import APIRouter
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

auth_router = APIRouter(prefix="/auth")

template = Jinja2Templates(directory="templates/error")


@auth_router.get("/")
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return template.TemplateResponse(
            name="error.html",
            context={
                "request": request,
                "error": e.error,
                }
        )
        user = token.get("userinfo")
        if user:
            request.session["user"] = dict(user)
        return 
