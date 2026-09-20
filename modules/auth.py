"""Модуль для авторизации пользователей"""

from functools import wraps
import random

import config

error_messages = [
    "⚠️ Команда недоступна. Попробуйте подкупить админа печеньками"
]

def authorize(ctx):
    """Функция авторизации пользователей для использования админских функций.
    Не обрабатывает исключения.
    Возвращает:
    1 - всё ок
    0 - доступ запрещён"""

    if ctx.is_admin:
        return 1

    return 0

def randomise_errors():
    return random.choice(error_messages)

def require_auth(func=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            ctx = kwargs.get('ctx') or (args[1] if args else None)

            if not ctx:
                raise ValueError("ctx не найден в аргументах!")

            if not authorize(ctx):
                ctx.reply(randomise_errors())
                return None

            return f(*args, **kwargs)

        return wrapper

    if func is not None:
        return decorator(func)

    return decorator
