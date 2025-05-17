import os
import whisper
from moviepy import VideoFileClip
import google.generativeai as genai


# --- Step 1: Download Instagram Reel (if needed) ---
#def download_instagram_video(url, filename="reel.mp4"):
 #   yt = YouTube(url)
  #  stream = yt.streams.filter(file_extension="mp4", only_video=False).first()
   # stream.download(filename=filename)
    #print(f"Downloaded video to {filename}")

# --- Step 2: Extract Audio ---
def extract_audio(video_path, audio_path="audio.wav"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    print(f"Extracted audio to {audio_path}")

# --- Step 3: Transcribe using Whisper ---
def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # You can try 'tiny' for faster results
    result = model.transcribe(audio_path)
    return result['text']

# --- Step 4: Gemini Summary ---
def summarize_with_gemini(transcript, caption, gemini_api_key):
    genai.configure(api_key=gemini_api_key)

    prompt = f"""
You are an AI assistant that analyzes Instagram dance reels to create a detailed contextual summary.

Input:  
- Caption of the reel: "{caption}"  
- Transcript of the reel’s audio: "{transcript}"

Task:  
Generate a clear, detailed, and engaging summary that captures:  
- The overall mood and vibe of the reel (fun, energetic, chill, etc.)  
- Key themes or topics (dance, friendship, celebration, challenge, etc.)  
- Any emotions or attitudes expressed (joy, confidence, excitement, humor)  
- Important keywords, hashtags, or cultural references that set the scene  
- The style and tone of the content (casual, trendy, playful)

This summary will be used by another AI model to understand the context deeply and generate relevant, relatable replies or engagement messages.

Write the summary in 2-4 sentences, keeping it informative and descriptive but concise.
"""


    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# -------------------------
# ✅ USAGE STARTS HERE
# -------------------------

# Set your Gemini API Key
GEMINI_API_KEY = "AIzaSyCuKpvbc731CLaPBtIs1yC2dQk9cLGV1bQ"


# Optional: Download video (skip if already downloaded)
# download_instagram_video("https://youtube.com/your-reel-url", "reel.mp4")

# Extract audio
extract_audio("Video by ycovers [DAtmXFnML5g].mp4", "audio.wav")

# Transcribe
transcript = transcribe_audio("audio.wav")

# Summary from Gemini
caption = """The dress layers were the main character here✨
#dance #explore #trendingreels #kathakdance #foryoupage #bollywood
"""
summary = summarize_with_gemini(transcript, caption, GEMINI_API_KEY)

print("\n🎬 Summary for AI Agent:\n", summary)