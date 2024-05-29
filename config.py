import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile import qtile
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from libqtile.widget import backlight
from libqtile.dgroups import simple_key_binder
from qtile_extras.widget.decorations import RectDecoration

mod = "mod4"

terminal = "alacritty"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "r", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
	Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "control"], "s", lazy.spawn("xrandr --output HDMI1 --auto --rotate left --left-of eDP1"), desc="Reload the config"),
    Key([mod, "shift"], "space", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "e", lazy.spawn("emacsclient -c -a 'emacs'"), desc="Spawn a doom-emacs"),
    Key([mod, "shift"], "m", lazy.spawn("emacs --with-profile=doom"), desc="Spawn a doom-emacs"),
    Key([mod], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'"), desc="Spawn a dmenu"),
    Key([mod], "n", lazy.spawn("obsidian"), desc="Spawn a obsidian"),
    Key([mod], "t", lazy.spawn("setxkbmap -layout tr"), desc="Swich keyboard layout to tr"),
    Key([mod], "u", lazy.spawn("setxkbmap -layout us"), desc="Swich keyboard layout to us"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise Volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute/Unmute Volume"),
    Key([mod], "p", lazy.spawn("playerctl -p spotify play-pause"), desc="Play/Pause player"),
    Key([mod], "o", lazy.spawn("playerctl -p spotify next"), desc="Skip to next"),
    Key([mod], "i", lazy.spawn("playerctl -p spotify previous"), desc="Skip to previous"),
    Key([], "XF86KbdBrightnessUp", lazy.spawn("brightnessctl --device='asus::kbd_backlight' s 1+"), desc="Spawn a obsidian"),
    Key([], "XF86KbdBrightnessDown", lazy.spawn("brightnessctl --device='asus::kbd_backlight' s 1-"), desc="Spawn a obsidian"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 30+"), desc="Spawn a obsidian"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 30-"), desc="Spawn a obsidian"),
]


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1),
    layout.Max(),
    layout.Stack(num_stacks=2),
    layout.Matrix(),
    layout.MonadWide(),
    layout.RatioTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = [["#282c34", "#282c34"],
          ["#171617", "#171617"],
          ["#dfdfdf", "#dfdfdf"],
          ["#474745", "#474745"],
          ["#595959", "#595959"],
          ["#da8548", "#da8548"],
          ["#311d3b", "#311d3b"],
          ["#7c7a7d", "#7c7a7d"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

groups = [Group("DEV", layout='monadtall'),
          Group("WWW", layout='monadtall'),
          Group("OBS", layout='monadtall'),
          Group("OBS", layout='monadtall'),
          Group("DOC", layout='monadtall'),
          Group("VBOX", layout='monadtall'),
          Group("CHAT", layout='monadtall'),
          Group("MUS", layout='monadtall'),
          Group("VID", layout='monadtall'),
          Group("GFX", layout='floating')]

dgroups_key_binder = simple_key_binder("mod4")



def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = "00000000"
                       ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "#00000000",
                        padding = 2,
                        fontsize = 14,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.GroupBox(
                        font = "Ubuntu Bold",
                        fontsize = 15,
                        margin_y = 3,
                        margin_x = 3,
                        borderwidth = 0,
                        active = colors[2],
                        inactive = colors[7],
                        rounded = True,
                        highlight_color = colors[1],
                        highlight_method = "block",
                        this_current_screen_border = colors[6],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[6],
                        other_screen_border = colors[4],
                        background = "#00000000",
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "00000000",
                        padding = 2,
                        fontsize = 14,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = "00000000"
                       ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "00000000",
                        padding = 2,
                        fontsize = 14,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[2],
                       background = "#00000000",
                       padding = 0,
                       scale = 0.3,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = "#00000000",
                       padding = 5,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "00000000",
                        padding = 2,
                        fontsize = 14,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = "00000000"
                       ),
              widget.WindowName(
                       foreground = colors[2],
                       background = "#00000000",
                       padding = 0,
                       ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "00000000",
                        padding = 2,
                        fontsize = 14,
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = "00000000"
                       ),
              widget.Systray(
                       background = "#00000000",
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = "00000000"
                       ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "00000000",
                        padding = 2,
                        fontsize = 14,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
                widget.Net(
                        interface = "wlp3s0",
                        format = 'Net: {down} ↓↑ {up}',
                        foreground = colors[1],
                        background = "#00000000",
                        padding = 5,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.ThermalSensor(
                       foreground = colors[1],
                        background = "#00000000",
                       threshold = 90,
                       fmt = 'Temp: {}',
                       padding = 5,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.CPU(
                       foreground = colors[1],
                        background = "#00000000",
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
              ),
              widget.Memory(
                       foreground = colors[1],
                        background = "#00000000",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                       fmt = 'Mem: {}',
                       padding = 5,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "00000000",
                        padding = 2,
                        fontsize = 14,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.TextBox(
                       text = ' ',
                       font = "Ubuntu Mono",
                        background = "#00000000",
                       foreground = colors[7],
                       padding = 0,
                       fontsize = 37
                       ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "00000000",
                        padding = 2,
                        fontsize = 14,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.Battery(
                        background = "#00000000",
                       font = "Ubuntu Mono",
                       format = '{hour:d}:{min:02d} {percent:2.0%} {char}',
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e rog-control-center')},
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
              ),
              widget.UPowerWidget(
                        background = "#00000000",
                       font = "Ubuntu Mono",
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
              ),
             widget.TextBox(
                        text = ' ',
                        font = "Ubuntu Mono",
                        background = "00000000",
                        padding = 2,
                        fontsize = 14,
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              widget.TextBox(
                       text = ' ',
                       font = "Ubuntu Mono",
                        background = "#00000000",
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                        marign = 10,
                        padding = 20,
                        format = "%A, %B %d - %H:%M ",
                        decorations = [
                        RectDecoration(
                            colour="#004040",
                            radius=15,
                            filled=True,
                            padding_y=10,
                            padding_x=0,
                            margin_x=20,
                            margin_y=20,
                            group=True
                            )
                        ],
                       ),
              ]
    return widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), background="#00000000", opacity=1.0, size=55)),]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

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

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

wmname = "LG3D"
