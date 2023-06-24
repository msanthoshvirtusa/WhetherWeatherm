# import colorama, Fore and Style from colorama and pyfiglet from pyfiglet
import colorama
from colorama import Fore, Style
from pyfiglet import Figlet

# import forecast function from forecaster.py
from forecaster import forecast


# import logger from logger.py
from logger import logger

# Initialize colorama for colored output
colorama.init()

# A main function that takes city nameas input from user and calls forecast function to get the weather forecast


def main() -> None:
    while True:
        city = input(Fore.LIGHTBLUE_EX +
                     "Please Enter the beautiful city's name  : ")
        print()
        logger.info(f"Getting weather for city: {city}")
        weather_data = forecast(city)
        if len(weather_data) == 0:
            print(Fore.RED + "oops.. please enter a valid city name")
            print()
        else:
            logger.info(f"Got weather for city: {city}")
            print()
            print(Fore.GREEN + f"Weather forecast for {city}:")
            print(Fore.YELLOW + f"Description: {weather_data[0]}")
            print(Fore.YELLOW + f"Temperature: {weather_data[1]}°C")
            print(Fore.YELLOW + f"Humidity: {weather_data[2]}%")
            print(Fore.YELLOW + f"Wind Speed: {weather_data[3]} m/s")


if __name__ == "__main__":

    # Attractive command line interface
    f = Figlet(font='slant')
    welcome_message = f.renderText('Welcome to WhetherWeather')
    print(Fore.CYAN + welcome_message)
    print(Style.RESET_ALL)
    print()

    main()
