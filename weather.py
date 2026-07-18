import requests

# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("=" * 40)
print("🌤️      WEATHER API APPLICATION")
print("=" * 40)

city = input("Enter city name: ").strip()

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("\n========== WEATHER REPORT ==========")
    print(f"📍 City        : {data['name']}, {data['sys']['country']}")
    print(f"🌡 Temperature : {data['main']['temp']} °C")
    print(f"🤗 Feels Like  : {data['main']['feels_like']} °C")
    print(f"💧 Humidity    : {data['main']['humidity']}%")
    print(f"🌬 Wind Speed  : {data['wind']['speed']} m/s")
    print(f"☁ Weather      : {data['weather'][0]['description'].title()}")
    print(f"🔽 Pressure    : {data['main']['pressure']} hPa")
    print("=" * 40)

except requests.exceptions.HTTPError:
    if response.status_code == 404:
        print("❌ City not found.")
    elif response.status_code == 401:
        print("❌ Invalid API key.")
    else:
        print(f"❌ Error: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("❌ No internet connection.")

except requests.exceptions.Timeout:
    print("❌ Request timed out.")

except Exception as e:
    print("❌ Something went wrong.")
    print(e)
