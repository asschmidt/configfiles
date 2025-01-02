import os
import subprocess

from libqtile import hook, qtile
from libqtile.log_utils import logger

from wallpaper import *

wallpaperTimer = None

@hook.subscribe.startup_once
def start_once():
    #wallpaperTimer = Timer(WALLPAPER_TIMEOUT_MINUTES * 60, set_random_wallpaper)

    qtile.cmd_spawn("bash /home/andreas/.config/qtile/autostart.sh")
    logger.warning("Called Autostart")

    set_wallpaper(WALLPAPERS_PATH + '/0199.jpg')


@hook.subscribe.client_name_updated
def spotify(window):
    if window.name == 'Spotify':
        window.togroup(group_name='9')
        logger.warning("Moved Spotify Window")
