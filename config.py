import os

class Config:
    API_ID = int(os.getenv("API_ID", 20103040))
    API_HASH = os.getenv("API_HASH", "8c4162dedd5303a8e3fe36257e40d1f6")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7728627887:AAFuVSYKBwVnW0jjcSaXs35k8txIP2HtF6A")
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb+srv://siam420:siam420@cluster0.zcqe3zx.mongodb.net/?retryWrites=true&w=majority")

    # Default user settings
    DEFAULT_SETTINGS = {
        "watermark": True,
        "screenshot": True,
        "demo_video": True,
        "sprite": True,
        "thumbnail": True
    }