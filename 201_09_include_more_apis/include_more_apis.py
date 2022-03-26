import requests
from pprint import pprint
import weather
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API = os.getenv("WEATHER_API")

weather_conditions = ["clear sky", "few clouds", "scattered clouds", "broken clouds", "shower rain", "rain", "thunderstorm", "snow", "mist", "overcast clouds", "haze", "universe"]
weather_gifs = [weather.clear_sky, weather.few_clouds, weather.scattered_clouds, weather.broken_clouds, weather.shower_rain, weather.rain, weather.thunderstorm, weather.snow, weather.mist, weather.overcast_clouds, weather.haze, weather.universe]

city_name = input("Enter the city name of the news you want to find: ").lower()

geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=3&appid={WEATHER_API}"

response = requests.get(geo_url)
data = response.json()
lat = data[1]["lat"]
lon = data[1]["lon"]

current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API}"

response = requests.get(current_weather_url)
data = response.json()
current_weather = data["weather"][0]["description"]
temp = data["main"]["temp"]
current_temp = int(temp - 273)
humidity = data["main"]["humidity"]

news_url = f"https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&q={city_name}&language=en"

response = requests.get(news_url) 
data = response.json()

if data["totalResults"] == 0:
    news_title = "There is no related news to this location today."
    news_gist = "Have a great day!"
    news_link = "https://media.giphy.com/media/JRmluCCJv13yEDmEFd/giphy.gif"
else:
    news_title = data["results"][0]["title"]
    news_gist = data["results"][0]["description"]
    news_link = data["results"][0]["link"]

heading = f"Current {city_name.capitalize()} weather: {current_weather}"

for w in weather_conditions: 
    w = current_weather  
    if current_weather not in weather_conditions:
        gif_index = 11
    else:
        gif_index = weather_conditions.index(current_weather)
        
image = weather_gifs[gif_index]   

with open("index.html", "w") as file:
    file.write(f"<div style='text-align:center'><body style='background-color:black'><h1 style='color:#5800FF;'>{heading}</h1>\n<h3 style='color:white'>Temperature is {current_temp}℃</h3>\n<h3 style='color:white'>Humidity is {humidity}%\n</h3><img src={image}>\n<h2 style='color:#E900FF;'>Latest News</h2>\n<h3 style='color:white'>{news_title}</h3>\n<p style='color:white'>{news_gist}</p>\n<a style='color:#FFC600;' href={news_link}>Click Here For Full Description</a></body></div>")



