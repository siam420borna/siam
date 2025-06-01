# helper/ffmpeg_tools.py

import os
import subprocess
import uuid

TEMP_DIR = "/tmp/video_bot"
os.makedirs(TEMP_DIR, exist_ok=True)

def generate_screenshot(video_path: str, timestamp: str = "00:00:03") -> str:
    output_path = os.path.join(TEMP_DIR, f"screenshot_{uuid.uuid4().hex}.jpg")
    command = [
        "ffmpeg", "-ss", timestamp, "-i", video_path,
        "-frames:v", "1", "-q:v", "2", output_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path if os.path.exists(output_path) else None

def add_watermark(video_path: str, watermark_path: str) -> str:
    output_path = os.path.join(TEMP_DIR, f"wm_{uuid.uuid4().hex}.mp4")
    command = [
        "ffmpeg", "-i", video_path, "-i", watermark_path,
        "-filter_complex", "overlay=10:10", "-c:a", "copy", output_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path if os.path.exists(output_path) else None

def create_demo_clip(video_path: str, duration: int = 15) -> str:
    output_path = os.path.join(TEMP_DIR, f"demo_{uuid.uuid4().hex}.mp4")
    command = [
        "ffmpeg", "-ss", "00:00:00", "-i", video_path,
        "-t", str(duration), "-c:v", "libx264", "-c:a", "aac", output_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path if os.path.exists(output_path) else None

def generate_sprite(video_path: str) -> str:
    output_path = os.path.join(TEMP_DIR, f"sprite_{uuid.uuid4().hex}.jpg")
    command = [
        "ffmpeg", "-i", video_path,
        "-vf", "select='not(mod(n\\,50))',scale=160:-1,tile=5x5",
        "-frames:v", "1", output_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path if os.path.exists(output_path) else None