"""
Makes a dictionary based on settings.ini by format {key: value}
"""

import os
from configparser import ConfigParser

from __init import settings_path
from default_settings import set_default_settings
from logger import get_logger


if not os.path.exists(settings_path):
    set_default_settings()

__log = get_logger(__file__)

settings = {}
config = ConfigParser()
config.read(settings_path)
for section in config.sections():
    for key in config[section]:
        settings[key] = config[section][key]
        __log.debug("Setting (%s) loaded", key)
__log.info("All settings loaded succesfully")
