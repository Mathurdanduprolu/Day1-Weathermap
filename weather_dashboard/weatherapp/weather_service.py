import requests
from django.conf import settings

def get_weather_data(city):
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return {"error": "City not found"}
        else:
            return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}
