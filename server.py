from flask import render_template, Flask, request
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if request.method == 'POST':
        location = request.form.get('location').title()
        response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&days=7&alerts=yes")      
        weather_data = response.json()

        try:
            forecast = weather_data["forecast"]["forecastday"]
        except:
            error_message = f"{location} is not an available city or postcode in the database, please try again. "
            return render_template('index.html', error=error_message, location=location)
        
        city_name = weather_data["location"]["name"]
        city_region = weather_data["location"]["region"]
        country = weather_data["location"]["country"]
        location = f"{city_name}, {city_region}, {country}"

        def weekday(date):
            date_object = datetime.strptime(date, "%Y-%m-%d")
            day_of_week = date_object.strftime("%A")
            return day_of_week
        return render_template("index.html", location=location, forecast_data=forecast, weekday=weekday)


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)