import yaml
from model.config import Config
import pathlib
import glob
import os

CONFIG_FILE_PATH = "/usr/src/app/config.yaml"

def load_config(file_path):
    global CONFIG 
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    CONFIG = Config(data)

load_config(CONFIG_FILE_PATH)