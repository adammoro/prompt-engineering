import json
import requests
import csv
from config import settings

# Set OpenAI API key (add key in config.py)
api_key = settings['OPENAI_API_KEY']
# Set API endpoint
if settings['EVAL_TYPE'] == 'completions':
    api_endpoint = settings['OPENAI_API_ENDPOINT_COMPLETIONS']
elif settings['EVAL_TYPE'] == 'chat':
    api_endpoint = settings['OPENAI_API_ENDPOINT_CHAT']
# Set HTTP headers    
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

def get_test_cases(eval_topic): 
    # Open the CSV file
    csv_file_name = f'test_cases/{eval_topic}.csv'
    with open(csv_file_name, 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        # Initialize an empty dictionary
        test_cases = {}     
        # Loop through each row in the CSV file
        for row in csv_reader:
            # Use the first column as the key and the second column as the value
            eval_input = row[0]
            eval_expected_output = row[1]
            # Add the key-value pair to the dictionary
            test_cases[eval_input] = eval_expected_output
    return test_cases

def evaluate_model(test_cases):
    correct_answers = 0
    total_test_cases = len(test_cases)
    
    for input_prompt, expected_output in test_cases.items():
        if settings['EVAL_TYPE'] == 'completions':
            prompt = input_prompt
            data = {
                'model': settings['TEST_MODEL'],
                'prompt': prompt,
                'max_tokens': settings['MAX_TOKENS'],
                'n': settings['N'],
                'stop': settings['STOP'],
                'temperature': settings['TEMPERATURE'],
            }
        elif settings['EVAL_TYPE'] == 'chat':
            messages = input_prompt
            data = {
                'model': settings['TEST_MODEL'],
                'messages': messages,
                'max_tokens': settings['MAX_TOKENS'],
                'n': settings['N'],
                'temperature': settings['TEMPERATURE'],
            }
        else:
            raise ValueError("Invalid EVAL_TYPE in settings. Must be 'completions' or 'chat'.")

        response = requests.post(api_endpoint, headers=headers, json=data)
        response_data = response.json()
        print(response_data)

        if settings['EVAL_TYPE'] == 'completions':
            generated_output = response_data['choices'][0]['text'].strip()
        elif settings['EVAL_TYPE'] == 'chat':
            generated_output = response_data['choices'][0]['message']['content'].strip()

        # Compare the generated output with the expected output
        if generated_output == expected_output:
            correct_answers += 1

    accuracy = (correct_answers / total_test_cases) * 100
    return accuracy

test_cases = get_test_cases(settings['EVAL_TOPIC'])
accuracy = evaluate_model(test_cases)
print(f"{settings['EVAL_TOPIC']} Evaluation Accuracy: {accuracy:.2f}%")

