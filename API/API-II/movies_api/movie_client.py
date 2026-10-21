from api_client import get_json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY not found. Check your .env file.")

headers = {"X-API-Key": API_KEY}

BASE = "http://127.0.0.1:8000"

result = get_json(f"{BASE}/movies")
# print(result)
movie = {"title":"Mental Health", "director":"Quiet Riot", "year": 1986}
result = requests.post(f"{BASE}/movies/", json=movie, headers=headers)


# result = requests.delete(f"{BASE}/movies/1", headers=headers)
print(result)

