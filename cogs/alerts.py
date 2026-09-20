from lxmfy import Command

from modules import mysql_adapter as sql

class AlertsCommands:
    def __init__(self, bot):
        self.bot = bot

    @Command(name="sub", description="Подписаться на уведомления")
    def sub_command(self, ctx):
        sql.sub(ctx.sender, 1)

        ctx.reply("✅ Вы подписаны на уведомления")

    @Command(name="unsub", description="Отписаться от уведомлений")
    def unsub_command(self, ctx):
        sql.sub(ctx.sender, 0)

        ctx.reply("✅ Вы отписаны от уведомлений")

    @Command(name="status", description="Узнать текущий уровень")
    def status_command(self, ctx):
        last = sql.get_last_message()

        if not last:
            ctx.reply("⚠️ Нет сообщений в базе данных")
            return

        ctx.reply(
            f"""
Время: {last["time"]}
{last["text"]}""" # type: ignore
        )
