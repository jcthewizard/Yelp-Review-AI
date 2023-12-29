# Contains the logic for interacting with the OpenAI GPT API
import requests
import os

api_key = os.getenv('YELP_API_KEY')
headers = {'Authorization': f'Bearer {api_key}'}
response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers)


def get_restaurant_details(restaurant_id, api_key):
    """Fetch details for a specific restaurant using the Yelp API."""
    url = f"https://api.yelp.com/v3/businesses/{restaurant_id}"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_restaurant_reviews(restaurant_id, api_key):
    """Fetch reviews for a specific restaurant using the Yelp API."""
    url = f"https://api.yelp.com/v3/businesses/{restaurant_id}/reviews"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    api_key = "your_api_key"
    restaurant_id = "example_restaurant_id"
    print(get_restaurant_details(restaurant_id, api_key))
    print(get_restaurant_reviews(restaurant_id, api_key))