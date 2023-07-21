import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup

# Set up speech recognition
r = sr.Recognizer()
with sr.Microphone() as source:
    print("What do you want to search?")
    audio = r.listen(source)

# Convert speech to text
try:
    query = r.recognize_google(audio, language='en-US')
    audio("You said: " + query)
except sr.UnknownValueError:
    print("Sorry, I didn't catch that. Please try again.")

# Search Google
url = 'https://www.google.com/search?q=' + query
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

