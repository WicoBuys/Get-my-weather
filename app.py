from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = '9929843ec76689e6d5798b5c755a58f5'  # Replace with your OpenWeatherMap API key


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = get_weather(city)
    if weather_data:
        return render_template('weather.html', weather=weather_data)
    else:
        error_message = "City not found or API request failed."
        return render_template('index.html', error=error_message)


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)
