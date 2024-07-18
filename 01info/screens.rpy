﻿################################################################################
## Initialization
################################################################################

init offset = -1
default persistent.textbox_transparency = 1.0
default l_alpha = 1 - persistent.textbox_transparency
################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################

screen say(who, what):
    style_prefix "say"
   
    window:
        id "window"
        #######Textbox transparency
        background Image(im.Alpha("gui/textbox.png", l_alpha), xalign=0.5, yalign=1.0)
        ######
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')
style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background None
    color "#FFFFFF"
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
style say_dialogue:
    color "#FFFFFF"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

## Input screen ################################################################
screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xalign gui.dialogue_text_xalign
            #xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos
            text prompt style "input_prompt"
            input id "input"
style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    #color "#FFFFFF"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    #color "#FFFFFF"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

## Choice screen ###############################################################
screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.9
        yalign 0.6
        for i in items:
            textbutton i.caption action i.action

define config.narrator_menu = True
style choice_vbox is vbox
style choice_button is button
style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing
style choice_button is default:
    properties gui.button_properties("choice_button")
style choice_button_text:
    idle_color "#FFFFFF"
    hover_color "#FFFF99"
    insensitive_color "#aaaaaa7f"
    size 36
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    hover_xoffset 20

## Quick Menu screen ###########################################################
screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Options") action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")
default quick_menu = True
style quick_button is default
style quick_button_text is button_text
style quick_button:
    background None
    xpadding 5
style quick_button_text:
    background None
    size int(config.screen_height / 60)
    idle_color "#FFFF"
    hover_color "#0F0F"
    insensitive_color "#4445"
    outlines [ (absolute(1), "#000A", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(1), "#000F", absolute(0), absolute(0)) ]



################################################################################
## Main and Game Menu Screens
################################################################################
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        ypos 150
        spacing 0
        if main_menu:
            textbutton _("Start") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/switch7.ogg")] action Start()
        else:
            textbutton _("Profiles") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/click3.ogg"), Jump("profiles")]
            textbutton _("Chapters") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/click3.ogg"), Jump("storymode")]
            textbutton _("Gallery") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/click3.ogg"), ShowMenu("gallery")]
            textbutton _("Save") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/switch7.ogg")] action ShowMenu("save")
        textbutton _("Load") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/switch7.ogg")] action ShowMenu("load")
        textbutton _("Settings") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/switch7.ogg")] action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()
            textbutton _("Credits") action ShowMenu("about")
        if renpy.variant("pc"):
            textbutton _("Help") action ShowMenu("help")
            textbutton _("Quit") action Quit(confirm=not main_menu)
style navigation_button is gui_button
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
style navigation_button_text:
    font "fonts/RicksAmericanPlainNF.ttf"
    idle_size 60
    hover_size 72
    color "#FFFF"
    outlines [ (absolute(1), "#000A", absolute(0), absolute(0)) ]
    hover_xoffset 20

screen main_menu():
    tag menu
    add gui.main_menu_background
    vbox:
        style_prefix "mainmenu"
        xpos gui.navigation_xpos
        ypos 500
        spacing 0
        textbutton _("Start") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/switch7.ogg")] action Start()
        textbutton _("Load") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/switch7.ogg")] action ShowMenu("load")
        textbutton _("Settings") hovered [Play("sound", "sfx/rollover3.ogg")] clicked [Play("sound", "sfx/switch7.ogg")] action ShowMenu("preferences")
        if renpy.variant("pc"):
            textbutton _("Help") action ShowMenu("help")
            textbutton _("Quit") action Quit(confirm=not main_menu)
    vbox:
        xalign 0
        ypos 1050
        text _("Version 1.0.1 - English") size 12 color "#fff"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -100
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_version:
    properties gui.text_properties("version")
style mainmenu_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
style mainmenu_button_text:
    font "fonts/RicksAmericanPlainNF.ttf"
    idle_size 60
    hover_size 72
    color "#FFFF"
    outlines [ (absolute(1), "#000A", absolute(0), absolute(0)) ]
    hover_xoffset 20

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    textbutton _("Return"):
        style "return_button"
        action Return()
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text
style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu.png"
style game_menu_navigation_frame:
    xsize 420
    yfill True
style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15
style game_menu_viewport:
    xsize 1380
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_side:
    spacing 15
style game_menu_label:
    xpos 75
    ysize 180
style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
style return_button:
    xalign 0.9
    yalign 1.0
    yoffset -45
## About screen ################################################################
screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "The King of MILFs"
            text _("Version 1.0.0")
            text _("Writer/Developer/Animation: CocoVC")

            textbutton _("Itch.io")action OpenURL ("https://vcproductions.itch.io")
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_label_text:
    size gui.label_text_size
screen save():
    tag menu
    use file_slots(_("Save"))
screen load():
    tag menu
    use file_slots(_("Load"))
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    use game_menu(title):
        fixed:
            order_reverse True
            button:
                style "page_label"
                key_events True
                xalign 0.5
                ypos -150
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            #if title == "Save":
                #hbox:
                    #text "Name : "
                    #input:
                        #value VariableInputValue('save_name')
            ## The grid of file slots.
            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                ypos -75
                spacing 10
                #yalign 1.0
                #spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")
                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 13):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()
            vbox:
                style_prefix "slot"
                xalign 0.5
                yalign 0
                spacing gui.slot_spacing
                for i in range(gui.file_slot_rows):
                    $slot = i + 1
                    button:
                        hovered [Play ("sound", "sfx/rollover3.ogg")]
                        clicked [Play ("sound", "sfx/save.ogg")]
                        action FileAction(slot)
                        has hbox
                        add FileScreenshot(slot) xpos 15 ypos 5
                        vbox:
                            xpos 20 ypos 50
                            text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                            key "save_delete" action FileDelete(slot)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
style page_button:
    properties gui.button_properties("page_button")
style page_button_text:
    properties gui.button_text_properties("page_button")
style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
screen preferences():
    tag menu
    use game_menu(_("Options"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:

                    label _("Text Speed")
                    bar value Preference("text speed")
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
                    label _("Textbox Transparency")
                    bar value FieldValue (persistent, "textbox_transparency", range=1.0, style="slider")
                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
style pref_label_text:
    yalign 1.0
    font "fonts/RicksAmericanPlainNF.ttf"
    size 60
    idle_color "#FFFF"
    outlines [ (absolute(1), "#000A", absolute(0), absolute(0)) ]
style pref_vbox:
    xsize 338
style radio_vbox:
    spacing gui.pref_button_spacing
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
style radio_button_text:
    properties gui.button_text_properties("radio_button")
style check_vbox:
    spacing gui.pref_button_spacing
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text:
    properties gui.button_text_properties("check_button")
style slider_slider:
    xsize 525
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_vbox:
    xsize 675

screen history():
    tag menu
    predict False
    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False                     
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                $what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_allow_tags = { "alt", "noalt" }
style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text
style history_window:
    xfill True
    ysize gui.history_height
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
style history_label:
    xfill True
style history_label_text:
    xalign 0.5

screen help():
    tag menu
    default device = "keyboard"
    use game_menu(_("Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 23
            hbox:
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")
    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")
    hbox:
        label _("Escape")
        text _("Accesses the game menu.")
    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")
    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")
    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")
    hbox:
        label "H"
        text _("Hides the user interface.")
    hbox:
        label "S"
        text _("Takes a screenshot.")
    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():
    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")
    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")
    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")

screen gamepad_help():
    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")
    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")
    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")
    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")
    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")
    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")
    textbutton _("Calibrate") action GamepadCalibrate()

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_button:
    properties gui.button_properties("help_button")
    xmargin 12
style help_button_text:
    properties gui.button_text_properties("help_button")
style help_label:
    xsize 375
    right_padding 30
style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 150
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text
style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame2.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 9
            text _("Skipping Story.")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text
style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding
style skip_text:
    size gui.notify_text_size
style skip_triangle:
    font "DejaVuSans.ttf"

screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 5.25 action Hide('notify')
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
style notify_frame is empty
style notify_text is gui_text
style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
style notify_text:
    properties gui.text_properties("notify")

##For Mobile Builds:
style pref_vbox:
    variant "medium"
    xsize 675
screen quick_menu():
    variant "touch"
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()
style window:
    variant "small"
    background "gui/phone/textbox.png"
style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"
style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"
style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"
style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"
style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"
style game_menu_navigation_frame:
    variant "small"
    xsize 510
style game_menu_content_frame:
    variant "small"
    top_margin 0
style pref_vbox:
    variant "small"
    xsize 600
style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"
style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"
style slider_vbox:
    variant "small"
    xsize None
style slider_slider:
    variant "small"
    xsize 900
