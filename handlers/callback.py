from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from ai_model.ai_dialog import AIDialog
from keyboards.callback_data import ModeratorCallback

callback_router = Router()


@callback_router.callback_query(ModeratorCallback.filter())
async def accept_rework(callback: CallbackQuery, callback_data: ModeratorCallback, bot: Bot, state: FSMContext):
    ai_dialog: AIDialog = await state.get_value('dialog')
    if callback_data.button == 'accept':
        json_data = await ai_dialog.send_message('Да, отправляй переработанный вариант')
        await ai_dialog.answer(bot, state, json_data)
        await callback.answer(
            text='Спасибо, ваша история отправлена!',
            show_alert=True,
        )
    else:
        json_data = await ai_dialog.send_message('Нет, не надо!')
        await ai_dialog.answer(bot, state, json_data)
        await state.clear()
