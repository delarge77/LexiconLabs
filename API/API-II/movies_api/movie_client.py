from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

moviesURL = get_json(f"{BASE}/movies")
# movie = {"title":"Mental Health", "director":"Quiet Riot", "year": 1986}
# result = requests.post(f"{BASE}/movies/", json=movie)


result = requests.delete(f"{BASE}/movies/1")
print(result.status_code)

