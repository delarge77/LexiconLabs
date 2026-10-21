from api_client import get_json

def find_city(city: str):
    while True:
        city_results = get_json("https://geocoding-api.open-meteo.com/v1/search", params={"name": city, "count": 1})
        
        results = (city_results.get("results") 
                   if isinstance(city_results, dict)
                   else None
                   )

        if results:
            return (
                results[0]["latitude"],
                results[0]["longitude"]
            )

        city = input("City not found. Please try again: ").strip()

def get_weather(lat, lon):
    return get_json("https://api.open-meteo.com/v1/forecast", params={"latitude":lat, "longitude":lon,
                                                                     "current":["temperature_2m", "wind_speed_10m"]}) 

city = input("Input city: ")
lat, lon = find_city(city)
response = get_weather(lat, lon)
print(f"Temperature: {response['current']['temperature_2m']}{response['current_units']['temperature_2m']}")
