import tkinter as tk
import requests

#Put your APY
APY_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    request_url = f"{BASE_URL}?appid={APY_KEY}&q={city}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = round(data["main"]["temp"] - 273.15, 2)
        weather_label.config(text=weather)
        temp_label.config(text=temp)
    else:
        weather_label.config(text="Error")

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter a city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

temp_label = tk.Label(root, text="")
temp_label.pack()

root.mainloop()
