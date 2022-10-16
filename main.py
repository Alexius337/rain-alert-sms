from urllib import response
from pip._vendor import requests
import config

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = config.api_key

weather_params = {
    "lat": "47.6062",
    "lon": "-122.3321",
    "appid": api_key
}

response = requests.get(OWM_endpoint, params=weather_params)
print(response.status_code)