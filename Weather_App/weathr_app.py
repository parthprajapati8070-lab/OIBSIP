import requests
from datetime import datetime

print("\n" + "-" * 35)
print("----------- Weather App -----------`")

city_name = input("Enter city name: ")
if city_name.strip() == "":
    print("City name cannot be empty.")
    exit()

api_key = "4d744d2a5fe52a227328a8fcc32f36f1"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)

print(response.status_code)

if response.status_code == 200:

    data = response.json()

    current_time = datetime.now()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    feels_like = data["main"]["feels_like"]
    weather_condition = data["weather"][0]["description"]

    wind_speed = data["wind"]["speed"]
    wind_speed_kmh = wind_speed * 3.6

    print("\n------ Weather Report ------")
    print("City:", city_name.title())
    print("Temperature:", temperature, "°C")
    print("Feels Like:", feels_like, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather_condition.title())
    print("Wind Speed:", round(wind_speed_kmh, 2), "km/h")
    print("-" * 35)

    print("\nWeather Type:")

    if temperature < 10:
        print("Cold")
    elif temperature < 25:
        print("Pleasant")
    elif temperature < 35:
        print("Warm")
    else:
        print("Hot")

    print("\nAdvice:")

    if temperature > 35:
        print("Stay hydrated and avoid direct sunlight.")
    elif temperature < 10:
        print("Wear warm clothes.")
    else:
        print("Weather looks comfortable.")

    print("\nChecked On:",
      current_time.strftime("%d-%m-%Y %H:%M:%S"))

else:
    print("Unable to fetch weather data.")
    print("Check city name or API key.")

