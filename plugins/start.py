from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_handler(_, message: Message):
    await message.reply_text(
        "👋 Welcome! Send any video/audio/social media link to begin downloading.\nUse /settings to customize your experience."
    )