from pydoc import apropos

from fastapi import APIRouter

from api import rout_task, route_user

api_router = APIRouter()
api_router.include_router(route_user.router, prefix="", tags=["users"])
api_router.include_router(rout_task.router, prefix="", tags=["tasks"])
