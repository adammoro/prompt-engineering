import csv
from urllib.parse import quote
from urllib.request import urlopen
import json
from datetime import datetime
import requests
import re
from bs4 import BeautifulSoup
from dict import location_page_urls

# Constants
GOOGLE_PLACES_QUERY = "Coffee Shops"
GOOGLE_PLACES_API_KEY = "YOUR_GOOGLE_PLACES_API_KEY"
OPENAI_API_ENDPOINT = 'https://api.openai.com/v1/completions'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
# Location Page URLs to Check for Address in dict.py

def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")

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

def get_location_data(location_page_url):
    response = requests.get(location_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    address_pattern = r'<p>(.*?)<br/>(.*?), ([A-Z]{2}) (\d{5})<br/>USA</p>'
    match = re.search(address_pattern, str(soup))
    if match:
        street_address, city, state, zip_code = match.groups()
    else:
        street_address, city, state, zip_code = '', '', '', ''
    return street_address.strip(), city.strip(), state.strip(), zip_code.strip()

def fetch_openai_description(api_endpoint, api_key, headers, place_name, place_address):
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
    return nearby_place.strip() + "\nAddress: " + place_address

def main():
    google_places_query = quote(GOOGLE_PLACES_QUERY)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    csv_name = f'results/nearby_places_{get_timestamp()}.csv'
    with open(csv_name, mode='w') as results_file:
        results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        results_writer.writerow(['location_page_url', 'location_address', 'location_city', 'location_state', 'location_zip', 'nearby_place'])
        
        for location_page_url in location_page_urls:
            location_address, location_city, location_state, location_zip = get_location_data(location_page_url)
            location_full_address = ', '.join([location_address, location_city, location_state, location_zip])
            lat, lng = get_coordinates(GOOGLE_PLACES_API_KEY, location_full_address)
            nearby_places = find_nearby_places(GOOGLE_PLACES_API_KEY, lat, lng, radius=500, keyword=google_places_query)
            
            for place in nearby_places:
                place_name = place["name"]
                place_address = place["vicinity"]
                nearby_place = fetch_openai_description(OPENAI_API_ENDPOINT, OPENAI_API_KEY, headers, place_name, place_address)

                results_writer.writerow([location_page_url, location_address, location_city, location_state, location_zip, nearby_place])

    print("Results saved to csv file.")

if __name__ == "__main__":
    main()



