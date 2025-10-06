from aiogram import Router

from .admin import admin_router
from .command import command_router
from .callback import callback_router
from .user import user_router
from .fsm import fsm_router

main_router = Router()

main_router.include_routers(
    admin_router,
    command_router,
    fsm_router,
    callback_router,
    user_router,
)
