import requests
import ollama
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="city_coordinates_app")

city = input("Input your city: ")
location = geolocator.geocode(city)
if location:
    lat = location.latitude
    lon = location.longitude
else:
    print("Location not found.")
api_key = "4f49f3dfb73a0708d266491fb70ea86c"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

temp = data["main"]["temp"]
weather = f"{data["weather"][0]["main"]}, {data["weather"][0]["description"]}"

print(f"\ntemp: {temp} \nweather: {weather}")

def giveWeatherAdvice(weather):
    stream = ollama.chat(
        model='gemma2',
        messages=[{
            'role': 'user',
            'content': f'Based on the weather provided that is in a dictionary form, give advice in a fun way however keep it short no more than 10 words but keep it fun and kind with emojis e.g. if it is raining: Take an umbrella ☔. Here is the data: {data}'
        }],
        stream=True
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

giveWeatherAdvice(data)
