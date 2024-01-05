

from fastapi import APIRouter#, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request



home_router = APIRouter(prefix="/home", response_class = HTMLResponse)

template = Jinja2Templates(directory="/templates/home")

@home_router.get("/")
async def read_home(req: Request):
    return template.TemplateResponse(
        name="home.html",
        context={"request":req}
    )