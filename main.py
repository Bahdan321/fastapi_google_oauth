from config import CLIEN_ID, CLIEN_SECRET

import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

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
        "redirect_url": "http://localhost:8000/v1/auth"
        }
)

app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
