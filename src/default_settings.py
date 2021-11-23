import ctypes
from configparser import ConfigParser

from __init import game_path, settings_path
from logger import get_logger


def set_default_settings():
    """
    Sets default values for settings file
    """

    log = get_logger(__file__)

    config = ConfigParser()

    # Paths
    config["Paths"] = {"images_path": rf"{game_path}\\images",
                       "tiles_path": rf"{game_path}\\images\\tiles",
                       "characters_path": rf"{game_path}\\images\\characters",
                       "maps_path": rf"{game_path}\\maps",
                       }
    log.debug("Paths set to default")
    # Graphics
    config["Graphics"] = {"screen_width": ctypes.windll.user32.GetSystemMetrics(0),
                          "screen_height": ctypes.windll.user32.GetSystemMetrics(1),
                          "fullscreen": False,
                          "fps": 60,
                          }
    log.debug("Graphics set to default")
    # Input
    config["Input"] = {"pause": "escape",
                       "move_forward": "w",
                       "move_backward": "s",
                       "move_leftward": "a",
                       "move_rightward": "d",
                       "sprint": "left shift"
                       }
    # In-game
    config["In-game"] = {"sprint_modifier": "2"
                         }
    log.debug("Input set to default")

    with open(settings_path, 'w') as configfile:
        config.write(configfile)
    log.info("All settings set to default")

if __name__ == "__main__":
    set_default_settings()
