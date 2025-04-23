from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests
import pycountry

from kivy.lang import Builder  # 👈 Add this


API_KEY = "a129bdd138dec45a363d4722a31fd17e"  # Replace with your API key


class WeatherLayout(BoxLayout):
    def get_weather(self):
        city = self.ids.city_input.text
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": API_KEY, "units": "metric"}

        try:
            r = requests.get(url, params=params)
            if r.status_code == 200:
                data = r.json()
                country_code = data["sys"]["country"]
                country = pycountry.countries.get(alpha_2=country_code)
                country_name = country.name if country else country_code

                desc = data['weather'][0]['description'].capitalize()
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                wind = data['wind']['speed']

                result = (
                    f"{data['name']}, {country_name}\n"
                    f"{desc}, {temp}°C\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind: {wind} m/s"
                )
            else:
                result = "City not found."
        except Exception as e:
            result = f"Error: {e}"

        self.ids.result_label.text = result


class WeatherApp(App):
    def build(self):
        Builder.load_file("weather.kv")  # 👈 This loads the .kv file manually
        print("App is building...")
        return WeatherLayout()
