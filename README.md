# chittu-ai-  Personal Assistant with AI Chatbot

This is a Python-based personal assistant with an AI chatbot feature. The assistant can perform various tasks, such as opening files in your system, fetching data from the internet, providing information, playing music, and interacting with you through voice commands.

## Getting Started

### Prerequisites

Before running the code, make sure you have Python installed on your system. You will also need to install the required libraries. You can install them using pip:

```
pip install speech_recognition pyttsx3 transformers torch requests beautifulsoup4
```

### How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the `personal_assistant.py` file using Python:

```
python personal_assistant.py
```

4. The assistant will prompt you to say "basha" to activate it. Say "basha" to start giving voice commands.

5. You can interact with the assistant using the following voice commands:

   - "What is your name?" - To know the name of the assistant.
   - "Tell me about yourself" - To get information about the assistant.
   - "Open YouTube" - To open YouTube in your default web browser.
   - "Open Google" - To open Google in your default web browser.
   - "What time is it?" - To know the current time.
   - "Play music" - To play music from your music directory.
   - "Stop" - To stop the assistant and exit the program.
   - "Open calculator" - To open the system calculator.
   - "Search" - To perform a Google search. The assistant will ask for your query, and then it will search the internet for the information.

6. To chat with the AI chatbot, simply say "chat" when prompted. The assistant will then ask you what you want to chat about. You can have a conversation with the AI chatbot using your voice.

7. To exit the chat mode, say "basha" again, and the assistant will return to regular voice commands mode.

## Note

Please make sure that you have the necessary files in your specified directories, and ensure that you have internet connectivity for data collection from the internet.

The assistant uses GPT-2 model for the AI chatbot, which generates human-like text responses. It may not always provide accurate information and can sometimes generate random responses.

## Disclaimer

This personal assistant and AI chatbot is meant for educational and experimental purposes only. Use it responsibly, and be cautious when running the code with internet data collection capabilities.

## Acknowledgments

The AI chatbot is powered by the GPT-2 model provided by the Hugging Face Transformers library. Special thanks to Hugging Face for their incredible work in NLP and language models.

Feel free to modify and improve this personal assistant according to your needs. Happy coding!
