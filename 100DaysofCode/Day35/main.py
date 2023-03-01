import os
import requests
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ["API_KEY"]
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
my_number = os.environ["MY_NUMBER"]

weather_params = {
    "lat": 47.158455,
    "lon": 27.601442,
    "appid": api_key
}

will_rain = False

response = requests.get(OWN_ENDPOINT, params=weather_params)
print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring an ☔", from_=my_number,
                                     to=my_number)
    print(message.status)
