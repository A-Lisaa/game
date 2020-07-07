from pygame.locals import *
from ctypes import windll
from set_settings import update_setting

def set_default_settings():
    # Input
    update_setting("Input", "pause", f"{K_ESCAPE} # escape")
    update_setting("Input", "move_forward", f"{K_w} # w")
    update_setting("Input", "move_backward", f"{K_s} # s")
    update_setting("Input", "move_leftward", f"{K_a} # a")
    update_setting("Input", "move_rightward", f"{K_d} # d")
    # Graphics
    update_setting("Graphics", "SCREEN_HEIGHT", f"{windll.user32.GetSystemMetrics(0)}")
    update_setting("Graphics", "SCREEN_WIDTH", f"{windll.user32.GetSystemMetrics(1)}")
    update_setting("Graphics", "FPS", "60")
    update_setting("Graphics", "size", "16")