# Manages the interactions with the Yelp API.
import requests
import os
from dotenv import load_dotenv
from gpt_handler import summarize_reviews_with_gpt

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('YELP_API_KEY')
headers = {'Authorization': f'Bearer {api_key}'}
response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers)

# Get Restaurant Details
# def get_restaurant_details(restaurant_id, api_key):
#     """Fetch details for a specific restaurant using the Yelp API."""
#     url = f"https://api.yelp.com/v3/businesses/{restaurant_id}"
#     headers = {'Authorization': f'Bearer {api_key}'}
#     response = requests.get(url, headers=headers)
#     return response.json()

def get_restaurant_reviews(restaurant_id, api_key):
    """Fetch reviews for a specific restaurant using the Yelp API."""
    url = f"https://api.yelp.com/v3/businesses/{restaurant_id}/reviews"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()

# Test the routes
# if __name__ == "__main__":
#     api_key = os.getenv('YELP_API_KEY')
#     restaurant_id = "north-india-restaurant-san-francisco"
#     #print(get_restaurant_details(restaurant_id, api_key))
#     print(get_restaurant_reviews(restaurant_id, api_key))

def extract_review_texts(yelp_response):
    # print(yelp_response)
    reviews = []
    for review in yelp_response['reviews']:
        reviews.append(review['text'])
    return reviews

def concatenate_reviews(review_texts):
    # Join the reviews using a separator (like a newline or period)
    concatenated_reviews = " ".join(review_texts)
    return concatenated_reviews


restaurant_id = "applebees-grill-bar-new-york-3"
# print(extract_review_texts(get_restaurant_reviews(restaurant_id, api_key)))
# Extract review texts
review_texts = extract_review_texts(get_restaurant_reviews(restaurant_id, api_key))

# # Concatenate reviews
concatenated_reviews = concatenate_reviews(review_texts)

# Summarize with GPT API
summary = summarize_reviews_with_gpt(concatenated_reviews)
print(summary)