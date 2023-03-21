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

# Set Product Name
# Options: Product Name 1, Product Name 2, Product Name 3
product_name = "Product Name 2"

# API endpoint and authentication
api_endpoint = 'https://api.openai.com/v1/completions'
api_key = 'OPENAI API KEY HERE'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

csv_name = 'results/intros_by_state_'+timestamp+'.csv'

# Create a CSV file to store the results
with open(csv_name, mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['State', 'Product Name', 'Current Intro Text', 'New Intro Text'])
    states = us.states.STATES
    # Iterate through the states
    for state in states:                
        # Prepare Intro Text & Training Data
        if product_name is "Product Name 1":
            current_intro_text = f"This is some intro text currently being used on the website for pages about Product Name 1. "
            training_data = "This some copy related to Product Name 1 that I pulled in from the website using the [Text:] directive."
        elif product_name is "Product Name 2":
            current_intro_text = f"This is some intro text currently being used on the website for pages about Product Name 2. "
            training_data = "This some copy related to Product Name 2 that I pulled in from the website using the [Text:] directive."
        elif product_name is "Product Name 3":
            current_intro_text = f"This is some intro text currently being used on the website for pages about Product Name 3. "
            training_data = "This some copy related to Product Name 3 that I pulled in from the website using the [Text:] directive."
        else:
            print("You must specify an Product Name.")
            break

        # Use GPT-3 to generate unique intro text based on current intro text and provided training data
        prompt = f"Here's some ad copy from the website about the {product_name} program: \n"
        prompt += training_data + "\n\n"
        prompt += f"Please rewrite the following intro text in the style of the above ad copy. \n"
        prompt += f"Write it to speak to someone who lives in {state}. \n"
        prompt += f"[Text: {current_intro_text}]"
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
        new_intro_text = json_response["choices"][0]["text"]
        new_intro_text = unicodedata.normalize("NFKD", new_intro_text)
        new_intro_text = new_intro_text.strip()

        # Write the results to the CSV file
        results_writer.writerow([state, product_name, current_intro_text, new_intro_text])

print("Results saved to results.csv file.")

