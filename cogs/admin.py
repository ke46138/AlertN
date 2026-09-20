from lxmfy import Command

from modules import auth
from modules import broadcaster
from modules import mysql_adapter as sql

class AdminCommands:
    def __init__(self, bot):
        self.bot = bot

    @Command(
        name="broadcast",
        description="Принудительно сделать объявление, /silent чтобы не записывать в базу данных",
        admin_only=True,
        threaded=True
    )
    @auth.require_auth
    def broadcast_command(self, ctx):
        if not ctx.args:
            ctx.reply("⚠️ Необходимо указать текст оповещения")
            return

        text = " ".join(ctx.args)
        if not "/silent" in text:
            sql.write_message(text)
        else:
            text = text.replace("/silent", "").strip()

        ctx.reply("⏳ Рассылка в процессе...")

        broadcaster.broadcast(text)

        ctx.reply("✅ Готово")
