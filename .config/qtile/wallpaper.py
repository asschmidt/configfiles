import os
import random
from typing import Callable

from libqtile import qtile

from screens import screens

WALLPAPERS_PATH           = "/home/andreas/OpenSource/wallpapers"
WALLPAPER_TIMEOUT_MINUTES = 10

class Timer():
    def __init__(self, timeout: int, callback: Callable) -> None:
        self.callback = callback
        self.timeout = timeout
        self.call()

    def call(self) -> None:
        self.callback()
        self.setup_timer()

    def setup_timer(self) -> None:
        self.timer = qtile.call_later(self.timeout, self.call)
        pass


def set_random_wallpaper() -> None:
    wallpapers = [
        os.path.join(WALLPAPERS_PATH, x) for x in os.listdir(WALLPAPERS_PATH) if x[-4:] == ".jpg"
    ]

    wallpaper = random.choice(wallpapers)
    set_wallpaper(wallpaper)


def set_wallpaper(file_path: str) -> None:
    for screen in qtile.screens:
        screen.cmd_set_wallpaper(file_path, 'fill')
    #pass


# Set the first random wallpaper
#set_random_wallpaper()
