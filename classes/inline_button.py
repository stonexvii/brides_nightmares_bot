from keyboards.callback_data import ModeratorCallback


class Button:

    def __init__(self, text: str, callback: str, user_tg_id: int):
        self.text = text
        self.callback = ModeratorCallback(
            button=callback,
            user_tg_id=user_tg_id
        )

    def as_kwargs(self):
        return {
            'text': self.text,
            'callback_data': self.callback,
        }
