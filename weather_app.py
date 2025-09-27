import requests

API_KEY = "668a0cc0d493518ff164c54c59cf414e"  # Your OpenWeatherMap API key
BASE_URL = "BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found or API error. Please try again.")

def main():
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("👋 Exiting Weather App")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
