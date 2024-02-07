import requests
from datetime import datetime

def get_weather(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()

    current_weather = {}
    current_weather["temperature"] = weather_data["main"]["temp"]
    current_weather["humidity"] = weather_data["main"]["humidity"]
    current_weather["pressure"] = weather_data["main"]["pressure"]

    weather_id = weather_data["weather"][0]["id"]
    weather_description = weather_data["weather"][0]["description"]

    current_weather["weather_description"] = weather_description

    if weather_id >= 200 and weather_id < 300:
        current_weather["weather_condition"] = "гроза"
    elif weather_id >= 300 and weather_id < 400:
        current_weather["weather_condition"] = "морось"
    elif weather_id >= 500 and weather_id < 600:
        current_weather["weather_condition"] = "дождь"
    elif weather_id >= 600 and weather_id < 700:
        current_weather["weather_condition"] = "снег"
    elif weather_id >= 700 and weather_id < 800:
        current_weather["weather_condition"] = "туман"
    elif weather_id == 800:
        current_weather["weather_condition"] = "ясно"
    elif weather_id > 800:
        current_weather["weather_condition"] = "облачно"

    return current_weather

api_key = "8f76020291852cb116ac3b8c3ff5bed7"

def params(api_key, lat, lon):
    weather = get_weather(api_key, lat, lon)
    return [weather['temperature'],weather['humidity'],weather['pressure'],weather['weather_condition']]