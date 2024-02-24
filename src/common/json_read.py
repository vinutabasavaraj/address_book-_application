import json
import os
from pathlib import Path

script_dir = os.path.dirname(__file__)

current_directory = Path(__file__).parents[0]

info_msg_filename = 'info_log_messages.json'
info_msg_file_path = current_directory / info_msg_filename
with open(info_msg_file_path) as data:
	info_msg = json.load(data)
info_msg

error_msg_filename = 'error_log_messages.json'
error_msg_file_path = current_directory / error_msg_filename
with open(error_msg_file_path) as data:
	error_msg = json.load(data)
error_msg
