import speech_recognition as sr
import pyttsx3
import time
import os

# Create a recognizer object
recognizer = sr.Recognizer()

# Create a microphone object
microphone = sr.Microphone()

# Create a text-to-speech engine
engine = pyttsx3.init()

# Define a function to execute a command
def execute_command(command):
    # Voice Access Control Commands
    if command == "Voice access wake up":
        print("Voice access is awake")
        engine.say("Voice access is awake")
        engine.runAndWait()
    elif command == "Unmute":
        print("Microphone is unmuted")
        engine.say("Microphone is unmuted")
        engine.runAndWait()
    elif command == "Voice access sleep":
        print("Voice access is asleep")
        engine.say("Voice access is asleep")
        engine.runAndWait()
    elif command == "Mute":
        print("Microphone is muted")
        engine.say("Microphone is muted")
        engine.runAndWait()
    elif command == "Turn off microphone":
        print("Microphone is turned off")
        engine.say("Microphone is turned off")
        engine.runAndWait()
    elif command == "Turn off voice access" or command == "Stop voice access" or command == "Close voice access" or command == "Exit voice access" or command == "Quit voice access":
        print("Voice access is closed")
        engine.say("Voice access is closed")
        engine.runAndWait()
        exit()

    # Common Commands
    elif command == "What can I say" or command == "Show all commands" or command == "Show command list" or command == "Show commands":
        display_available_commands()
    elif command == "Open voice access settings":
        open_voice_access_settings()
    elif command == "Open voice access help":
        open_voice_access_help()
    elif command == "Open voice access guide":
        open_voice_access_guide()

    # App Interaction Commands
    elif command.startswith("Open "):
        app_name = command[5:]
        open_app(app_name)
    elif command.startswith("Close "):
        app_name = command[6:]
        close_app(app_name)
    elif command.startswith("Switch to "):
        app_name = command[11:]
        switch_to_app(app_name)
    elif command == "Minimize window":
        minimize_window()
    elif command == "Maximize window":
        maximize_window()
    elif command == "Restore window":
        restore_window()
    elif command == "Show task switcher" or command == "List all windows" or command == "Show all windows":
        show_task_switcher()
    elif command == "Go to desktop" or command == "Go home" or command == "Minimize all windows":
        go_to_desktop()

    # Search Commands
    elif command.startswith("Search on "):
        search_engine, search_term = command[11:].split(" for ")
        search_web(search_engine, search_term)

    # Window Snapping Commands
    elif command.startswith("Snap window to "):
        direction = command[16:]
        snap_window(direction)

    # Other Commands
    else:
        print("Unknown command:", command)
        engine.say("Unknown command: " + command)
        engine.runAndWait()

# Display available commands
def display_available_commands():
    print("Available commands:")
    print("* Voice Access Control Commands:")
    print("  * Voice access wake up")
    print("  * Unmute")
    print("  * Voice access sleep")
    print("  * Mute")
    print("  * Turn off microphone")
    print("  * Turn off voice access")
    print("  * Stop voice access")
    print("  * Close voice access")
    print("  * Exit voice access")
    print("  * Quit voice access")
    print("* Common Commands:")
    print("  * What can I say")
    print("  * Show all commands")
    print("  * Show command list")
    print("  * Show commands")
    print("  * Open voice access settings")
    print("  * Open voice access help")
    print("  * Open voice access guide")
    print("* App")
