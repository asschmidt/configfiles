from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen

from widgets import *

bar_margin = 5 # Margin = N E S W

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=30, margin=[bar_margin, bar_margin, bar_margin, bar_margin])),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=30, margin=[bar_margin, bar_margin, bar_margin, bar_margin])),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=30, margin=[bar_margin, bar_margin, bar_margin, bar_margin]))]


screens         = init_screens()
widgets_list    = init_widgets_list()
widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()