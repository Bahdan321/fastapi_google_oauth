from config import CLIEN_ID, CLIEN_SECRET

import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

from authlib.integrations.starlette_client import OAuth, OAuthError

from routers import main_api_router


app = FastAPI(
    title="Google OAuth"
)

app.add_middleware(SessionMiddleware, secret_key="add")

app.mount("/static", StaticFiles(directory="static"), name="static")

oauth = OAuth()
oauth.register(
    name = "google",
    server_matadata_url = "https://accounts.google.com/.well-known/openid-configuration",
    client_id = CLIEN_ID,
    client_secret = CLIEN_SECRET,
    client_kwargs ={
        "scope": "email opeid profile",
        "redirect_url": "http://localhost:8000/auth"
        }
)

app.include_router(main_api_router)


template_error = Jinja2Templates(directory="templates/error")
template_welcome = Jinja2Templates(directory="templates/welcome")

@app.get("/login")
async def login(request: Request):
    url = request.url_for("http://127.0.0.1:8000/auth")
    return await oauth.google.authorize_redirect(request,url)

@app.get("/auth")
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return template_error.TemplateResponse(
            name="error.html",
            context={
                "request": request,
                "error": e.error,
                }
        )
        user = token.get("userinfo")
        if user:
            request.session["user"] = dict(user)
        return template_welcome.TemplateResponse(
            name = "welcome.html",
            context = {
                "request": request,
                "user": dict(user),
                }
        )

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
