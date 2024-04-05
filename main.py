from pytube import YouTube
from sys import argv
import os
import requests

DEFAULT_OUTPUT_PATH = ''

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        print("Title:", yt.title)
        print("Author:", yt.author)
        print("Description:", yt.description)
        
        # Download thumbnail
        thumbnail_url = yt.thumbnail_url
        if thumbnail_url:
            download_thumbnail(thumbnail_url, output_path)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        if stream:
            print("Downloading...")
            stream.download(output_path=output_path)
            print("Download completed successfully.")
        else:
            print("No stream found.")
    except Exception as e:
        print("An error occurred:", str(e))

def download_thumbnail(url, output_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            thumbnail_filename = os.path.join(output_path, "thumbnail.jpg")
            with open(thumbnail_filename, "wb") as f:
                f.write(response.content)
            print("Thumbnail downloaded successfully.")
        else:
            print("Failed to download thumbnail.")
    except Exception as e:
        print("An error occurred while downloading the thumbnail:", str(e))

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python main.py <YouTube_URL>")
    else:
        url = argv[1]
        download_video(url, DEFAULT_OUTPUT_PATH)
