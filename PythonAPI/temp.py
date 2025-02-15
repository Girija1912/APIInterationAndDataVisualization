import requests
import json
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MY_API_KEY")

# OpenWeatherMap API Key (Replace with your own key)
# API_KEY = "97b60aa829df943eb186b83a42a4fb12"
CITY = input("Enter a name of city: ")
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response=requests.get(URL)
data=response.json()
D={
         "Temperature (°C)": data["main"]["temp"],
         "Feels Like (°C)": data["main"]["feels_like"],
         "Humidity (%)": data["main"]["humidity"],
         "Pressure (hPa)": data["main"]["pressure"],
         "Wind Speed (m/s)": data["wind"]["speed"],
}          
Weather_Condition=data["weather"][0]["description"].capitalize()

labels = list(D.keys())  # Exclude "Weather Condition"
values = list(D.values())
plt.figure(figsize=(10, 5))
plt.bar(labels, values, color=["blue", "red", "green", "orange", "purple"])
plt.xlabel("Weather Parameters")
plt.ylabel("Values")
plt.title(f"Current Weather in {CITY} ")

plt.xticks(rotation=2)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
