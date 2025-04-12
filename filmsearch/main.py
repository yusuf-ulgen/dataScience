import requests
import os   
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

API_KEY = os.getenv("API_KEY")
CX = os.getenv("CX_FILM")

def google_search(word, max_results=30):
    url = "https://www.googleapis.com/customsearch/v1"
    all_results = []

    for start in range(1, max_results, 10):  # Google Custom Search API returns 10 results per page
        params = {
            "key": API_KEY,
            "cx": CX,
            "q": word,
            "start": start
        }

        response = requests.get(url, params=params)
        data = response.json()
        items = data.get("items", [])
        all_results.extend(items)

        if not items:  # if no more items are returned, break the loop
            break

    # Sonuçları yazdır
    for i, item in enumerate(all_results, 1):
        print(f"{i}. Title: {item['title']}")
        print(f"   Link: {item['link']}")
        print(f"   Explanation: {item.get('snippet', '')}\n")

# Usage :
google_search("Al Pacino",max_results=30)