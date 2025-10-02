from datetime import timedelta

import config

BUTTONS_TEXT = {
    'personal': '🪪 Персональные данные',
    'explicit': '🔞 Нецензурные выражения',
    'ad': '💸 Реклама',
    'politics': '🏢 Политика',
    'religion': '🕌 Религия',
    'criminal_themes': '🧨 Криминал',
    'other': '❌ Прочее',
    'post': '✅ Запостить',
}


class Minutes:
    MINUTES = {
        0: 'минут',
        1: 'минуту',
        2: 'минуты',
        3: 'минуты',
        4: 'минуты',
        5: 'минут',
        6: 'минут',
        7: 'минут',
        8: 'минут',
        9: 'минут',
    }

    @classmethod
    def as_str(cls, minutes: int):
        if minutes:
            if 5 <= minutes < 20:
                return f'{minutes} {cls.MINUTES[5]}'
            else:
                return f'{minutes} {cls.MINUTES[minutes % 10]}'
        return 'меньше минуты'


class ModeratorText:
    SUCCESS = 'Сообщение опубликовано!'
    FAILURE = 'Отказ отправлен!'
    OTHER = 'Укажите причину отказа'
    ANTI_SPAM = 'Извините, но чтобы модератор не сошел с ума, сообщения можно отправлять не чаще одного за ' + \
                str(config.ANTI_SPAM_MINUTES) + ' минут\nОсталось ждать {minutes}'

    @staticmethod
    def as_text(reason: str, message: str):
        return 'В публикации отказано\n' \
               f'Причина: {BUTTONS_TEXT[reason] if reason in BUTTONS_TEXT else reason}\n\n' \
               f'{message[:4000]}\n\n' \
               'Ознакомьтесь с правилами /rules, затем отредактируйте текст и пришлите заново\nСпасибо!'

    @classmethod
    def elapsed_time(cls, e_time: timedelta):
        return cls.ANTI_SPAM.format(
            minutes=Minutes.as_str(config.ANTI_SPAM_MINUTES - int(e_time.total_seconds()) // 60),
        )
