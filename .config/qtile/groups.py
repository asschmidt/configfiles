#from libqtile import qtile
from libqtile.config import Group, Key
from libqtile.lazy import lazy

from keys import mod, keys

groups        = []
group_names   = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
group_labels  = ["DEV", "TOL", "UTL", "SYS", "MSC", "DOC", "WWW", "VID", "MUS",]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

# Create the groups defined by the group_names and group_labels lists
for i in range(len(group_names)):
    groups.append(
        Group(
            name   = group_names[i],
            layout = group_layouts[i].lower(),
            label  = group_labels[i],
        ))

for group in groups:
    keys.extend(
        [
            # mod + letter of group = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=False),
                desc="Move focused window to group {}".format(group.name),
            ),
        ]
    )

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)