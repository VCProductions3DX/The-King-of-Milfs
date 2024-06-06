#Profiles
label profiles:
    call screen eventmodescreen
screen profilescreen():
    modal True
    add gui.game_menu_background
    label _("Profiles") xpos 10 ypos 10
#Jump back to Story
    hbox:
        xalign 0.98
        yalign 0.03
        textbutton _("Replay Mode") action [Hide("profiles"), Jump("storymode")]
    hbox:
        frame:
            style_prefix "storyline"
            ysize 1080
            xsize 300
            vbox:
                xoffset 10
                yoffset 120
                imagebutton auto "gui/button/Reina_%s.webp" action [SetLocalVariable("selectedCharacter", ReinaC), SetLocalVariable("cg_eventpage", 1)]
                imagebutton auto "gui/button/Jenni_%s.webp"action [SetLocalVariable("selectedCharacter",JenniC), SetLocalVariable("cg_eventpage", 2)]
                imagebutton auto "gui/button/Briana_%s.webp" action [SetLocalVariable("selectedCharacter",BrianaC),SetLocalVariable("cg_eventpage", 3)]
                imagebutton auto "gui/button/Penny_%s.webp" action[SetLocalVariable("selectedCharacter",PennyC), SetLocalVariable("cg_eventpage", 4)]
                imagebutton auto "gui/button/Aisha_%s.webp" action [SetLocalVariable("selectedCharacter",AishaC), SetLocalVariable("cg_eventpage", 5)]
                imagebutton auto "gui/button/Camilla_%s.webp" action [SetLocalVariable("selectedCharacter",CamillaC), SetLocalVariable("cg_eventpage", 6)]
                imagebutton auto "gui/button/Sabrina_%s.webp" action [SetLocalVariable("selectedCharacter",SabrinaC),SetLocalVariable("cg_eventpage", 7)]
                imagebutton auto "gui/button/Rose_%s.webp"  action [SetLocalVariable("selectedCharacter",RoseC), SetLocalVariable("cg_eventpage", 8)]
                imagebutton auto "gui/button/Miyuki_%s.webp" action [SetLocalVariable ("selectedCharacter",MiyukiC) SetLocalVariable("cg_eventpage", 9)]
        frame:
            ysize 1080
            xsize 667
            vbox:
                add selectedCharacter.pic
        frame:
            ysize 1080
            xsize 700
            style_prefix "storyline"
            #spacing 10

            vbox:
                xoffset 20
                xsize 600
                ysize 100
                text "[selectedCharacter.name]" style "eventline_label"
                text "[selectedCharacter.title]" size 38
                text "[selectedCharacter.desc]" size 28

            vbox:
                xoffset 20
                yoffset 250
                xsize 600
                #ysize 300
                text "Trust: [selectedCharacter.c_trust] / [selectedCharacter.m_trust]" size 20
                bar value StaticValue(selectedCharacter.c_trust,selectedCharacter.m_trust) xsize 300
                text "Love:  [selectedCharacter.c_love] / [selectedCharacter.m_love]" size 20
                bar value StaticValue(selectedCharacter.c_love,selectedCharacter.m_love) xsize 300
              
           
style eventline_label:
    font "fonts/RicksAmericanPlainNF.ttf"
    size 60

style eventline_button_text:
    font "fonts/RicksAmericanPlainNF.ttf"
    idle_size 36
    hover_size 42
    color "#FFFF"
    outlines [ (absolute(1), "#000A", absolute(0), absolute(0)) ]
    hover_xoffset 20
