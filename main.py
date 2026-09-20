import threading

from lxmfy import LXMFBot

from cogs import admin, alerts

from modules import broadcaster
from modules import grpc_worker
from modules.logger import logger

import config

bot = LXMFBot(
    name=config.NAME,
    announce=config.ANNOUNCE_INTERVAL,
    announce_immediately=True,
    admins=config.ADMINS,
    hot_reloading=False,
    rate_limit=5,
    cooldown=10,
    max_warnings=3,
    warning_timeout=300,
    command_prefix="/",
    cogs_dir="cogs",
    cogs_enabled=True,
    permissions_enabled=False,
    storage_type="json",
    storage_path="data",
    first_message_enabled=True,
    event_logging_enabled=True,
    max_logged_events=1000,
    event_middleware_enabled=True,
    announce_enabled=config.ANNOUNCE_ENABLED,
    autopeer_propagation=False,
    direct_delivery_retries=config.DIRECT_DELIVERY_RETRIES,
    propagation_fallback_enabled=config.PROPAGATION_ENABLED
)

if config.PROPAGATION_ENABLED:
    bot.set_propagation_node(config.PROPAGATION_NODE)

broadcaster.init(bot)

admin_cog = admin.AdminCommands(bot)
alerts_cog = alerts.AlertsCommands(bot)

@bot.on_first_message()
def first_message(sender, message):
    bot.send(
        sender,
        config.FIRST_MESSAGE_TEXT
    )

@bot.command(name="ping", description="Проверка доступности бота")
def ping_command(ctx):
    ctx.reply("Pong!")

bot.add_cog(admin_cog)
bot.add_cog(alerts_cog)

if __name__ == "__main__":
    grpc_thread = threading.Thread(target=grpc_worker.grpc_worker, daemon=True)
    grpc_thread.start()
    try:
        logger.info("Запущен бот с именем %s", config.NAME)
        bot.run()
    except KeyboardInterrupt:
        bot.cleanup()
