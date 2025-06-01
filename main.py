from pyrogram import Client, idle
from config import Config
import logging

logging.basicConfig(level=logging.INFO)

app = Client(
    "video_downloader_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

if __name__ == "__main__":
    from plugins import start, downloader, settings
    logging.info("Bot Started")
    app.run()
    idle()