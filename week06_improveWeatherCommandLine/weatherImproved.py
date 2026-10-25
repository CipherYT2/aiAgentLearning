import requests
import ollama
from geopy.geocoders import Nominatim
import json
import sys


geolocator = Nominatim(user_agent="city_coordinates_app")
mode = input("1. Manually choose city \n2. Choose From favorites \n3. Clear Favorites \nInput:")
if mode == '1':
    city = input("Input your city: ")
    if input("Do you want to add this to favorites? (y/n)") == 'y':
        with open("/Users/OL/agentProjects/aiAgentLearning/week06_improveWeatherCommandLine/favoriteCities.json", 'r', encoding="utf-8") as file:
            add = json.load(file)
            print(add)
        add.append(city)
        with open("/Users/OL/agentProjects/aiAgentLearning/week06_improveWeatherCommandLine/favoriteCities.json", 'w', encoding="utf-8") as file:
            json.dump(add, file)
if mode == '2':
    with open("/Users/OL/agentProjects/aiAgentLearning/week06_improveWeatherCommandLine/favoriteCities.json", 'r', encoding="utf-8") as file:
        fav = json.load(file)
        if len(fav) > 0:
            ct = 0
            print("Your favorites: ")
            for item in fav:
                print(f"{ct}. {item}")
                ct += 1
            chosenFav = int(input("\nChoose Number: "))
            city = fav[chosenFav]
        else:
            print("No favorites found.")
            sys.exit(0)
if mode == '3':
    if input("Confirm deleting all favorites(y/n)").lower() == 'y':
        with open("/Users/OL/agentProjects/aiAgentLearning/week06_improveWeatherCommandLine/favoriteCities.json", 'w', encoding='utf-8') as file:
            json.dump([], file)
            sys.exit(0)


location = geolocator.geocode(city)
if location:
    lat = location.latitude
    lon = location.longitude
else:
    print("Location not found.")
api_key = "4f49f3dfb73a0708d266491fb70ea86c"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

d1temp = data["list"][0]["main"]["temp"]
d1weather = f"{data["list"][0]["weather"][0]["description"]}"

d2temp = data["list"][7]["main"]["temp"]
d2weather = f"{data["list"][7]["weather"][0]["description"]}"

d3temp = data["list"][15]["main"]["temp"]
d3weather = f"{data["list"][15]["weather"][0]["description"]}"

print(f"\nTodays forecast: temp: {round((d1temp - 273.15), 2)}°C \nweather: {d1weather}")
print(f"\nTommorow's forecast: temp: {round((d2temp - 273.15), 2)}°C \nweather: {d2weather}")
print(f"\nThe day after's forecast: temp: {round((d3temp - 273.15), 2)}°C \n weather: {d3weather}\n")

def giveWeatherAdvice(weather):
    stream = ollama.chat(
        model='gemma2',
        messages=[{
            'role': 'user',
            'content': f"Based on the dictionary provided later, provide the tempreture FEELS LIKE (I provided the actual tempreture previously) (their one is in kelvin give it in celcius) for today, tommorow and the next day. Make sure to check the date as each of them is a set time apart. For each day, give a little piece of advice with fun little emojis. The advice should be for clothing, activities or gear to bring. MAKE SURE TO INCLUDE EMOJIS. Here is the data: {data}. DO NOT INCLUDE ANY OTHER TEXT SUCH AS: This json data... etc. GIVE IT IN A HUMAN READABLE FORMAT. Give the day's average unless it will rain or any other bad weather."
        }],
        stream=True
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

giveWeatherAdvice(data)
