from urllib import response
from pip._vendor import requests
from twilio.rest import Client
import config

# Twilio authentication and account information
account_sid = config.twilio_account_sid
auth_token  = config.twilio_api_token
twilio_number = config.my_twilio_number
outgoing_number = config.outgoing_number

# OpenWeatherMap endpoint and authentication
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = config.weather_api_key

# Set up OWM API params dictionary
weather_params = {
    "lat": "47.6062",
    "lon": "-122.3321",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

#Send the API request to OWM
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()

# Parse OWM response for weather condition id
weather_data = response.json()
weather_dict = weather_data["weather"][0]
condition_code = weather_dict["id"]

# Determine rain status
raining = False
rain_message = "It is not raining right now."

if int(condition_code) < 700:
    raining = True
    rain_message = "It is raining, bring an umbrella!"

# Send SMS message through twilio
client = Client(account_sid, auth_token)
message = client.messages.create(
    to=outgoing_number, 
    from_=twilio_number,
    body=rain_message
    )
# Verify SMS message was sent successfully 
print(message.status)