from urllib import response
from pip._vendor import requests
import config

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = config.weather_api_key

weather_params = {
    "lat": "47.6062",
    "lon": "-122.3321",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_dict = weather_data["weather"][0]
condition_code = weather_dict["id"]

will_rain = False

if int(condition_code) < 700:
    will_rain = True

if will_rain: 
    print("Bring an umbrella!")
else:
    print("You're staying dry")