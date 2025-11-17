Generate Instagram Video Summary

This tool takes any Instagram video, extracts its audio, converts the speech to text using Whisper, and then generates a meaningful summary using Google Generative AI.
It’s a quick way to understand long videos without watching them end-to-end.

✨ Features

Extracts audio from Instagram videos

Converts speech to text with Whisper

Uses Google Generative AI to produce clean summaries

Supports most video formats

Fully automated pipeline

🧰 Tech Stack

Python

OpenAI Whisper – speech-to-text transcription

MoviePy – video/audio processing

Google Generative AI – summary generation

OS module – handling paths and file operations

📦 Installation

Make sure you have Python 3.8+ installed.

git clone https://github.com/Iamyashjain/Generate_Insta_Video_summary
cd Generate_Insta_Video_summary


Install dependencies:

pip install -r requirements.txt


Required packages include:

whisper

moviepy

google-generativeai

ffmpeg (system-level dependency)

Install FFmpeg (if not already installed):

Windows

Download from https://ffmpeg.org/download.html
 and add to PATH.

Linux
sudo apt install ffmpeg

macOS
brew install ffmpeg

⚙️ How It Works

The script loads the Instagram video from your filesystem.

MoviePy extracts the audio.

Whisper transcribes the audio into text.

Google Generative AI processes the transcription and produces a summary.

The summary is saved or printed.

▶️ Usage
import os
import whisper
from moviepy import VideoFileClip
import google.generativeai as genai

# Load your video here
video = VideoFileClip("your_video.mp4")

# Extract audio logic...
# Whisper transcription...
# Summary generation...


After running the script, you’ll get a clean summary of the video content.

📁 Project Structure
├── main.py
├── requirements.txt
├── README.md
└── output/
    ├── audio.wav
    └── summary.txt

🚀 Future Improvements

Direct Instagram URL scraping

UI dashboard for uploading videos

Multi-language support

🤝 Contributing

Pull requests are welcome. Feel free to suggest enhancements!

📜 License

MIT License.
