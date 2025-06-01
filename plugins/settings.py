from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from helper.database import get_settings, toggle_setting

async def settings(_, message: Message):
    user_id = message.from_user.id
    settings = await get_settings(user_id)

    buttons = [
        [InlineKeyboardButton(f"Watermark: {'✅' if settings['watermark'] else '❌'}", callback_data="toggle_watermark")],
        [InlineKeyboardButton(f"Screenshot: {'✅' if settings['screenshot'] else '❌'}", callback_data="toggle_screenshot")],
        [InlineKeyboardButton(f"Demo Video: {'✅' if settings['demo_video'] else '❌'}", callback_data="toggle_demo_video")],
        [InlineKeyboardButton(f"Sprite: {'✅' if settings['sprite'] else '❌'}", callback_data="toggle_sprite")],
        [InlineKeyboardButton(f"Thumbnail: {'✅' if settings['thumbnail'] else '❌'}", callback_data="toggle_thumbnail")],
    ]

    await message.reply("⚙️ Your current settings:", reply_markup=InlineKeyboardMarkup(buttons))

async def on_callback(_, callback_query):
    user_id = callback_query.from_user.id
    setting_key = callback_query.data.replace("toggle_", "")
    status = await toggle_setting(user_id, setting_key)
    await callback_query.answer(f"{setting_key.replace('_', ' ').title()} set to {'ON' if status else 'OFF'}", show_alert=True)
    await settings(_, callback_query.message)

settings_handler = MessageHandler(settings, filters.command("settings"))
settings_callback = CallbackQueryHandler(on_callback, filters.regex("toggle_"))