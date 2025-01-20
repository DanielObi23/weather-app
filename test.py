#TODO: Add an option to view the entire day list of weathers by clicking on the day forecast or to search for a particular time.


# import requests

# API_KEY = "a3ce1f4be62f4c4daa8195313250801"


# location = input("City Name or postcode: ")
# response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&days=7&alerts=yes")
# weather_data = response.json()


# # THE FOR LOOP data
# # getting the location of retrieved weather data
# city_name = weather_data["location"]["name"]
# city_region = weather_data["location"]["region"]
# country = weather_data["location"]["country"]

# location = f"{city_name}, {city_region}, {country}"

# # current
# forecast = weather_data["forecast"]["forecastday"]

# print("\n\nCity Name: " + city_name)
# for data in forecast:
#     # PART 1: sunrise, sunset and date
#     print(f"\ndate: {data["date"]}\nsunrise: {data["astro"]["sunrise"]}\nsunset: {data["astro"]["sunset"]}\n")

#     # PART 2: temperature, feels_like, windspeed and humidity
#     print(f"condition: {data["day"]["condition"]["text"]}"
#           f"\nimg url: {data["day"]["condition"]["icon"]}"
#           f"\nmax temp: {data["day"]["maxtemp_c"]}℃, min temp: {data["day"]["mintemp_c"]}℃"
#           f"\nhumidity: {data["day"]["avghumidity"]}%, windspeed: {data["day"]["maxwind_kph"]}kph\n\n")

# # print("\n\n", weather_data)






import datetime

def get_day_of_week(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime("%A")

# Example usage:
year = 2025
month = 1
day = 9
day_of_week = get_day_of_week(year, month, day)
print(f"The day of the week for {year}-{month}-{day} is {day_of_week}.")
