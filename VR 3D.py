import spotipy
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr

# Set up Spotify API credentials
client_id = 'e727e26f66ce4638ab8bef5cf668506b'
client_secret = '46c4e8907a3242edbbb02cc4170d819f'
redirect_uri = 'http://localhost:8000/callback/'
scope = 'user-modify-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Set up speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

# Listen for voice commands
with mic as source:
    print("Say something!")
    audio = r.listen(source)

# Recognize voice command
try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

# Search for song and play it
results = sp.search(q=text, type='track')
uri = results['tracks']['items'][0]['uri']
sp.start_playback(uris=[uri])
