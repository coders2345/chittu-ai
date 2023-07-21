import google.auth
from googleapiclient.discovery import build
from youtube_player import play_video
import speech_recognition as sr

# Set up YouTube API credentials
api_key = "AIzaSyBPqY04WEbQ4xwjkdcbvTjUuWx4ywiX64c")

# Set up YouTube API client
service = build('youtube', 'v3', developerKey="AIzaSyBPqY04WEbQ4xwjkdcbvTjUuWx4ywiX64c")

# Set up speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

# Listen for voice commands
with mic as source:
    speak("Say something!")
    audio = r.listen(source)

# Recognize voice command
try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

# Search for video and play it
request = service.search().list(q=text, part='id', type='video')
response = request.execute()
video_id = response['items'][0]['id']['videoId']
play_video(video_id)
