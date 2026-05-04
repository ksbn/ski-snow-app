import requests

def get_coordinates(resort_name: str):
    """Convert resort name to latitude and longitude."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": resort_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if not data.get("results"):
        return None

    result = data["results"][0]
    return {
        "name": result["name"],
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


def get_snow_conditions(latitude: float, longitude: float):
    """Fetch current weather and snow conditions."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "snowfall",
            "snow_depth",
            "windspeed_10m",
            "weathercode"
        ],
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["current"]


def get_resort_weather(resort_name: str):
    """Main function - get full snow report for a resort."""
    location = get_coordinates(resort_name)
    if not location:
        return None, None

    conditions = get_snow_conditions(location["latitude"], location["longitude"])
    return location, conditions