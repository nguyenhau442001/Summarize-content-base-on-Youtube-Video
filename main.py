# Import necessary libraries
import streamlit as st
from pytube import YouTube
from moviepy.editor import AudioFileClip
import speech_recognition as sr

# Title
st.title("YouTube Video to Text Converter")

# Input field for YouTube URL
youtube_url = st.text_input("Enter YouTube URL:")

# Function to download video, extract audio, and convert to text
def process_video(url):
    # Download video
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    stream.download(filename="temp_audio")

    # Extract audio
    audio_clip = AudioFileClip("temp_audio.mp4")
    audio_clip.write_audiofile("temp_audio.wav")

    # Convert audio to text
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp_audio.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    return text

# Check if URL is provided and process the video
if youtube_url:
    st.write("Processing video...")
    try:
        video_text = process_video(youtube_url)
        st.write("Transcribed text:")
        st.write(video_text)
    except Exception as e:
        st.write("Error processing the video:", e)
