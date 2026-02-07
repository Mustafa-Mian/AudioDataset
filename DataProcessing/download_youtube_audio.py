#!/usr/bin/env python3
"""
Downloads audio from a YouTube video and saves it as an MP3 file.

Usage:
    python download_youtube_audio.py "<YouTube URL>"
    
Example:
    python download_youtube_audio.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
"""

import sys
import os
import subprocess


def download_audio(youtube_url, output_path="downloaded_audio"):
    """
    Download audio from a YouTube video.
    
    Args:
        youtube_url: The URL of the YouTube video
        output_path: Directory to save the audio file (default: downloaded_audio)
    """
    
    os.makedirs(output_path, exist_ok=True)
    
    # -x: extract audio
    # --audio-format mp3: convert to mp3
    # -o: output template with title
    # --js-runtimes deno: use Deno for JavaScript extraction (required for YouTube)
    command = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "--js-runtimes", "deno",
        "-o", f"{output_path}/%(title)s.%(ext)s",
        youtube_url
    ]
    
    try:
        print(f"Downloading audio from: {youtube_url}")
        print(f"Saving to: {output_path}/")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("✓ Download completed successfully!")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during download: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: yt-dlp is not installed.")
        print("Install it with: pip install yt-dlp")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_youtube_audio.py '<YouTube URL>' [output_directory]")
        print("Example: python download_youtube_audio.py 'https://www.youtube.com/watch?v=...'")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "downloaded_audio"
    
    download_audio(youtube_url, output_directory)
