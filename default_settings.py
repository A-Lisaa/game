import ctypes
from __init import settings_path
from logger import get_logger
from configparser import ConfigParser

def set_default_settings():
    """Sets default values for settings file
    """
    
    log = get_logger(__file__)
    
    config = ConfigParser()
    
    # Paths
    config["Paths"] = {"images_path": r".\\images",
                       "tiles_path": r".\\images\\tiles",
                       "characters_path": r".\\images\\characters",
                       "maps_path": r".\\maps",
                       }
    log.debug("Paths set to default")
    # Graphics
    config["Graphics"] = {"screen_height": ctypes.windll.user32.GetSystemMetrics(0),
                          "screen_width": ctypes.windll.user32.GetSystemMetrics(1),
                          "fps": 60,
                          "size": 32
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
    config["In-game"] = {"sprint_modifier": "1.5"
                         }
    log.debug("Input set to default")
    
    with open(settings_path, 'w') as configfile:
        config.write(configfile)
    log.info("All settings set to default")
    
if __name__ == "__main__":
    set_default_settings()