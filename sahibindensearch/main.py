import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını yükle

API_KEY = os.getenv("API_KEY")
CX = os.getenv("CX_SAHIBINDEN")

def google_search(kategori, yil, fiyat, renk, konum):
    # Sorguyu oluştur
    query = f"{kategori} {yil} {fiyat} {renk} {konum}"

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query
    }

    response = requests.get(url, params=params)
    data = response.json()

    for i, item in enumerate(data.get("items", []), 1):
        print(f"{i}. Başlık: {item['title']}")
        print(f"   Link: {item['link']}")
        print(f"   Açıklama: {item.get('snippet', '')}\n")

# Örnek kullanım:
google_search("otomobil", "2020", "500000", "kırmızı", "ankara keçiören")
