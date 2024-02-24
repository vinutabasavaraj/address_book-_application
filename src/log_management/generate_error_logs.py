import logging
import json


from pathlib import Path
from datetime import datetime


def generate_error_logs(log_name):
    """
    Function to create errror logs for Address Application.
    """
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
    
    logger = logging.getLogger(log_filename)
    if logger.handlers:
        return logger
    else:
        handler = logging.FileHandler(log_filename)
        handler.setFormatter(message_format)
        logger.setLevel(logging.ERROR)
        logger.addHandler(handler)
        handler.close()
        return logger

error_logs  = generate_error_logs('address_error')