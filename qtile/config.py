#  _______     _________ _    _  ____  _   _ 
# |  __ \ \   / |__   __| |  | |/ __ \| \ | |
# | |__) \ \_/ /   | |  | |__| | |  | |  \| |
# |  ___/ \   /    | |  |  __  | |  | | . ` |
# | |      | |     | |  | |  | | |__| | |\  |
# |_|      |_|     |_|  |_|  |_|\____/|_| \_|
#  _      _____ ____  _____           _____  _____ ______  _____ 
# | |    |_   _|  _ \|  __ \    /\   |  __ \|_   _|  ____|/ ____|
# | |      | | | |_) | |__) |  /  \  | |__) | | | | |__  | (___  
# | |      | | |  _ <|  _  /  / /\ \ |  _  /  | | |  __|  \___ \ 
# | |____ _| |_| |_) | | \ \ / ____ \| | \ \ _| |_| |____ ____) |
# |______|_____|____/|_|  \_/_/    \_|_|  \_|_____|______|_____/ 

import os, subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# ===============================================================
#   _____ _    _  _____ _______ ____  __  __ 
#  / ____| |  | |/ ____|__   __/ __ \|  \/  |
# | |    | |  | | (___    | | | |  | | \  / |
# | |    | |  | |\___ \   | | | |  | | |\/| |
# | |____| |__| |____) |  | | | |__| | |  | |
#  \_____|\____/|_____/   |_|  \____/|_|  |_|
#  _      _____ ____  _____           _____  _____ ______  _____ 
# | |    |_   _|  _ \|  __ \    /\   |  __ \|_   _|  ____|/ ____|
# | |      | | | |_) | |__) |  /  \  | |__) | | | | |__  | (___  
# | |      | | |  _ <|  _  /  / /\ \ |  _  /  | | |  __|  \___ \ 
# | |____ _| |_| |_) | | \ \ / ____ \| | \ \ _| |_| |____ ____) |
# |______|_____|____/|_|  \_/_/    \_|_|  \_|_____|______|_____/ 

#def arrow_divider_left():
#	return TextBox(
#		widget.TextBox(
#			text="\u002F",
 #             		fontsize=32,)

# autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

# ===============================================================
#  _______ _    _ ______ __  __ ______  _____ 
# |__   __| |  | |  ____|  \/  |  ____|/ ____|
#    | |  | |__| | |__  | \  / | |__  | (___  
#    | |  |  __  |  __| | |\/| |  __|  \___ \ 
#    | |  | |  | | |____| |  | | |____ ____) |
#    |_|  |_|  |_|______|_|  |_|______|_____/ 

# Dracula
colors =[
	["#171837", "#171837"], # 0 - bar background
	["#FFFFFF", "#FFFFFF"], # 1 - focused window
	["#f8f8f2", "#f8f8f2"], # 2 - text color
	["#2d2846", "#2d2846"], # 3 - widget 1 
	["#97977b", "#97977b"], # 4 - widget 2 
	["#000000", "#000000"], # 5 - Black
	["#FFA500", "#FFA500"], # 6 - Orange
]
  
# ===============================================================
#  _  __________     ______ _____ _   _ _____   _____ 
# | |/ /  ____\ \   / /  _ \_   _| \ | |  __ \ / ____|
# | ' /| |__   \ \_/ /| |_) || | |  \| | |  | | (___  
# |  < |  __|   \   / |  _ < | | | . ` | |  | |\___ \ 
# | . \| |____   | |  | |_) || |_| |\  | |__| |____) |
# |_|\_\______|  |_|  |____/_____|_| \_|_____/|_____/ 

# Declare Mod Key as Windows Key  
mod = "mod4"

# Custom Keybinds
keys = [
   
   # Media Control
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/pause playing media"),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="previous playing media"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="previous playing media"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="next playing media"),
   
    # Volume Control
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="Decrease volume (5%)"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-"), desc="Decrease volume (5%)"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+"), desc="Increase volume (5%)"),
    Key(["control"], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 1%-"), desc="Decrease volume (1%)"),
    Key(["control"], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 1%+"), desc="Increase volume (1%)"),
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture toggle"), desc="Toggle Mic"),
    Key(["control"], "XF86AudioMicMute", lazy.spawn("amixer set Capture 10%-"), desc="Decrease Mic"),
    Key(["shift"], "XF86AudioMicMute", lazy.spawn("amixer set Capture 10%+"), desc="Increase Mic"),
   
   # Media Control
   Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Decrease monitor brightness"),
   Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+"), desc="Increase monitor brightness"),
   
    # Move Focus
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    
       
    # Move Windows
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
   
    # Reize Windows
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Unsplit Focused Window
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    
    # Toggle Window Float
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'), 
    
    # Launchers
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch kitty"),
    Key([mod], "e", lazy.spawn("terminator"), desc="Launch terminator + ranger"),  
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    
    # Rofi
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch rofi launcher"),
    Key([mod], "d", lazy.spawn("rofi -show window"), desc="Launch rofi launcher"),
    Key([mod], "x", lazy.spawn("rofi -show run"), desc="Launch rofi launcher"),
    
    # CoreShot
    Key([mod, "shift"], "s", lazy.spawn("coreshot"), desc="Launch CoreShot"),
    
    # Qtile Controls
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "r", lazy.spawn("gedit /home/mjalmonte/.config/qtile/config.py"), desc="Open the config"),    
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control" ], "t", lazy.window.toggle_floating(), desc='Toggle floating'),
    
]



# ===============================================================
# __          ______  _____  _  __ _____ _____        _____ ______  _____ 
# \ \        / / __ \|  __ \| |/ // ____|  __ \ /\   / ____|  ____|/ ____|
#  \ \  /\  / | |  | | |__) | ' /| (___ | |__) /  \ | |    | |__  | (___  
#   \ \/  \/ /| |  | |  _  /|  <  \___ \|  ___/ /\ \| |    |  __|  \___ \ 
#    \  /\  / | |__| | | \ \| . \ ____) | |  / ____ | |____| |____ ____) |
#     \/  \/   \____/|_|  \_|_|\_|_____/|_| /_/    \_\_____|______|_____/ 
                                                                     
groups = [
    Group("1", label="SYS", matches=[Match(wm_class=["gedit", "conky"],)]),
    Group("2", label="MDA", spawn=["spotify"], matches=[Match(wm_class=["spotify", "jellyfinmediaplayer"],)], layout="stack",),
    Group("3", label="WWW" , matches=[Match(wm_class=["firefox", "qbittorrentq"],)],layout="column"),
    Group("4", label="COM", spawn=["discord", "ferdi"], matches=[Match(wm_class=["discord","ferdi"],)], layout="stack"),
    Group("5", label="WRK", matches=[Match(wm_class=["google-chrome"],)]),
    Group("6", label=""),
    Group("7", label=""),
    Group("8", label="DEV", matches=[Match(wm_class=["atom"],)], layout="stack"),
    Group("9", label="GME", matches=[Match(wm_class=["minecraft-launcher", "Steam"],)], layout="stack"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
    
# ===============================================================
#  _           __     ______  _    _ _______ _____ 
# | |        /\\ \   / / __ \| |  | |__   __/ ____|
# | |       /  \\ \_/ | |  | | |  | |  | | | (___  
# | |      / /\ \\   /| |  | | |  | |  | |  \___ \ 
# | |____ / ____ \| | | |__| | |__| |  | |  ____) |
# |______/_/    \_|_|  \____/ \____/   |_| |_____/ 

layouts = [
    layout.Columns(
    	border_focus=colors[6],
    	border_width=4, 
    	margin=10,
    	),
    layout.Stack(
    	num_stacks=1,
    	margin=10,
    	border_width=0,
    	),
    	
    # layout.MonadTall(),
    
    # layout.Max(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Bsp(),
    # layout.Matrix(),
]

# ===============================================================
#  _______ ____  _____  ____          _____  
# |__   __/ __ \|  __ \|  _ \   /\   |  __ \ 
#    | | | |  | | |__) | |_) | /  \  | |__) |
#    | | | |  | |  ___/|  _ < / /\ \ |  _  / 
#    | | | |__| | |    | |_) / ____ \| | \ \ 
#    |_|  \____/|_|    |____/_/    \_|_|  \_\

widget_defaults = dict(
    font="Cantarell",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [	
            	
            	# Arch Updates
            	widget.Spacer(background=colors[3], length=10,),
            	widget.TextBox( text="", fontsize=24, background=colors[3], padding=10, mouse_callbacks = {'Button1':lazy.spawn("checkupdates"), 'Button3':lazy.spawn("kitty")},),
            	widget.CheckUpdates(no_update_string='0 ', display_format="{updates} ", distro="Arch_checkupdates", background=colors[3], update_interval=60, mouse_callbacks = {'Button1':lazy.spawn("checkupdates"), 'Button3':lazy.spawn("checkupdates")},),
            	widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
            	
            	# Workspace Indicator
            	widget.GroupBox(background=colors[3], inactive=colors[4], highlight_color=['171837', '171837'], highlight_method="line", disable_drag=True,),
            	widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
            	
            	# System Tray       
            	widget.Spacer(background=colors[3], length=10,), 
            	widget.Systray(background=colors[3], padding=10, icon_size=18,),
                widget.Spacer(background=colors[3], length=10,),
                
                # Spacer                
                widget.Spacer(background=colors[3],),
                
                # Current Qtile Layout
                widget.Spacer(background=colors[3], length=10,),
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                widget.CurrentLayoutIcon(scale=0.5, background=colors[3],),
                widget.CurrentLayout(scale=0.5, background=colors[3], fmt="{}"),
                
                # Volume
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                widget.Spacer(background=colors[3], length=10,),
                widget.TextBox( text="墳", fontsize=24, background=colors[3], ),
                widget.Volume(background=colors[3], fmt="{}", padding=10, channel="Master"),
                widget.TextBox( text="", fontsize=14, background=colors[3], ),
                widget.Volume(background=colors[3], fmt="{}", padding=10, channel="Capture"),
                
                # Battery
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),                
                widget.Spacer(background=colors[3], length=10,),
                widget.TextBox( text="", fontsize=24, background=colors[3],),
                widget.Battery(format='{char}  {percent:2.0%}', padding=10, background=colors[3], update_interval=2, charge_char="", discharge_char="", unknown_char="蘒",),
                
                # Wlan
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                widget.Spacer(background=colors[3], length=10,),
                widget.TextBox( text="", fontsize=24, background=colors[3],),
                widget.Wlan(format="{essid} {percent:2.0%}", disconnected_message="Disconnected", interface="wlp0s20f3", background=colors[3], padding=10,),
                       
                # Date + Clock
              	widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
              	widget.Spacer(background=colors[3], length=10,),
              	widget.TextBox( text="﨟", fontsize=24, background=colors[3],),
                widget.Clock(format="%I:%M %p %Z %A - %B %d, %Y", background=colors[3],padding=10,),
               
                # Arch Logo
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                widget.Spacer(background=colors[3], length=10,),
                widget.WidgetBox(
                	text_closed="",
                	text_open="",
                	fontsize=32,
                	padding=2,
                	background=colors[3],
                	close_button_location="right",
                	# Child Widgets
                	widgets=[
                		
                		# Config Options
                		 widget.WidgetBox(
                				text_closed="  ",
                				text_open=" ",
                				fontsize=26,
                				padding=0,
                				background=colors[3],
                				close_button_location="right",
                				
                				# Child Widgets
                				widgets=[
                					# Qtile Config
                					widget.TextBox(
                					text="    [ qtile ]",
                					fontsize=12,
                					padding=5,
                					background=colors[3],
                					mouse_callbacks = {'Button1':lazy.spawn("gedit /home/mjalmonte/.config/qtile/config.py"), },),
                					
                					# Nitrogen
                					widget.TextBox(
                					text="[ wallpaper ]   ",
                					fontsize=12,
                					padding=5,
                					background=colors[3],
                					mouse_callbacks = {'Button1':lazy.spawn("nitrogen"), },),
                				]),
                					
                		# Power Options
                		 widget.WidgetBox(
                				text_closed=" ",
                				text_open=" ",
                				fontsize=26,
                				padding=0,
                				background=colors[3],
                				close_button_location="right",
                				
                				# Child Widgets
                				widgets=[
                					# Restart
                					widget.TextBox(
                					text="[ restart ]",
                					fontsize=12,
                					padding=5,
                					background=colors[3],
                					mouse_callbacks = {'Button1':lazy.spawn("reboot"), },),
                					
                					# Shutdown
                					widget.TextBox(
                					text="[ shutdown ]   ",
                					fontsize=12,
                					padding=5,
                					background=colors[3],
                					mouse_callbacks = {'Button1':lazy.spawn("poweroff"), },),
                				]),
                	]),
                	widget.Spacer(background=colors[3], length=10,),
                
            ],
            30,
            backround="#171837",
            margin=[10, 10, 0, 10],
            # border_width=[5, 5, 5, 5],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    
    Screen(
        top=bar.Bar(
            [	
            	
            	# Arch Updates
            	widget.Spacer(background=colors[3], length=10,),
            	widget.TextBox( text="HDMI-0", background=colors[3], padding=10),
            	widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
            	
            	# Workspace Indicator
            	widget.GroupBox(background=colors[3], inactive=colors[4], highlight_color=['171837', '171837'], highlight_method="line", disable_drag=True,),
            	widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                        
                # Spacer                
                widget.Spacer(background=colors[3],),
                
                # Current Qtile Layout
                widget.Spacer(background=colors[3], length=10,),
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                widget.CurrentLayoutIcon(scale=0.5, background=colors[3],),
                widget.CurrentLayout(scale=0.5, background=colors[3], fmt="{}"),
                
                # Volume
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                widget.Spacer(background=colors[3], length=10,),
                widget.TextBox( text="墳", fontsize=24, background=colors[3], ),
                widget.Volume(background=colors[3], fmt="{}", padding=10, channel="Master"),
                widget.TextBox( text="", fontsize=14, background=colors[3], ),
                widget.Volume(background=colors[3], fmt="{}", padding=10, channel="Capture"),
                
                # Battery
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),                
                widget.Spacer(background=colors[3], length=10,),
                widget.TextBox( text="", fontsize=24, background=colors[3],),
                widget.Battery(format='{char}  {percent:2.0%}', padding=10, background=colors[3], update_interval=2, charge_char="", discharge_char="", unknown_char="蘒",),
                
                # Wlan
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                widget.Spacer(background=colors[3], length=10,),
                widget.TextBox( text="", fontsize=24, background=colors[3],),
                widget.Wlan(format="{essid} {percent:2.0%}", disconnected_message="Disconnected", interface="wlp0s20f3", background=colors[3], padding=10,),
                       
                # Date + Clock
              	widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
              	widget.Spacer(background=colors[3], length=10,),
              	widget.TextBox( text="﨟", fontsize=24, background=colors[3],),
                widget.Clock(format="%I:%M %p %Z %A - %B %d, %Y", background=colors[3],padding=10,),
               
                # Arch Logo
                widget.TextBox( text="\u002F", fontsize=72, padding=0, foreground=colors[4], background=colors[3],),
                widget.Spacer(background=colors[3], length=10,),
                widget.WidgetBox(
                	text_closed="",
                	text_open="",
                	fontsize=32,
                	padding=2,
                	background=colors[3],
                	close_button_location="right",
                	# Child Widgets
                	widgets=[
                		
                		# Config Options
                		 widget.WidgetBox(
                				text_closed="  ",
                				text_open=" ",
                				fontsize=26,
                				padding=0,
                				background=colors[3],
                				close_button_location="right",
                				
                				# Child Widgets
                				widgets=[
                					# Qtile Config
                					widget.TextBox(
                					text="    [ qtile ]",
                					fontsize=12,
                					padding=5,
                					background=colors[3],
                					mouse_callbacks = {'Button1':lazy.spawn("gedit /home/mjalmonte/.config/qtile/config.py"), },),
                					
                					# Nitrogen
                					widget.TextBox(
                					text="[ wallpaper ]   ",
                					fontsize=12,
                					padding=5,
                					background=colors[3],
                					mouse_callbacks = {'Button1':lazy.spawn("nitrogen"), },),
                				]),
                					
                		# Power Options
                		 widget.WidgetBox(
                				text_closed=" ",
                				text_open=" ",
                				fontsize=26,
                				padding=0,
                				background=colors[3],
                				close_button_location="right",
                				
                				# Child Widgets
                				widgets=[
                					# Restart
                					widget.TextBox(
                					text="[ restart ]",
                					fontsize=12,
                					padding=5,
                					background=colors[3],
                					mouse_callbacks = {'Button1':lazy.spawn("reboot"), },),
                					
                					# Shutdown
                					widget.TextBox(
                					text="[ shutdown ]   ",
                					fontsize=12,
                					padding=5,
                					background=colors[3],
                					mouse_callbacks = {'Button1':lazy.spawn("poweroff"), },),
                				]),
                	]),
                	widget.Spacer(background=colors[3], length=10,),
                
            ],
            30,
            backround="#171837",
            margin=[10, 10, 0, 10],
            # border_width=[5, 5, 5, 5],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
            
]

# ===============================================================
#  __  __  ____  _    _  _____ ______ 
# |  \/  |/ __ \| |  | |/ ____|  ____|
# | \  / | |  | | |  | | (___ | |__   
# | |\/| | |  | | |  | |\___ \|  __|  
# | |  | | |__| | |__| |____) | |____ 
# |_|  |_|\____/ \____/|_____/|______|

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  		# gitk
        Match(wm_class="makebranch"),  			# gitk
        Match(wm_class="maketag"),  			# gitk
        Match(wm_class="ssh-askpass"),  		# ssh-askpass
        Match(title="branchdialog"),  			# gitk
        Match(title="pinentry"),  			# GPG key password entry
        Match(wm_class="nitrogen"),  			# Nitrogen Wallpaper Manager
        Match(wm_class="coreshot"),  			# CoreShot Screenshot Tool
        #Match(wm_class="conky"),  			# Conky
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
