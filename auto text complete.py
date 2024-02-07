import time
import pyautogui

def auto_type(question, answer):
    # Give some time to switch to the input field
    time.sleep(5)

    # Type the question
    pyautogui.typewrite(question)

    # Press Enter to submit the question
    pyautogui.press('enter')

    # Give some time for the answer to be generated
    time.sleep(2)

    # Type the answer
    pyautogui.typewrite(answer)

    # Press Enter to submit the answer
    pyautogui.press('enter')

# Example usage
auto_type("What is the capital of France?", "The capital of France is Paris.")
