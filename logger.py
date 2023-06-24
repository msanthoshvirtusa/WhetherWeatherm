# Import logging for python
import logging
import os

# Get current working directory
cwd = os.getcwd()

# Create logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create file handler and set its properties
file_handler = logging.FileHandler(f'{cwd}//weather_forecast.log')
file_handler.setLevel(logging.INFO)

# Create log formatter and set it for the file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)
