# Contains the logic for interacting with the OpenAI GPT API
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def summarize_reviews_with_gpt(concatenated_reviews):
    prompt = f"Please summarize the following restaurant reviews: {concatenated_reviews} please outline the things that customers seem to enjoy and dislike. please try to touch on the subjects of ambiance, price, location, taste if possible. Also try to highlight dishes that were favorites if possible."

    try:
        response = openai.Completion.create(
            engine="davinci",  # Replace with the latest model name
            prompt=prompt,
            # max_tokens=1000  # Adjust as needed
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

