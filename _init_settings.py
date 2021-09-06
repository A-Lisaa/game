from __init import settings_path
from logger import get_logger
from configparser import ConfigParser

"""
Makes variables based on settings.ini by pattern: key = value
"""

log = get_logger(__file__)

config = ConfigParser()
config.read(settings_path)
for section in config.sections():
    for key in config[section]:
        exec(f"{key} = '{config[section][key]}'")
        log.debug(f"Setting ({key}) loaded")
log.info("All settings loaded succesfully")