import requests

API_KEY = "149bc69c573f40daaf665535241705"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

city = input("Enter city name: ")

request_url = f"{BASE_URL}?q={city}&key={API_KEY}"

response = requests.get(request_url)

if response.status_code == 200:

    data = response.json()
    weather = data["current"]["condition"]["text"]

    print(weather)

    temperature = data["current"]["temp_c"]
    print(f"Temperature: {temperature}°C")
else:
    print("An error occurred")
