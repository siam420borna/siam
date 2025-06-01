# helper/yt_utils.py

import yt_dlp

async def extract_formats(url: str):
    """
    Extract video/audio formats and metadata from a given URL using yt-dlp.
    Returns a dictionary containing formats, title, thumbnail, duration, etc.
    """
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'format': 'bestvideo+bestaudio/best',
        'forcejson': True,
        'simulate': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info
        except Exception as e:
            return {"error": str(e)}