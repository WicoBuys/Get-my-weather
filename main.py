import requests

api_key = "9929843ec76689e6d5798b5c755a58f5"
location = "Johannesburg,ZA"
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data)
