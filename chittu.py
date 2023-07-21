import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import subprocess
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import requests
from bs4 import BeautifulSoup

# Initialize speech recognizer and engine
r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()

# Set up GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to interact with the GPT-2 model
def interact_with_gpt2(user_input):
    inputs = tokenizer.encode(user_input, return_tensors="pt", add_special_tokens=True)
    attention_mask = inputs.ne(tokenizer.pad_token_id).float()
    with torch.no_grad():
        outputs = model.generate(inputs, attention_mask=attention_mask, max_length=50, num_return_sequences=1)
    ai_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return ai_response

# Function to open files in the specified directory
def open_files(directory_path):
    files = os.listdir(directory_path)
    for file in files:
        speak(f"Opening {file}")
        os.startfile(os.path.join(directory_path, file))

# Function to collect data from the internet using web scraping
def collect_data_from_internet(query):
    url = f"https://www.example.com/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract relevant information from the web page
        # ...
        speak("Here is the data I found.")
    else:
        speak("Sorry, I couldn't fetch the data at the moment.")

# Function to execute voice commands
def execute_command(command, chat_mode=False):
    if not chat_mode:
        if "what is your name" in command:
            speak("My name is Chittu. I was developed by Basha.")
        elif "tell about you" in command:
            speak("I am Chittu, a voice assistant developed by Basha.")
        elif "open YouTube" in command:
            webbrowser.open("https://www.youtube.com")
        elif "open Google" in command:
            webbrowser.open("https://www.google.com")
        elif "what time is it" in command:
            now = datetime.datetime.now()
            speak(f"The time is {now.strftime('%H:%M:%S')}")
        elif "play music" in command:
            music_dir = "C:/Users/User/Music"  # Replace this with your music directory path
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "stop" in command:
            speak("Stopping...")
            exit()
        elif "open calculator" in command:
            calci = r'C:\Windows\System32\calc.exe'
            subprocess.Popen(calci)
        elif "search" in command:
            speak("What do you want me to search for?")
            query = ""

            while not query:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, phrase_time_limit=5)
                    query = r.recognize_google(audio)
                    speak(f"You said: {query}")
                    webbrowser.open(f'https://www.google.com/search?q={query}')
        elif "open files" in command:
            speak("Sure! Which directory should I open?")
            directory_path = ""
            while not directory_path:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, phrase_time_limit=5)
                    directory_path = r.recognize_google(audio)
                    speak(f"Opening files in directory: {directory_path}")
                    open_files(directory_path)
        elif "collect data" in command:
            speak("What do you want to collect data about?")
            query = ""
            while not query:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, phrase_time_limit=5)
                    query = r.recognize_google(audio)
                    speak(f"Collecting data about: {query}")
                    collect_data_from_internet(query)
        elif "chat now" in command:
            speak("Sure! What do you want to chat about?")
            user_input = ""
            while not user_input:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, phrase_time_limit=5)
                    try:
                        user_input = r.recognize_google(audio)
                    except sr.UnknownValueError:
                        speak("Sorry, I didn't catch that. Please try again.")
                        user_input = ""

            ai_response = interact_with_gpt2(user_input)
            speak(f"AI says: {ai_response}")
        else:
            speak("Sorry, I didn't understand that command.")
    else:
        # Execute only GPT-2 chatbot
        if "chat" in command:
            speak("Sure! What do you want to chat about?")
            user_input = ""
            while not user_input:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, phrase_time_limit=5)
                    try:
                        user_input = r.recognize_google(audio)
                    except sr.UnknownValueError:
                        speak("Sorry, I didn't catch that. Please try again.")
                        user_input = ""

            ai_response = interact_with_gpt2(user_input)
            speak(f"AI says: {ai_response}")
        else:
            speak("Sorry, I didn't understand that command.")

# Function to check for the activation phrase "basha"
def check_activation_phrase():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak("Say 'basha' to activate me.")
        audio = r.listen(source, phrase_time_limit=3)

    try:
        activation_phrase = r.recognize_google(audio).lower()
        if "basha" in activation_phrase:
            speak("I'm listening...")
            return True
        else:
            speak("Activation phrase not recognized. Please say 'basha' to activate.")
            return False
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Please say 'basha' to activate.")
        return False
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.")
        return False

# Call the activation function to listen for the activation phrase "basha"
while not check_activation_phrase():
    pass

# Main loop for listening to user commands
chat_mode = False
while True:
    try:
        with sr.Microphone() as source:
            # Adjust the recognizer for ambient noise
            r.adjust_for_ambient_noise(source)
            if not chat_mode:
                speak("Ready for command")
            else:
                speak("Listening for chat input")

            # Listen for user input
            audio = r.listen(source, phrase_time_limit=5)
            # Recognize the speech and convert to text
            command = r.recognize_google(audio).lower()

            # Check if the user says "quit" to end the loop
            if "quit" in command:
                speak("Goodbye!")
                break

            # Check if the user says "basha" to toggle chat mode
            if "basha" in command:
                chat_mode = not chat_mode
                if chat_mode:
                    speak("Chat mode activated. Please say 'basha' again to exit chat mode.")
                else:
                    speak("Chat mode deactivated. How can I help you?")

            # Execute the appropriate command based on the mode
            if chat_mode:
                execute_command(command, chat_mode=True)
            else:
                execute_command(command)

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Please try again.")
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.")
