import ctypes
from init_paths import game_path


paths = {"images_path": rf"{game_path}\\images",
         "tiles_path": rf"{game_path}\\images\\tiles",
         "characters_path": rf"{game_path}\\images\\characters",
         "maps_path": rf"{game_path}\\maps",
        }

graphics = {"screen_width": ctypes.windll.user32.GetSystemMetrics(0),
            "screen_height": ctypes.windll.user32.GetSystemMetrics(1),
            "fullscreen": False,
            "fps": 60.0,
            }

input = {"pause": "escape",
         "move_forward": "w",
         "move_backward": "s",
         "move_leftward": "a",
         "move_rightward": "d",
         "sprint": "left shift"
        }