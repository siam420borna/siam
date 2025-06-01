# helper/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

client = AsyncIOMotorClient(Config.MONGODB_URL)
db = client["video_bot"]
settings_col = db["user_settings"]

async def get_settings(user_id: int) -> dict:
    user = await settings_col.find_one({"user_id": user_id})
    if not user:
        default = Config.DEFAULT_SETTINGS.copy()
        default["user_id"] = user_id
        await settings_col.insert_one(default)
        return Config.DEFAULT_SETTINGS.copy()
    return user

async def toggle_setting(user_id: int, key: str) -> bool:
    user = await get_settings(user_id)
    new_value = not user.get(key, True)
    await settings_col.update_one({"user_id": user_id}, {"$set": {key: new_value}})
    return new_value