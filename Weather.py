import requests
import pycountry
# import json

# from datetime import datetime
import tkinter as tk
API_KEY = "a129bdd138dec45a363d4722a31fd17e"  # Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():

    city = city_entry.get()
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # For Celsius; use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    # print("Status code:", response.status_code)
    # print("Response text:", response.text)

    if response.status_code == 200:
        data = response.json()

        country_data = data["sys"]["country"]
        country = pycountry.countries.get(alpha_2=country_data).name if pycountry.countries.get(
            alpha_2=country_data) else country_data

        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]

        result = (
            f"\nWeather in {data['name']}:\n"
            f"Country: {country}\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {weather_desc.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s\n"
            f"Pressure: {pressure}mmHg\n")

    else:
        result = "City not found or error fetching data."
    result_label.config(text=result)


# Setup Tkinter
window = tk.Tk()
window.title("Weather App")
window.geometry("380x360")

tk.Label(window, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(window)
city_entry.pack(pady=5)

tk.Button(window, text="Get Weather", command=get_weather).pack(pady=5)
result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)

window.mainloop()
