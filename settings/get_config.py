import configparser
import os
import sys


def get_settings():
    config = configparser.ConfigParser()
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    settings_path = os.path.join(base_dir, "settings.ini")
    config.read(settings_path, encoding='utf-8')
    return config

