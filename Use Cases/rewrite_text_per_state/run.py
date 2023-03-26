import csv
from urllib.parse import quote
from urllib.request import urlopen
import json
import us
import requests
import unicodedata
import datetime

# Get current date and time
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# API endpoint and authentication
api_endpoint = 'https://api.openai.com/v1/completions'
api_key = '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'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Set the name of the CSV file
csv_name = 'results/rewrite_text_per_state_'+timestamp+'.csv'

# Create a CSV file to store the results
with open(csv_name, mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['State', 'Source Text', 'AI Rewritten Text'])
    states = us.states.STATES
    # Iterate through the states
    for state in states:                
        # Add Source Text (source_text) & Training Data (training_data)
        # The Source Text will be rewritten using the provided Training Data
        source_text = f"This is the text we want to rewrite with AI."
        # The Training Data can be anything that faciliates a better prompt response
        training_data = "Add additional context you want to provide the AI."
        # Build the prompt 
        prompt = f"Apply the following info to your response: \n"
        prompt += training_data + "\n\n"
        prompt += f"Rewrite the following text in the style of someone from {state}: \n"
        prompt += f"[Text: {source_text}]"
        data = {
            'model': 'text-davinci-003',
            'prompt': prompt,
            'temperature': 0.9,
            'max_tokens': 250,
            'frequency_penalty': 0,
            'presence_penalty': 0.6
        }
        data = json.dumps(data).encode()
        response = requests.post(api_endpoint, data=data, headers=headers)
        json_response = response.json()
        new_text = json_response["choices"][0]["text"]
        new_text = unicodedata.normalize("NFKD", new_text)
        new_text = new_text.strip()

        # Write the results to the CSV file
        results_writer.writerow([state, source_text, new_text])

print("Results saved to results.csv file.")

