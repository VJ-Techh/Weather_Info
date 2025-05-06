import os
from dotenv import load_dotenv     #To read and use personal information such as API KEY and models
import requests


load_dotenv('weather.env', override = True)
api_key = os.getenv('API_key')        #Reads the API Key from the env file
lat = os.getenv('latitude')           #Reads the Latitude
lon = os.getenv('longitude')          #Reads the Longitude
website_url = "https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=1&lat="
url = f"{website_url}{lat}&lon={lon}&appid={api_key}"     #url for obtaining the weather through the source using this prompt

# you can use instead url = f"https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=1&lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)      #Obttains the information from the url
data = response.json()            #Stores obtained data
print(data)                       #It will give an idea of how data is available and provided through the source


temperature = data['list'][0]['main']['temp']    #Storing just the temperature value
description = data['list'][0]['weather'][0]['description']    #Storing just the description just as sunny\cloudy"
wind_speed = data['list'][0]['wind']['speed']    #Storing the wind speed from the data dict

print(f"Temperature: {temperature}")
print(f"Weather Description: {description}")
print(f"Wind Speed: {wind_speed}")
