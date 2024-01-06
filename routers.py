from fastapi import APIRouter
from view.home.homeRouter import home_router
#from view.auth.authRouter import auth_router
#from view.login.loginRouter import login_router

#main_api_router = APIRouter(prefix='/v1')
main_api_router = APIRouter()


main_api_router.include_router(home_router)
#main_api_router.include_router(auth_router)
#main_api_router.include_router(login_router)

