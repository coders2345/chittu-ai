import os

# Function to read the GPT-3 dataset from the file
def read_gpt3_dataset(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(line.strip())
    return data

# Example usage
file_path = "D:\\PycharmProjects\\chittu\\gpt-3-master\\175b_samples.jsonl"  # Replace with the correct file path
try:
    dataset = read_gpt3_dataset(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError as e:
    print(e)
