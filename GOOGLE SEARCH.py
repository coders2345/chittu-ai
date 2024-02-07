from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import re

file_path = "D:\\PycharmProjects\\chittu\\gpt-3-master\\175b_samples.jsonl"
# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")


# Read the GPT-3 dataset from the file
def read_gpt3_dataset(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(line.strip())
    return data


# Choose a random sample from the dataset for generation
def choose_random_sample(dataset):
    import random
    return random.choice(dataset)


# Function for text generation based on user input
def generate_text(user_input, max_length=50):
    input_ids = tokenizer.encode(user_input, return_tensors="pt", add_special_tokens=True)
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text


# Reinforcement learning reward function
def calculate_reward(expected_response, generated_response):
    # Simple rule-based reward: +1 for matching response, -1 otherwise
    return 1 if expected_response == generated_response else -1


# Function to evaluate math expressions
def evaluate_math_expression(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid math expression."


if __name__ == "__main__":
    # Replace with your actual file path to the GPT-3 dataset
    file_path = "D:\\PycharmProjects\\chittu\\gpt-3-master\\175b_samples.jsonl"
    dataset = read_gpt3_dataset(file_path)

    print("Welcome! How can I assist you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "stop"]:
            print("Goodbye!")
            break

        # Check if the user input is a math expression
        if re.match(r"^[0-9+\-*/()\s]+$", user_input):
            result = evaluate_math_expression(user_input)
            print("Result:", result)
        else:
            # Text Generation
            generated_text = generate_text(user_input)
            print("Generated Text:", generated_text)

            # Reinforcement Learning
            expected_response = input("Expected Response: ")
            reward = calculate_reward(expected_response, generated_text)
            print("Reward:", reward)

            # Creative Writing
            random_sample = choose_random_sample(dataset)
            print("Random Sample from GPT-3 Dataset:", random_sample)

            # Content Generation for Chatbots
            # You can integrate the 'generated_text' into your chatbot's response
