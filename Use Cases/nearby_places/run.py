import csv
from urllib.parse import quote
from urllib.request import urlopen
import json
import us
import requests
import re
from bs4 import BeautifulSoup
import datetime

# Get current date and time
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Specify a keyword to refine results by
google_places_query = "Coffee Shops"
google_places_query = quote(google_places_query)

# Set up the Google Places API key
google_places_api_key = "ENTER YOUR GOOGLE PLACES API KEY"

def get_coordinates(api_key, address):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    if "results" in data and len(data["results"]) > 0:
        lat = data["results"][0]["geometry"]["location"]["lat"]
        lng = data["results"][0]["geometry"]["location"]["lng"]
        return lat, lng
    else:
        raise ValueError(f"Failed to get coordinates for address: {address}")

def find_nearby_places(api_key, lat, lng, radius=500, place_type=None, keyword=None):
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&key={api_key}'
    if place_type:
        url += f'&type={place_type}'
    if keyword:
        url += f'&keyword={keyword}'
    response = requests.get(url)
    data = response.json()
    if "results" in data:
        return data["results"]
    else:
        raise ValueError(f"Failed to find nearby places for coordinates: ({lat}, {lng})")

# OpenAI API endpoint and authentication
api_endpoint = 'https://api.openai.com/v1/completions'
api_key = 'ENTER YOUR OPENAI API KEY'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Get Location Page URLs into an array
with open("urls.txt") as file:
    location_page_urls = file.readlines()

# Use this for debugging. Comment out when ready to run.
location_page_urls = [
    'https://www.adammoro.com/junk/location-pages/1.html',
    'https://www.adammoro.com/junk/location-pages/2.html'
]

# Create a CSV file to store the results
csv_name = 'results/nearby_places_'+timestamp+'.csv'
with open(csv_name, mode='w') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    results_writer.writerow(['location_page_url', 'location_address', 'location_city', 'location_state', 'location_zip', 'nearby_place'])
    # Iterate through the RDPs
    for location_page_url in location_page_urls:
        # Get URL data
        response = requests.get(location_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Match the address pattern on location pages
        address_pattern = r'<p>(.*?)<br/>(.*?), ([A-Z]{2}) (\d{5})<br/>USA</p>'
        match = re.search(address_pattern, str(soup))
        if match:
            street_address, city, state, zip_code = match.groups()
        else:
            street_address, city, state, zip_code = '', '', '', ''

        location_address = street_address.strip()
        location_city = city.strip()
        location_state = state.strip()
        location_zip = zip_code.strip()
        
        # Use the Google Places API to search for nearby locations
        location_full_address = ', '.join([location_address, location_city, location_state, location_zip])
        lat, lng = get_coordinates(google_places_api_key, location_full_address)
        nearby_places = find_nearby_places(google_places_api_key, lat, lng, radius=500, keyword=google_places_query)
        
        # Iterate through each place returned in the response and build response for csv
        for place in nearby_places:
            place_name = place["name"]
            place_address = place["vicinity"]
            # Use GPT-3 to generate a high level summary of the place
            prompt = f"Write a description for {place_name} at {place_address}. "
            prompt += f"First describe who or what {place_name} is, " 
            prompt += "then describe the industry they operate in, "
            prompt += "then find their website address, and "
            prompt += "then describe any products and/or services they offer. \n\n"
            prompt += '''
            Desired format:
            Description: -||-
            Industry: -||-
            Website Address: -||-
            Services & Products: <comma_separated_list_of_services_and_products>
            '''
            # OpenAI API Endpoint Parameters
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
            nearby_place = json_response["choices"][0]["text"]
            nearby_place = nearby_place.strip()+"\nAddress: "+place_address

            # Write the results to the CSV file
            results_writer.writerow([location_page_url, location_address, location_city, location_state, location_zip, nearby_place])

print("Results saved to results.csv file.")
