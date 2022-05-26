"""
Sets paths that can't be obtained from settings.ini
"""

import os

game_path = os.path.abspath("").replace("\\", "\\\\")
appdata_path = f"{game_path}\\__appdata__"
settings_path = f"{appdata_path}\\settings.ini"
logs_path = f"{appdata_path}\\logs"
