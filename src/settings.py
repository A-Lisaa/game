import os
from configparser import ConfigParser

from default_configs import *
from init_paths import settings_path
from logger import get_logger


class Configuration:
    def __init__(self):
        self.log = get_logger(__file__)
        self.config = ConfigParser()
        self.config.read(settings_path)

    def update_file(self):
        with open(settings_path, mode='w', encoding="utf-8") as configfile:
            self.config.write(configfile)

    def set_setting(self, section: str, setting: str, value: str):
        self.config[section][setting] = value
        self.update_file()
        self.log.debug("Setting %s of Section %s set to %s", setting, section, value)

    def set_default_setting(self, section: str, setting: str):
        self.set_setting(section, setting, eval(section)[setting])

    def set_default_section(self, section: str):
        self.config[section] = eval(section)
        self.update_file()
        self.log.debug("Section %s set to default", section)

    def set_all_default_settings(self):
        """
        Sets default values for settings file
        """
        # Paths
        self.set_default_section("Paths")
        self.log.debug("Paths set to default")
        # Graphics
        self.set_default_section("Graphics")
        self.log.debug("Graphics set to default")
        # Input
        self.set_default_section("Input")
        self.log.debug("Input set to default")

        self.log.info("All settings set to default")

    def get_all_settings(self) -> dict[str, str | int | float | bool]:
        if not os.path.exists(settings_path):
            self.set_all_default_settings()

        settings = {}
        for section in self.config.sections():
            for key in self.config[section]:
                value = self.config[section][key]
                if value in ("True", "False"):
                    value = bool(value)
                elif value.isnumeric():
                    value = int(value)
                else:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                settings[key] = value
                self.log.debug("Setting (%s) loaded", key)

        self.log.debug("All settings loaded succesfully")

        return settings
