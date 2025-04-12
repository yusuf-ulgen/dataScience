import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

API_KEY = os.getenv("API_KEY")
CX = os.getenv("CX_SHOW")

def google_search(word):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": word
    }

    response = requests.get(url, params=params)
    data = response.json()

    for i, item in enumerate(data.get("items", []), 1):
        print(f"{i}. Title: {item['title']}")
        print(f"   Link: {item['link']}")
        print(f"   Explanation: {item.get('snippet', '')}\n")

# Usage :
google_search("Breaking Bad")