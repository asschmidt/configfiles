import os
import subprocess

from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

import colors
from apps import myTerm

widget_defaults = dict(
    font        ="Ubuntu Bold",
    fontsize    = 12,
    padding     = 0,
    background  = colors.themeColor[0]
)

extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
        widget.Image(
                 filename        = "~/.config/qtile/icons/alacritty-term.png",
                 scale           = "False",
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
                 ),
        widget.Prompt(
                 font = "Ubuntu Mono",
                 fontsize=14,
                 foreground = colors.themeColor[1]
        ),
        widget.GroupBox(
                 fontsize = 11,
                 margin_y = 5,
                 margin_x = 5,
                 padding_y = 0,
                 padding_x = 1,
                 borderwidth = 3,
                 active = colors.themeColor[8],
                 inactive = colors.themeColor[1],
                 rounded = False,
                 highlight_color = colors.themeColor[2],
                 highlight_method = "line",
                 this_current_screen_border = colors.themeColor[7],
                 this_screen_border = colors.themeColor[4],
                 other_current_screen_border = colors.themeColor[7],
                 other_screen_border = colors.themeColor[4],
                 ),
        widget.TextBox(
                 text = '|',
                 font = "Ubuntu Mono",
                 foreground = colors.themeColor[1],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.CurrentLayoutIcon(
                 # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                 foreground = colors.themeColor[1],
                 padding = 4,
                 scale = 0.6
                 ),
        widget.CurrentLayout(
                 foreground = colors.themeColor[1],
                 padding = 5
                 ),
        widget.TextBox(
                 text = '|',
                 font = "Ubuntu Mono",
                 foreground = colors.themeColor[1],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.WindowName(
                 foreground = colors.themeColor[6],
                 max_chars = 40
                 ),
        widget.GenPollText(
                 update_interval = 300,
                 func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
                 foreground = colors.themeColor[3],
                 fmt = '{}',
                 decorations=[
                     BorderDecoration(
                         colour = colors.themeColor[3],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.CPU(
                 format = 'Cpu: {load_percent}%',
                 foreground = colors.themeColor[4],
                 decorations=[
                     BorderDecoration(
                         colour = colors.themeColor[4],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.Memory(
                 foreground = colors.themeColor[8],
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                 format = '{MemUsed: .0f}{mm}',
                 fmt = 'Mem: {} used',
                 decorations=[
                     BorderDecoration(
                         colour = colors.themeColor[8],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.DF(
                 update_interval = 60,
                 foreground = colors.themeColor[5],
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e df')},
                 partition = '/',
                 #format = '[{p}] {uf}{m} ({r:.0f}%)',
                 format = '{uf}{m} free',
                 fmt = 'Disk: {}',
                 visible_on_warn = False,
                 decorations=[
                     BorderDecoration(
                         colour = colors.themeColor[5],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.Volume(
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
                 foreground = colors.themeColor[7],
                 fmt = 'Vol: {}',
                 decorations=[
                     BorderDecoration(
                         colour = colors.themeColor[7],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.KeyboardLayout(
                 foreground = colors.themeColor[4],
                 fmt = ' Kbd: {}',
                 configured_keyboards = ['de', 'us'],
                 decorations=[
                     BorderDecoration(
                         colour = colors.themeColor[4],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        widget.Clock(
                 foreground = colors.themeColor[8],
                 format = "%a, %b %d - %H:%M",
                 decorations=[
                     BorderDecoration(
                         colour = colors.themeColor[8],
                         border_width = [0, 0, 2, 0],
                     )
                 ],
                 ),
        widget.Spacer(length = 8),
        #widget.Systray(padding = 3),
        #widget.Spacer(length = 8),

        ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    #del widgets_screen2[22:24]
    return widgets_screen2