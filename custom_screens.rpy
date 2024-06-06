#Splash Screen
label splashscreen:
    scene black
    with Pause(1)
    show vclogo with dissolve
    with Pause(1)
    scene black with dissolve
    with Pause(1)
return

#Consent Screen
screen consentscreen():
    frame:
        #ysize 1080
        xsize 1000
        xalign 0.5
        yalign 0.3
        vbox:
            style_prefix "consent"
            text _("This is a work of fiction.") size 48
            text _("All names, characters, businesses,places, events, locales, and incidents are either products of the author's imagination or used in a fictitous manner.") yoffset 50
            text _("Any resemblance to actual persons, living or dead, or actual events is purely coincidental.")yoffset 75

            text _("Are you 18 years of age or older?") size 42 yoffset 150

            hbox:
                style_prefix "consent"
                yoffset 250
                xalign 0.5
                textbutton _("Yes") action [Hide("consent screen"), Jump ("playerentername")]

                textbutton _("No") action Quit(confirm=not main_menu)

#Finale Screen
#The player has the option to clear persistent data and play again.


#Change Language
#This is for anyone who wants to add a translation patch
#screen changelanguage():
    #add gui.game_menu_background
    #label _("Change Language") xpos 10 ypos 10 style "taskline_label"

    #vbox:
        #xalign 0.5
        #yalign 0.3


        #textbutton "English" action Language(None)
        #textbutton _("Español") style "roboto_desc" action Language("Spanish")
        #textbutton _("Français") style "roboto_desc" action Language ("French")
        #textbutton _("Português") style "roboto_desc" #action Language ("Portuguese")
        #textbutton _("Português(Brasil)") style "roboto_desc" action Language ("PortugueseBR")
        #textbutton _("Italiano") style "roboto_desc" action Language ("Italian")
        #textbutton _("Română") style "roboto_desc" action Language ("Romanian")

        #textbutton _("Deutsch") style "roboto_desc" action Language ("German")
        #textbutton _("Nederlands") style "roboto_desc" action Language ("Dutch")
        #textbutton _("Svenska") style "roboto_desc" action [Language ("Swedish")
        #textbutton _("Dansk") style "roboto_desc" action [Language ("Danish")
        #textbutton _("Norsk") style "roboto_desc" action [Language ("Norwegian")

        #textbutton _("Türkçe") style "roboto_desc" action [Language ("Turkish")

        #textbutton _("Руссиан") style "nanum_desc" action Language("Russian")
        #textbutton _("Ελληνικά") style "roboto_desc" action Language("Greek")
        #textbutton _("日本語") style "nanum_desc" action Language("Japanese")
        #textbutton _("한국어") style "nanum_desc" action Language("Korean")
        #textbutton _("中文简单") style "noto_desc" action Language("ChineseSimple")

        #textbutton _("ไทย") style "kanit_desc" action Language("Thai")
        #textbutton _("اللغه العربية") style "mada_desc" action Language("Arabic")
        #textbutton _("עברית") style "rubik_desc" action Language("Hebrew")

        #Latin languages
        #translate_font("Spanish", "font/Roboto_Regular.ttf")
        #translate_font("French", "font/Roboto_Regular.ttf")
        #translate_font("Portuguese", "font/Roboto_Regular.ttf")
        #translate_font("PortugueseBR", "font/Roboto_Regular.ttf")
        #translate_font("Italian", "font/Roboto_Regular.ttf")
        #translate_font("Romanian", "font/Roboto_Regular.ttf")
        #German languages
        #translate_font("German", "font/Roboto_Regular.ttf")
        #translate_font("Dutch", "font/Roboto_Regular.ttf")
        #translate_font("Swedish", "font/Roboto_Regular.ttf")
        #translate_font("Danish", "font/Roboto_Regular.ttf")
        #translate_font("Norwegian", "font/Roboto_Regular.ttf")
        #Turkish
        #translate_font("Turkish", "font/Roboto_Regular.ttf")
        #Cyrillic languages
        #translate_font("Russian", "font/NanumGothic_Regular.ttf")
        #Japanese
        #translate_font("Japanese", "font/NanumGothic_Regular.ttf")
        #Korean
        #translate_font("Korean", "font/NanumGothic_Regular.ttf")
        #Greek
        #translate_font("Greek", "font/NanumGothic_Regular.ttf")
        #Chinese Simple
        #translate_font("ChineseSimple", "font/NanumGothic_Regular.ttf")
        #Arabic
        #translate_font("Arabic", "font/Mada_Regular.ttf")
        #Hebrew
        #translate_font("Hebrew", "font/Rubik_Regular.ttf")
        #Thai
        #translate_font("Thai", "font/Kanit_Regular.ttf")

    #textbutton _("Return") action [Return(), Hide("changelanguage")] xalign 0.97 yalign 0.95


style consent_text is gui_text:
    properties gui.text_properties("interface")
    xalign 0.5
    yspacing 70

style consent_button_text is gui_text:
    properties gui.text_properties("button")
    xalign 0.5
    xspacing 100




   
