
define config.name = _("The King of Milfs")
define gui.show_name = False
define config.version = "1.0.00.00"
#Full Game.Main Story.Patch. Hotfix
# define gui.about = _p(""" """)

define build.name = "KingOfMilfs"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.menu_include_disabled = True
# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"
define config.main_menu_music = "music/Title.ogg"
define config.developer = True
## Transitions ##
define config.enter_transition = None
define config.exit_transition = None
define config.intra_transition = None
#Loading Menu Screen
define config.after_load_transition = None
#Ending Screen
define config.end_game_transition = None

## Window management ###
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Preference defaults ###
default preferences.text_cps = 0
default preferences.afm_time = 15

## Save directory #####
## Windows: %APPDATA\RenPy\<config.save_directory>
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
## Linux: $HOME/.renpy/<config.save_directory>
define config.save_directory = "KingofMilfs-1625785598"

## Icon ####
define config.window_icon = "gui/window_icon.png"

## Build configuration #
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.archive("01info", "all")
    build.classify('game/01info/**.**', '01info')
    #Story Patch
    build.archive("02story", "all")
    build.classify('game/02story/**.**', '02story')
    build.archive("images", "all")
    build.classify('game/images/**.**', 'images')
    build.archive("videos", "all")
    build.classify('game/videos/**.**', 'videos')
    build.archive("music", "all")
    build.classify('game/music/**.**', 'music')
    build.archive("sfx", "all")
    build.classify('game/sfx/**.**', 'sfx')
    build.documentation('*.html')
    build.documentation('*.txt')

# define build.itch_project = "vcproductions/the-king-of-milfs"
