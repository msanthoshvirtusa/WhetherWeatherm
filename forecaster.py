# Import request and os packages
import os
import requests

# import logger from logger.py
from logger import logger

# import API_KEY from .env file
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv("API_KEY")

# function that takes in the city name and returns the weather forecast using the openweathermap API


def forecast(city: str) -> list:
    # url for the API
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(
        city, KEY)
    # get the response from the API with error handling
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logger.error(err)
        return []
    # convert the response to json format
    data = response.json()
    # get the weather forecast from the json data
    forecast_description = data["weather"][0]["description"]
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    # return the forecast data
    return [forecast_description, temperature, humidity, wind_speed]
