"""Модуль конфигурации"""

from typing import Any

class _Config:
    """Хранилище конфигурации приложения"""

    # Имя бота
    NAME = "AlertN"
    # Включить анонсы
    ANNOUNCE_ENABLED = True
    # Интервал анонсов в секундах
    ANNOUNCE_INTERVAL = 600
    # Identity hash`и админов
    ADMINS = [
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ]
    # Текст при первом сообщении боту
    FIRST_MESSAGE_TEXT = """
Это бот для получения уведомлений о красных уровнях в городе.

Отправьте /sub чтобы подписаться на уведомления
/unsub для отписки
/status чтобы узнать текущий уровень

Github:
https://github.com/ke46138/AlertN
https://github.com/ke46138/BPLA_api"""

    # Включить пропагацию
    PROPAGATION_ENABLED = True
    # Адрес проп ноды
    PROPAGATION_NODE = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # Количество попыток доставить сообщение напрямую
    DIRECT_DELIVERY_RETRIES = 5

    # IP BPLA_api
    GRPC_HOST = "127.0.0.1"
    # Порт BPLA_api
    GRPC_PORT = 8040

    # Учётные данные MySQL
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "reticulum"
    MYSQL_PASSWORD = "password"
    MYSQL_DATABASE = "alerts"

_config = _Config()

def __getattr__(name: str) -> Any:
    """Делегирует доступ к атрибутам конфигурации"""
    return getattr(_config, name)
