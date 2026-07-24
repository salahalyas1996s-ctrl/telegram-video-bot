import yt_dlp
import uuid
import os

os.makedirs("downloads", exist_ok=True)

def download_video(url):
    filename = f"downloads/{uuid.uuid4()}.mp4"

    ydl_opts = {
        "format": "best",
        "outtmpl": filename,
        "quiet": True,
        "noplaylist": True,
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return filename
