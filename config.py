import os

class Config:
    API_ID = int(os.getenv("20103040"))
    API_HASH = os.getenv("8c4162dedd5303a8e3fe36257e40d1f6")
    BOT_TOKEN = os.getenv("7909791290:AAHbaeT9PjUeGdUNPs3FJRZjaUStat28V40")
    MONGODB_URL = os.getenv("mongodb+srv://siam420:siam420@cluster0.ov6coln.mongodb.net/?retryWrites=true&w=majority")