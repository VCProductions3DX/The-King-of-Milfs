#Story Mode
#Each Chapter has its own set of events
#When the Chapter is clicked on, the events are shown.

label storymode:
    call screen storymodescreen

screen storymodescreen():
    tag menu
    add gui.game_menu_background
#Jump to Profiles
    hbox:
        xalign 0.98
        yalign 0.03
        textbutton _("Profiles >>") action [Hide("storymode"), Jump("profiles")]

#Hbox containing all chapters
    vbox:
        xalign 0.0
        yalign 0.0
        label _("Chapter Select") style "storyline_label"
    vbox:
        xalign 0.0
        ypos 0.12
        style_prefix "chapterselect"
        textbutton _("Chapter 1") action SetLocalVariable("cg_storypage_a", 1)
        if epilogue01event.status == "completed":
            textbutton _("Chapter 2") action SetLocalVariable("cg_storypage_a", 2)
        if epilogue02event.status == "completed":
            textbutton _("Chapter 3") action SetLocalVariable("cg_storypage_a", 3)
        if reinaevent08.status == "completed":
            textbutton _("Chapter 4") action SetLocalVariable("cg_storypage_a", 4)
        if epilogue04event.status == "completed":
            textbutton _("Chapter 5") action SetLocalVariable("cg_storypage_a", 5)
        if epilogue05event.status == "completed":
            textbutton _("Epilogue") action SetLocalVariable("cg_storypage_a", 6)
    hbox:
        xalign 0.85
        yalign 0.95
        textbutton _("Return") action [Return(), Hide("storymode_screen")]
        textbutton _("Save Game") action ShowMenu('save')
        textbutton _("Quit Game") action Quit(confirm=not main_menu)

    showif cg_storypage_a == 1:
        hbox:
            xpos 0.15
            ypos 0.14
            frame:
                ysize 750
                xsize 550
                style_prefix "storyline"
                vbox:
                    xoffset 50
                    yoffset 20
                    text _("Chapter 1:7 Years Later") style "storyline_label"

                vbox:
                    xoffset 80
                    yoffset 100
                    textbutton _("[prologue01.name]") hovered SetVariable("selectedChapter", prologue01) action [Hide("storymode_screen"), Jump("prologue01")]
                    textbutton _("[reinaevent01.name]") hovered SetVariable("selectedChapter", reinaevent01) action [Hide("storymode_screen"),Jump("reinaevent01")]
                    textbutton _("[camillaevent01.name]") hovered SetVariable("selectedChapter",camillaevent01) action [Hide("storymodescreen"), Jump("camillaevent01")]
                    textbutton _("[reinaevent02.name]") hovered SetVariable("selectedChapter", reinaevent02) action [Hide("storymode_screen"),Jump("reinaevent02")]
                    textbutton _("[pennyevent01.name]") hovered SetVariable("selectedChapter", pennyevent01) action [Hide("storymode_screen"),Jump("pennyevent01")]
                    textbutton _("[brianaevent01.name]") hovered SetVariable("selectedChapter", brianaevent01) action [Hide("storymode_screen"),Jump("brianaevent01")]
                    textbutton _("[sabrinaevent01.name]") hovered SetVariable("selectedChapter", sabrinaevent01)  action [Hide("storymode_screen"),Jump("sabrinaevent01")]
                    textbutton _("[camillaevent02.name]") hovered SetVariable("selectedChapter",camillaevent02) action [Hide("storymodescreen"), Jump("camillaevent02")]
                    textbutton _("[pennyevent02.name]") hovered SetVariable("selectedChapter", pennyevent02) action [Hide("storymode_screen"),Jump("pennyevent02")]
                    textbutton _("[jennievent01.name]") hovered SetVariable("selectedChapter", jennievent01) action [Hide("storymode_screen"),Jump("jennievent01")]
                    textbutton _("[jennievent02.name]") hovered SetVariable("selectedChapter", jennievent02) action [Hide("storymode_screen"),Jump("jennievent02")]
                    textbutton _("[brianaevent02.name]") hovered SetVariable("selectedChapter", brianaevent02) action [Hide("storymode_screen"),Jump("brianaevent02")]
                    textbutton _("[epilogue01.name]") hovered SetVariable("selectedChapter", epilogue01)action [Hide("storymode_screen"),Jump("epilogue01event")]
            frame:
                ysize 800
                xsize 500
                vbox:
                    add "[selectedChapter.image]"          
            frame:
                ysize 800
                xsize
                vbox:
                    text _("[selectedChapter.desc]")
                    text _("You have [selectedChapter.status] this event.")
                    #Description of each event goes here.

#Chapter 2
    showif cg_storypage_a == 2:
        hbox:
            xpos 0.15
            yalign 0.5
            frame:
                ysize 750
                xsize 550
                style_prefix "storyline"
                vbox:
                    xoffset 50
                    yoffset 20
                    label "Chapter 2: Starting Over"

                vbox:
                    xoffset 80
                    yoffset 100
                    textbutton _("[prologue02.name]") hovered SetVariable("selectedChapter", prologue01) action [Hide("storymode_screen"),Jump("prologue2")]
                    textbutton _("[reinaevent03.name]") hovered SetVariable("selectedChapter", reinaevent03) action [Hide("storymode_screen"),Jump("reinaevent03")]
                    textbutton _("[jennievent03.name]") hovered SetVariable("selectedChapter", jennievent03) action [Hide("storymode_screen"),Jump("jennievent03")]
                    textbutton _("[aishaevent01.name]")  hovered SetVariable("selectedChapter", aishaevent01) action [Hide("storymode_screen"), Jump("aishaevent01")]
                    textbutton _("[camillaevent03.name]")  hovered SetVariable("selectedChapter",camillaevent03)action [Hide("storymode_screen"),Jump("camillaevent03")]
                    textbutton _("[pennyevent03.name]") hovered SetVariable("selectedChapter", pennyevent03) action [Hide("storymode_screen"),Jump("pennyevent03")]
                    textbutton _("[brianaevent03.name]") hovered SetVariable("selectedChapter", brianaevent03)  action [Hide("storymode_screen"),Jump("brianaevent03")]
                    textbutton _("[reinaevent04.name]") hovered SetVariable("selectedChapter", reinaevent04) action [Hide("storymode_screen"),Jump("reinaevent04")]
                    textbutton _("[sabrinaevent02.name]") hovered SetVariable("selectedChapter", sabrinaevent02)  action [Hide("storymode_screen"),Jump("sabrinaevent02")]
                    textbutton _("[pennyevent04.name]") hovered SetVariable("selectedChapter", pennyevent04) action [Hide("storymode_screen"),Jump("pennyevent04")]
                    textbutton _("[brianaevent04.name]") hovered SetVariable("selectedChapter", brianaevent04)  action [Hide("storymode_screen"),Jump("brianaevent04")]
                    textbutton _("[jennievent04.name]") hovered SetVariable("selectedChapter", jennievent04) action [Hide("storymode_screen"),Jump("jennievent04")]
                    textbutton _("[epilogue02.name]") hovered SetVariable("selectedChapter",epilogue02) action [Hide("storymode_screen"),Jump("epilogue02event")]
            frame:
                ysize 800
                xsize 500
                vbox:
                    add "[selectedChapter.image]"
                    text _("This event is [selectedChapter.status].")

#Chapter 3
    showif cg_storypage_a == 3:
        hbox:
            xpos 0.15
            yalign 0.5
            frame:
                ysize 750
                xsize 550
                style_prefix "storyline"
                vbox:
                    xoffset 50
                    yoffset 20
                    label "Chapter 3: Changes"
                vbox:
                    xoffset 80
                    yoffset 100
                    textbutton _("[prologue03.name]") hovered SetVariable("selectedChapter", prologue03) action [Hide("storymode_screen"),Jump("prologue03")]
                    textbutton _("[miyukievent01.name]") hovered SetVariable("selectedChapter", miyukievent01) action [Hide("storymode_screen"),Jump("miyukievent01")]
                    textbutton _("[reinaevent05.name]") hovered SetVariable("selectedChapter", reinaevent05) action [Hide("storymode_screen"),Jump("reinaevent05")]
                    textbutton _("[jennievent05.name]") hovered SetVariable("selectedChapter", jennievent05) action [Hide("storymode_screen"),Jump("jennievent05")]
                    textbutton _("[camillaevent04.name]")  hovered SetVariable("selectedChapter",camillaevent04) action [Hide("storymode_screen"),Jump("camillaevent04")]
                    textbutton _("[aishaevent02.name]")  hovered SetVariable("selectedChapter", aishaevent02) action [Hide("storymode_screen"), Jump("aishaevent02")]
                    textbutton _("[sabrinaevent03.name]") hovered SetVariable("selectedChapter", sabrinaevent03)  action [Hide("storymode_screen"),Jump("sabrinaevent03")]
                    textbutton _("[brianaevent05.name]") hovered SetVariable("selectedChapter", brianaevent05)  action [Hide("storymode_screen"),Jump("brianaevent05")]
                    textbutton _("[reinaevent07.name]") hovered SetVariable("selectedChapter", reinaevent06) action [Hide("storymode_screen"),Jump("reinaevent06")]
                    textbutton _("[reinaevent08.name]") hovered SetVariable("selectedChapter",reinaevent07) action [Hide("storymode_screen"),Jump("reinaevent07")]
            frame:
                ysize 800
                xsize 500
                vbox:
                    add "[selectedChapter.image]"
                    text _("This event is [selectedChapter.status].")

# Chapter 4
    showif cg_storypage_a == 4:
        hbox:
            xpos 0.15
            yalign 0.5
            frame:
                ysize 750
                xsize 550
                style_prefix "storyline"
                vbox:
                    xoffset 50
                    yoffset 20
                    label "Chapter 4: Consequences"
                vbox:
                    xoffset 80
                    yoffset 100
                    textbutton _("[reinaevent08.name]")  hovered SetVariable("selectedChapter", reinaevent08) action [Hide("storymode_screen"), Jump("reinaevent08")]
                    textbutton _("[jennievent06.name]")  hovered SetVariable("selectedChapter",jennievent06)action [Hide("storymode_screen"),Jump("jennievent06")]                  
                    textbutton _("[miyukievent02.name]") hovered SetVariable("selectedChapter", miyukievent02) action [Hide("storymode_screen"),Jump("miyukievent02")]
                    textbutton _("[camillaevent05.name]")  hovered SetVariable("selectedChapter",camillaevent05) action [Hide("storymode_screen"),Jump("camillaevent05")]
                    textbutton _("[sabrinaevent04.name]") hovered SetVariable("selectedChapter", sabrinaevent04)  action [Hide("storymode_screen"),Jump("sabrinaevent04")]
                    textbutton _("[brianaevent06.name]") hovered SetVariable("selectedChapter", brianaevent06)  action [Hide("storymode_screen"),Jump("brianaevent06")]
                    textbutton _("[epilogue04.name]") hovered SetVariable("selectedChapter",epilogue04) action [Hide("storymode_screen"),Jump("epilogue04event")]
            frame:
                ysize 800
                xsize 500
                vbox:
                    add "[selectedChapter.image]"
                    text _("This event is [selectedChapter.status].")

#Chapter 5
    showif cg_storypage_a == 5:
        hbox:
            xpos 0.15
            yalign 0.5
            frame:
                ysize 750
                xsize 550
                style_prefix "storyline"
                vbox:
                    xoffset 50
                    yoffset 20
                    label "Chapter 5:A New Man"
                vbox:
                    xoffset 80
                    yoffset 100
                    textbutton _("[prologue05.name]") hovered SetVariable("selectedChapter", prologue05) action [Hide("storymode_screen"),Jump("prologue05")]
                    textbutton _("[brianaevent07.name]") hovered SetVariable("selectedChapter", brianaevent07)  action [Hide("storymode_screen"),Jump("brianaevent07")]
                    textbutton _("[reinaevent09.name]")  hovered SetVariable("selectedChapter", reinaevent09) action [Hide("storymode_screen"), Jump("reinaevent09")]
                    textbutton _("[jennievent07.name]")  hovered SetVariable("selectedChapter",jennievent07)action [Hide("storymode_screen"),Jump("jennievent07")]
                    textbutton _("[sabrinaevent05.name]") hovered SetVariable("selectedChapter", sabrinaevent05)  action [Hide("storymode_screen"),Jump("sabrinaevent05")]
                    textbutton _("[pennyevent05.name]") hovered SetVariable("selectedChapter", pennyevent05) action [Hide("storymode_screen"),Jump("pennyevent05")]
                    textbutton _("[epilogue05.name]") hovered SetVariable("selectedChapter",epilogue05) action [Hide("storymode_screen"),Jump("epilogue05event")]
            frame:
                ysize 800
                xsize 500
                vbox:
                    add "[selectedChapter.image]"
                    text _("This event is [selectedChapter.status].")

#Chapter 5
    showif cg_storypage_a == 6:
        hbox:
            xpos 0.15
            yalign 0.5
            frame:
                ysize 750
                xsize 550
                style_prefix "storyline"
                vbox:
                    xoffset 50
                    yoffset 20
                    label "Epilogue"
                vbox:
                    xoffset 80
                    yoffset 100
                    textbutton _("[epiloguestart.name]") hovered SetVariable("selectedChapter", epiloguestart) action [Hide("storymode_screen"),Jump("epiloguestart")]
                    textbutton _("[brianaending.name]") hovered SetVariable("selectedChapter", brianaending)  action [Hide("storymode_screen"),Jump("brianaending")]
                    textbutton _("[reinaending.name]")  hovered SetVariable("selectedChapter", reinaending) action [Hide("storymode_screen"), Jump("reinaending")]
                    textbutton _("[jenniending.name]")  hovered SetVariable("selectedChapter",jenniending)action [Hide("storymode_screen"),Jump("jenniending")]
                    textbutton _("[sabrinaending.name]") hovered SetVariable("selectedChapter", sabrinaending)  action [Hide("storymode_screen"),Jump("sabrinaending")]
                    textbutton _("[pennyending.name]") hovered SetVariable("selectedChapter", pennyending) action [Hide("storymode_screen"),Jump("pennyending")]
                    textbutton _("[camillaending.name]") hovered SetVariable("selectedChapter", camillaending) action [Hide("storymode_screen"),Jump("camillaending")]
                    textbutton _("[badending.name]") hovered SetVariable("selectedChapter",badending) action [Hide("storymode_screen"),Jump("badending")]
                    textbutton _("[hiddenending.name]") hovered SetVariable("selectedChapter",hiddenending) action [Hide("storymode_screen"),Jump("kingending")]
            frame:
                ysize 800
                xsize 500
                vbox:
                    add "[selectedChapter.image]"
                    text _("This event is [selectedChapter.status].")



style storyline_label:
    font "fonts/RicksAmericanPlainNF.ttf"
    size 60
style chapterselect_button_text:
    font "fonts/RicksAmericanPlainNF.ttf"
    size 48
    hover_color "#000000"
    selected_color "#000000"
style chapterselect_button:
    hover_background "#FFFF99"
    selected_background "#FFFF99"
    selected_xoffset 15
style storyline_button:
    hover_background "#FFFF99"
    selected_background "#FFFF99"
style storyline_button_text:
    font "fonts/RicksAmericanPlainNF.ttf"
    idle_size 38
    hover_size 42
    idle_color "#FFFFFF"
    hover_color "#000000"
    idle_outlines [ (absolute(1), "#000A", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(1), "#FFF", absolute(0), absolute(0)) ]
