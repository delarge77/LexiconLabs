from api_client import get_json

# 1. City name -> coordinates
city = input("Input city: ")

result = get_json("https://geocoding-api.open-meteo.com/v1/search", params={"name":city, "count":"1"})
print(result)
for city in result["results"]:
    print(city["latitude"], city["longitude"])
    print(city)

# result = get_json("https://api.open-meteo.com/v1/forecast", params={"-23.5475", "-46.63611", "current"="temperature_2m","wind_speed_10m"})
# print(result)

books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 2, "title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 4, "title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]