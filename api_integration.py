# api_integration.py
import requests

def get_weather(city):
    """Fetch weather data from an API (dummy example using OpenWeatherMap)."""
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"🌤️ The weather in {city} is {data['weather'][0]['description']}."
    else:
        return "❌ Unable to fetch weather data."

def get_joke():
    """Fetch a random joke from JokeAPI."""
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("joke", "No joke found!")
    return "❌ Couldn't fetch a joke."
