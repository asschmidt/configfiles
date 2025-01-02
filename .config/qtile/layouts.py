from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

import colors


layout_theme = {"border_width" : 2,
                "margin"       : 10,
                "border_focus" : colors.themeColor[8],
                "border_normal": colors.themeColor[0]
                }

layouts = [
    #layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(**layout_theme),
    layout.Tile(
         shift_windows=True,
         border_width = 1,
         margin = 1,
         ratio = 0.335,
         ),
    layout.Max(
         border_width = 0,
         margin = 0,
         ),
    layout.Stack(**layout_theme, num_stacks=2),
    layout.Columns(**layout_theme),
    layout.TreeTab(
        font = "Ubuntu Bold",
         fontsize = 11,
         border_width = 0,
         bg_color = colors.themeColor[0],
         active_bg = colors.themeColor[8],
         active_fg = colors.themeColor[2],
         inactive_bg = colors.themeColor[1],
         inactive_fg = colors.themeColor[0],
         padding_left = 8,
         padding_x = 8,
         padding_y = 6,
         sections = ["ONE", "TWO", "THREE"],
         section_fontsize = 10,
         section_fg = colors.themeColor[7],
         section_top = 15,
         section_bottom = 15,
         level_shift = 8,
         vspace = 3,
         panel_width = 240
         ),
    #layout.Zoomy(**layout_theme),
]

floating_layout = layout.Floating(
    border_focus=colors.themeColor[8],
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_type='utility'),
        Match(wm_class="confirmreset"),   # gitk
        Match(wm_class='confirm'),
        Match(wm_class='splash'),
        Match(wm_class="dialog"),         # dialog boxes
        Match(wm_class="download"),       # downloads
        Match(wm_class="error"),          # error msgs
        Match(wm_class="file_progress"),  # file progress boxes
        Match(wm_class='kdenlive'),       # kdenlive
        Match(wm_class="makebranch"),     # gitk
        Match(wm_class="maketag"),        # gitk
        Match(wm_class="notification"),   # notifications
        Match(wm_class='pinentry-gtk-2'), # GPG key password entry
        Match(wm_class="ssh-askpass"),    # ssh-askpass
        Match(wm_class="toolbar"),        # toolbars
        Match(wm_class="Yad"),            # yad boxesspeed
        #Match(wm_class='ghidra-Ghidra'),  # Ghidra
        Match(title="branchdialog"),      # gitk
        Match(title='Confirmation'),      # tastyworks exit box
        Match(title='Qalculate!'),        # qalculate-gtk
        Match(title='SpeedCrunch'),       # SpeedCrunch
        Match(func=lambda c: c.is_transient_for()),  # automatically float a window if it has a parent
    ]
)
