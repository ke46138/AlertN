from lxmfy import LXMFBot

from modules import mysql_adapter as sql

bot: LXMFBot = None # type: ignore

def init(temp):
    global bot
    bot = temp

def broadcast(text):
    users = sql.get_subscribed()

    for user in users:
        bot.send(
            user["identity_hash"], # type: ignore
            text
        )
