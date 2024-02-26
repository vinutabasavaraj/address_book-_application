import logging
import json

from pathlib import Path
from datetime import datetime


def generate_info_logs(log_name):
    """
    Function to create info logs for Address Application.
    """

    # Define the format for log messages
    message_format = logging.Formatter('%(asctime)s %(filename)s -> %(funcName)s() : %(lineno)s %(levelname)s: %(message)s')

    current_directory_path = Path(__file__).parents[2]
    properties_filename = current_directory_path/'properties.json'

    with open(properties_filename) as fp:
        properties = json.load(fp)
    properties
    
    log_dir_location = current_directory_path/properties.get("log_location")

    log_dir_location.mkdir(parents=True, exist_ok=True)
    
    today = datetime.now()
    dt_string = today.strftime("%d_%b_%Y")
    file_name = f'{log_name}_{dt_string}.log'

    log_filename = str(log_dir_location / file_name)
    
    # Create a logger object and configure it to log info messages to the specified file
    logger = logging.getLogger(log_filename)
    if logger.handlers:
        return logger
    else:
        handler = logging.FileHandler(log_filename)
        handler.setFormatter(message_format)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        handler.close()
        return logger

info_logs  = generate_info_logs('address_info')