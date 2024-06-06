################################################################################
## Initialization
################################################################################

init offset = -1
init python:
    gui.init(1920, 1080)
define gui.accent_color = u'#ffffff'
define gui.idle_color = u'#ffffff'
define gui.idle_small_color = u'#ffffff'
define gui.hover_color = u'#FFFF99'
define gui.selected_color = u'#FFFF99'
define gui.insensitive_color = u'#aaaaaa7f'
define gui.muted_color = u'#66c1ff'
define gui.hover_muted_color = u'#99d6ff'
define gui.text_color = u'#ffffff'
define gui.interface_text_color = u'#ffffff'
define config.call_screen_roll_forward = True

## Fonts and Font Sizes ########################################################
define gui.text_font = "fonts/Bahnschrift_Regular.ttf"
define gui.name_text_font = "fonts/RicksAmericanPlainNF.ttf"
define gui.interface_text_font = "fonts/Bahnschrift_Regular.ttf"
define gui.label_text_font = "fonts/Bahnschrift_Regular.ttf"
define gui.title_text_font = "fonts/RicksAmericanPlainNF.ttf"
define gui.text_size = 36
define gui.name_text_size = 52
define gui.interface_text_size = 32
define gui.label_text_size = 52
define gui.notify_text_size = 24
define gui.title_text_size = 75

## Main and Game Menus #########################################################
define gui.main_menu_background = "images/Title4.png"
define gui.game_menu_background = "gui/game_menu2.png"

## Dialogue ####################################################################
define gui.textbox_height = 278
define gui.textbox_yalign = 1.0
define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.5
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75
define gui.dialogue_width = 1116
define gui.dialogue_text_xalign = 0.0

## Buttons #####################################################################
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = gui.label_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0
define gui.radio_button_borders = Borders(27, 6, 6, 6)
define gui.check_button_borders = Borders(27, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

#Sound,Music, SFX
define config.default_music_volume = 0.4
define config.default_sfx_volume = 0.4
define config.default_voice_volume = 0.4

## Choice Buttons ##############################################################
define gui.choice_button_width = None
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(5, 5, 5, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#FFFFFF"
define gui.choice_button_text_hover_color = "#FFFFFF"
define gui.choice_button_text_insensitive_color = "#444444"

## File Slot Buttons ###########################################################
## The save slot button.
define gui.slot_button_width = 1200
define gui.slot_button_height = 200
define gui.slot_button_borders = Borders(5, 5, 5, 5)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 240
define config.thumbnail_height = 180

## The number of columns and rows in the grid of save slots.
define gui.file_slot_rows = 4

## Positioning and Spacing #####################################################
define gui.navigation_xpos = 0
define gui.skip_ypos = 15
define gui.notify_ypos = 68
define gui.choice_spacing = 10
define gui.navigation_spacing = 0
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 15
define gui.main_menu_text_xalign = 1.0
define gui.main_menu_text_color = "#000000"

## Frames ######################################################################
define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False

## Bars, Scrollbars, and Sliders ###############################################
define gui.bar_size = 26
define gui.scrollbar_size = 18
define gui.slider_size = 24

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Vertical borders.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"

## History #####################################################################
define config.history_length = 250
define gui.history_height = 210
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

## Localization ################################################################
define gui.language = "unicode"

################################################################################
## Mobile devices
################################################################################

init python:
    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)
    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():
        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51
        ## Adjust the location of the textbox.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650
        ## Change the size and spacing of various things.
        gui.slider_size = 54
        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45
        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15
        gui.history_height = 285
        gui.history_text_width = 1035
        gui.quick_button_text_size = 30
        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

