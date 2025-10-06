from datetime import datetime, timedelta

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.enums import ChatAction

from ai_model.ai_dialog import AIDialog
from ai_model import ai_client
from ai_model.enums import GPTRole
import config
from fsm.states import UserDialog
from keyboards.inline_keyboards import ikb_moderator_menu
from text.moderator_text import ModeratorText

fsm_router = Router()


# @fsm_router.message(UserDialog.timer)
# async def check_spam(message: Message, bot: Bot, state: FSMContext):
#     current_time = datetime.now()
#     state_data = await state.get_data()
#     elapsed_time = current_time - state_data['last_message']
#     if state_data['attempts'] >= config.ANTI_SPAM_ATTEMPTS:
#         pass
#     if elapsed_time < timedelta(minutes=config.ANTI_SPAM_MINUTES):
#         await message.answer(
#             text=ModeratorText.elapsed_time(elapsed_time),
#         )
#     else:
#         await bot.send_message(
#             chat_id=config.MODERATOR_ID,
#             text=message.text,
#             entities=message.entities,
#             reply_markup=ikb_moderator_menu(message.from_user.id),
#         )
#         await state.set_state(UserDialog.timer)
#         await state.set_data(
#             {
#                 'message_time': datetime.now(),
#             },
#         )


@fsm_router.message(UserDialog.input_data)
async def user_dialog(message: Message, bot: Bot, state: FSMContext):
    ai_dialog: AIDialog = await state.get_value('dialog')
    print(*ai_dialog.message_list, sep='\n')
    # message_list = data['message_list']
    # await bot.send_chat_action(
    #     chat_id=message.from_user.id,
    #     action=ChatAction.TYPING,
    # )
    # response = await ai_client.request(GPTRole.USER, message.text, message_list)
    # message_list.update(GPTRole.CHAT, response)
    # print(response)
    # if response.startswith('Correct') or response.startswith('Incorrect'):
    #     result, response = response.split(':', 1)
    #     await state.set_state(UserDialog.input_data)
    #     await state.update_data(
    #         {
    #             'messages': message_list,
    #             'attempts': data['attempts'] + 1,
    #         },
    #     )
    #     if result == 'Correct':
    #         await bot.send_message(
    #             chat_id=config.CHANNEL_ID,
    #             text=message.text,
    #         )
    #         await state.clear()
    # await message.answer(
    #     text=response.strip().capitalize(),
    # )
