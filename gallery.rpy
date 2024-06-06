style gallery_stuff_grid:
    xalign 0.6
    yalign 0.3
    xspacing 20
    yspacing 20

style gallery_stuff_hbox:
    xalign 0.5
    yanchor 0.95
    ypos 0.97
    xspacing 10

style gallery_nav_vbox:
    xalign 0.03
    ypos 100
    spacing 0

style gallery_nav_button_text:
    font "fonts/RicksAmericanPlainNF.ttf"
    size 48
    color "#FFFF"
    outlines [ (absolute(1), "#000A", absolute(0), absolute(0)) ]
    hover_xoffset 20


screen gallery():
    add gui.game_menu_background
    label _("Character Gallery") xpos 10 ypos 10 style "taskline_label"
    vbox:
        style_prefix "gallery_nav"

        imagebutton "gui/button/Reina_hovered.webp" action Show("gallery_a")
        imagebutton "gui/button/Jenni_hovered.webp" action Show("gallery_b")
        imagebutton "gui/button/Camilla_hovered.webp" action Show("gallery_c")
        imagebutton "gui/button/Briana_hovered.webp" action Show("gallery_d")
        imagebutton "gui/button/Penny_hovered.webp" action Show ("gallery_e")
        imagebutton "gui/button/Rose_hovered.webp" action Show("gallery_f")
        imagebutton "gui/button/Aisha_hovered.webp" action Show ("gallery_g")
        imagebutton "gui/button/Sabrina_hovered.webp" action Show ("gallery_h")
        imagebutton "gui/button/Miyuki_hovered.webp" action Show("gallery_i")
        imagebutton "gui/button/Videos_hovered.webp" action Show ("gallery_j")

    textbutton _("Return") action [Return(), Hide("gallery")] xalign 0.97 yalign 0.95
#
# #Reina
screen gallery_a():
    default cg_page_a = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        textbutton _("2") action SetLocalVariable("cg_page_a", 2)
        textbutton _("3") action SetLocalVariable("cg_page_a", 3)
        textbutton _("4") action SetLocalVariable("cg_page_a", 4)
        textbutton _("5") action SetLocalVariable("cg_page_a", 5)
        showif cg_page_a == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_reinagallery01","images/thumbnails/reina01.webp")
                add g.make_button("cg_reinagallery02","images/thumbnails/reina02.webp")
                add g.make_button("cg_reinagallery03","images/thumbnails/reina03.webp")
                add g.make_button("cg_reinagallery04","images/thumbnails/reina04.webp")
                add g.make_button("cg_reinagallery05","images/thumbnails/reina05.webp")
                add g.make_button("cg_reinagallery06","images/thumbnails/reina06.webp")
                add g.make_button("cg_reinagallery07","images/thumbnails/reina07.webp")
                add g.make_button("cg_reinagallery08","images/thumbnails/reina08.webp")
                add g.make_button("cg_reinagallery09","images/thumbnails/reina09.webp")
                add g.make_button("cg_reinagallery10","images/thumbnails/reina10.webp")
                null
                null
        showif cg_page_a == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_reinagallery11","images/thumbnails/reina11.webp")
                add g.make_button("cg_reinagallery12","images/thumbnails/reina12.webp")
                add g.make_button("cg_reinagallery13","images/thumbnails/reina13.webp")
                add g.make_button("cg_reinagallery14","images/thumbnails/reina14.webp")
                add g.make_button("cg_reinagallery15","images/thumbnails/reina15.webp")
                add g.make_button("cg_reinagallery16","images/thumbnails/reina16.webp")
                add g.make_button("cg_reinagallery17","images/thumbnails/reina17.webp")
                add g.make_button("cg_reinagallery18","images/thumbnails/reina18.webp")
                add g.make_button("cg_reinagallery19","images/thumbnails/reina19.webp")
                add g.make_button("cg_reinagallery20","images/thumbnails/reina20.webp")
                null
                null
        showif cg_page_a == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_reinagallery21","images/thumbnails/reina21.webp")
                add g.make_button("cg_reinagallery22","images/thumbnails/reina22.webp")
                add g.make_button("cg_reinagallery23","images/thumbnails/reina23.webp")
                add g.make_button("cg_reinagallery24","images/thumbnails/reina24.webp")
                add g.make_button("cg_reinagallery25","images/thumbnails/reina25.webp")
                add g.make_button("cg_reinagallery26","images/thumbnails/reina26.webp")
                add g.make_button("cg_reinagallery27","images/thumbnails/reina27.webp")
                add g.make_button("cg_reinagallery28","images/thumbnails/reina28.webp")
                add g.make_button("cg_reinagallery29","images/thumbnails/reina29.webp")
                add g.make_button("cg_reinagallery30","images/thumbnails/reina30.webp")
                null
                null
        showif cg_page_a == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_reinagallery31","images/thumbnails/reina31.webp")
                add g.make_button("cg_reinagallery32","images/thumbnails/reina32.webp")
                add g.make_button("cg_reinagallery33","images/thumbnails/reina33.webp")
                add g.make_button("cg_reinagallery34","images/thumbnails/reina34.webp")
                add g.make_button("cg_reinagallery35","images/thumbnails/reina35.webp")
                add g.make_button("cg_reinagallery36","images/thumbnails/reina36.webp")
                add g.make_button("cg_reinagallery37","images/thumbnails/reina37.webp")
                add g.make_button("cg_reinagallery38","images/thumbnails/reina38.webp")
                add g.make_button("cg_reinagallery39","images/thumbnails/reina39.webp")
                add g.make_button("cg_reinagallery40","images/thumbnails/reina40.webp")
                null
                null
        showif cg_page_a == 5:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_reinagallery41","images/thumbnails/reina41.webp")
                add g.make_button("cg_reinagallery42","images/thumbnails/reina42.webp")
                add g.make_button("cg_reinagallery43","images/thumbnails/reina43.webp")
                add g.make_button("cg_reinagallery44","images/thumbnails/reina44.webp")
                add g.make_button("cg_reinagallery45","images/thumbnails/reina45.webp")
                add g.make_button("cg_reinagallery46","images/thumbnails/reina46.webp")
                add g.make_button("cg_reinagallery47","images/thumbnails/reina47.webp")
                add g.make_button("cg_reinagallery48","images/thumbnails/reina48.webp")
                add g.make_button("cg_reinagallery49","images/thumbnails/reina49.webp")
                add g.make_button("cg_reinagallery50","images/thumbnails/reina50.webp")
                add g.make_button("cg_reinagallery51","images/thumbnails/reina51.webp")
                null
#Jenni
screen gallery_b():
    default cg_page_b = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_b", 1)
        textbutton _("2") action SetLocalVariable("cg_page_b", 2)
        textbutton _("3") action SetLocalVariable("cg_page_b", 3)
        textbutton _("4") action SetLocalVariable("cg_page_b", 4)
        textbutton _("5") action SetLocalVariable("cg_page_b", 5)

        showif cg_page_b == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_jennigallery01","images/thumbnails/jenni01.webp")
                add g.make_button("cg_jennigallery02","images/thumbnails/jenni02.webp")
                add g.make_button("cg_jennigallery03","images/thumbnails/jenni03.webp")
                add g.make_button("cg_jennigallery04","images/thumbnails/jenni04.webp")
                add g.make_button("cg_jennigallery05","images/thumbnails/jenni05.webp")
                add g.make_button("cg_jennigallery06","images/thumbnails/jenni06.webp")
                add g.make_button("cg_jennigallery07","images/thumbnails/jenni07.webp")
                add g.make_button("cg_jennigallery08","images/thumbnails/jenni08.webp")
                add g.make_button("cg_jennigallery09","images/thumbnails/jenni09.webp")
                add g.make_button("cg_jennigallery10","images/thumbnails/jenni10.webp")
                null
                null
        showif cg_page_b == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_jennigallery11","images/thumbnails/jenni11.webp")
                add g.make_button("cg_jennigallery12","images/thumbnails/jenni12.webp")
                add g.make_button("cg_jennigallery13","images/thumbnails/jenni13.webp")
                add g.make_button("cg_jennigallery14","images/thumbnails/jenni14.webp")
                add g.make_button("cg_jennigallery15","images/thumbnails/jenni15.webp")
                add g.make_button("cg_jennigallery16","images/thumbnails/jenni16.webp")
                add g.make_button("cg_jennigallery17","images/thumbnails/jenni17.webp")
                add g.make_button("cg_jennigallery18","images/thumbnails/jenni18.webp")
                add g.make_button("cg_jennigallery19","images/thumbnails/jenni19.webp")
                add g.make_button("cg_jennigallery20","images/thumbnails/jenni20.webp")
                null
                null
        showif cg_page_b == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_jennigallery21","images/thumbnails/jenni21.webp")
                add g.make_button("cg_jennigallery22","images/thumbnails/jenni22.webp")
                add g.make_button("cg_jennigallery23","images/thumbnails/jenni23.webp")
                add g.make_button("cg_jennigallery24","images/thumbnails/jenni24.webp")
                add g.make_button("cg_jennigallery25","images/thumbnails/jenni25.webp")
                add g.make_button("cg_jennigallery26","images/thumbnails/jenni26.webp")
                add g.make_button("cg_jennigallery27","images/thumbnails/jenni27.webp")
                add g.make_button("cg_jennigallery28","images/thumbnails/jenni28.webp")
                add g.make_button("cg_jennigallery29","images/thumbnails/jenni29.webp")
                add g.make_button("cg_jennigallery30","images/thumbnails/jenni30.webp")
                null
                null
        showif cg_page_b == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_jennigallery31","images/thumbnails/jenni31.webp")
                add g.make_button("cg_jennigallery32","images/thumbnails/jenni32.webp")
                add g.make_button("cg_jennigallery33","images/thumbnails/jenni33.webp")
                add g.make_button("cg_jennigallery34","images/thumbnails/jenni34.webp")
                add g.make_button("cg_jennigallery35","images/thumbnails/jenni35.webp")
                add g.make_button("cg_jennigallery36","images/thumbnails/jenni36.webp")
                add g.make_button("cg_jennigallery37","images/thumbnails/jenni37.webp")
                add g.make_button("cg_jennigallery38","images/thumbnails/jenni38.webp")
                add g.make_button("cg_jennigallery39","images/thumbnails/jenni39.webp")
                add g.make_button("cg_jennigallery40","images/thumbnails/jenni40.webp")
                null
                null
        showif cg_page_b == 5:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_jennigallery41","images/thumbnails/jenni41.webp")
                add g.make_button("cg_jennigallery42","images/thumbnails/jenni42.webp")
                add g.make_button("cg_jennigallery43","images/thumbnails/jenni43.webp")
                add g.make_button("cg_jennigallery44","images/thumbnails/jenni44.webp")
                add g.make_button("cg_jennigallery45","images/thumbnails/jenni45.webp")
                add g.make_button("cg_jennigallery46","images/thumbnails/jenni46.webp")
                add g.make_button("cg_jennigallery47","images/thumbnails/jenni47.webp")
                add g.make_button("cg_jennigallery48","images/thumbnails/jenni48.webp")
                add g.make_button("cg_jennigallery49","images/thumbnails/jenni49.webp")
                add g.make_button("cg_jennigallery50","images/thumbnails/jenni50.webp")
                null
                null


#Camilla
screen gallery_c():

    default cg_page_c = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_c", 1)
        textbutton _("2") action SetLocalVariable("cg_page_c", 2)
        textbutton _("3") action SetLocalVariable("cg_page_c", 3)
        textbutton _("4") action SetLocalVariable("cg_page_c", 4)
        textbutton _("5") action SetLocalVariable("cg_page_c", 5)

        showif cg_page_c == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_camillagallery01","images/thumbnails/camilla01.webp")
                add g.make_button("cg_camillagallery02","images/thumbnails/camilla02.webp")
                add g.make_button("cg_camillagallery03","images/thumbnails/camilla03.webp")
                add g.make_button("cg_camillagallery04","images/thumbnails/camilla04.webp")
                add g.make_button("cg_camillagallery05","images/thumbnails/camilla05.webp")
                add g.make_button("cg_camillagallery06","images/thumbnails/camilla06.webp")
                add g.make_button("cg_camillagallery07","images/thumbnails/camilla07.webp")
                add g.make_button("cg_camillagallery08","images/thumbnails/camilla08.webp")
                add g.make_button("cg_camillagallery09","images/thumbnails/camilla09.webp")
                add g.make_button("cg_camillagallery10","images/thumbnails/camilla10.webp")
                null
                null
        showif cg_page_c == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_camillagallery11","images/thumbnails/camilla11.webp")
                add g.make_button("cg_camillagallery12","images/thumbnails/camilla12.webp")
                add g.make_button("cg_camillagallery13","images/thumbnails/camilla13.webp")
                add g.make_button("cg_camillagallery14","images/thumbnails/camilla14.webp")
                add g.make_button("cg_camillagallery15","images/thumbnails/camilla15.webp")
                add g.make_button("cg_camillagallery16","images/thumbnails/camilla16.webp")
                add g.make_button("cg_camillagallery17","images/thumbnails/camilla17.webp")
                add g.make_button("cg_camillagallery18","images/thumbnails/camilla18.webp")
                add g.make_button("cg_camillagallery19","images/thumbnails/camilla19.webp")
                add g.make_button("cg_camillagallery20","images/thumbnails/camilla20.webp")
                null
                null
        showif cg_page_c == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_camillagallery21","images/thumbnails/camilla21.webp")
                add g.make_button("cg_camillagallery22","images/thumbnails/camilla22.webp")
                add g.make_button("cg_camillagallery23","images/thumbnails/camilla23.webp")
                add g.make_button("cg_camillagallery24","images/thumbnails/camilla24.webp")
                add g.make_button("cg_camillagallery25","images/thumbnails/camilla25.webp")
                add g.make_button("cg_camillagallery26","images/thumbnails/camilla26.webp")
                add g.make_button("cg_camillagallery27","images/thumbnails/camilla27.webp")
                add g.make_button("cg_camillagallery28","images/thumbnails/camilla28.webp")
                add g.make_button("cg_camillagallery29","images/thumbnails/camilla29.webp")
                add g.make_button("cg_camillagallery30","images/thumbnails/camilla30.webp")
                null
                null
        showif cg_page_c == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_camillagallery31","images/thumbnails/camilla31.webp")
                add g.make_button("cg_camillagallery32","images/thumbnails/camilla32.webp")
                add g.make_button("cg_camillagallery33","images/thumbnails/camilla33.webp")
                add g.make_button("cg_camillagallery34","images/thumbnails/camilla34.webp")
                add g.make_button("cg_camillagallery35","images/thumbnails/camilla35.webp")
                add g.make_button("cg_camillagallery36","images/thumbnails/camilla36.webp")
                add g.make_button("cg_camillagallery37","images/thumbnails/camilla37.webp")
                add g.make_button("cg_camillagallery38","images/thumbnails/camilla38.webp")
                add g.make_button("cg_camillagallery39","images/thumbnails/camilla39.webp")
                add g.make_button("cg_camillagallery40","images/thumbnails/camilla40.webp")
                null
                null
        showif cg_page_c == 5:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_camillagallery41","images/thumbnails/camilla41.webp")
                null
                null
                null
                null
                null
                null
                null
                null
                null


#Briana
screen gallery_d():

    default cg_page_d = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_d", 1)
        textbutton _("2") action SetLocalVariable("cg_page_d", 2)
        textbutton _("3") action SetLocalVariable("cg_page_d", 3)
        textbutton _("4") action SetLocalVariable("cg_page_d", 4)
        textbutton _("5") action SetLocalVariable("cg_page_d", 5)

        showif cg_page_d == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_brianagallery01","images/thumbnails/briana01.webp")
                add g.make_button("cg_brianagallery02","images/thumbnails/briana02.webp")
                add g.make_button("cg_brianagallery03","images/thumbnails/briana03.webp")
                add g.make_button("cg_brianagallery04","images/thumbnails/briana04.webp")
                add g.make_button("cg_brianagallery05","images/thumbnails/briana05.webp")
                add g.make_button("cg_brianagallery06","images/thumbnails/briana06.webp")
                add g.make_button("cg_brianagallery07","images/thumbnails/briana07.webp")
                add g.make_button("cg_brianagallery08","images/thumbnails/briana08.webp")
                add g.make_button("cg_brianagallery09","images/thumbnails/briana09.webp")
                add g.make_button("cg_brianagallery10","images/thumbnails/briana10.webp")
                null
                null
        showif cg_page_d == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_brianagallery11","images/thumbnails/briana11.webp")
                add g.make_button("cg_brianagallery12","images/thumbnails/briana12.webp")
                add g.make_button("cg_brianagallery13","images/thumbnails/briana13.webp")
                add g.make_button("cg_brianagallery14","images/thumbnails/briana14.webp")
                add g.make_button("cg_brianagallery15","images/thumbnails/briana15.webp")
                add g.make_button("cg_brianagallery16","images/thumbnails/briana16.webp")
                add g.make_button("cg_brianagallery17","images/thumbnails/briana17.webp")
                add g.make_button("cg_brianagallery18","images/thumbnails/briana18.webp")
                add g.make_button("cg_brianagallery19","images/thumbnails/briana19.webp")
                add g.make_button("cg_brianagallery20","images/thumbnails/briana20.webp")
                null
                null
        showif cg_page_d == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_brianagallery21","images/thumbnails/briana21.webp")
                add g.make_button("cg_brianagallery22","images/thumbnails/briana22.webp")
                add g.make_button("cg_brianagallery23","images/thumbnails/briana23.webp")
                add g.make_button("cg_brianagallery24","images/thumbnails/briana24.webp")
                add g.make_button("cg_brianagallery25","images/thumbnails/briana25.webp")
                add g.make_button("cg_brianagallery26","images/thumbnails/briana26.webp")
                add g.make_button("cg_brianagallery27","images/thumbnails/briana27.webp")
                add g.make_button("cg_brianagallery28","images/thumbnails/briana28.webp")
                add g.make_button("cg_brianagallery29","images/thumbnails/briana29.webp")
                add g.make_button("cg_brianagallery30","images/thumbnails/briana30.webp")
                null
                null
        showif cg_page_d == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_brianagallery31","images/thumbnails/briana31.webp")
                add g.make_button("cg_brianagallery32","images/thumbnails/briana32.webp")
                add g.make_button("cg_brianagallery33","images/thumbnails/briana33.webp")
                add g.make_button("cg_brianagallery34","images/thumbnails/briana34.webp")
                add g.make_button("cg_brianagallery35","images/thumbnails/briana35.webp")
                add g.make_button("cg_brianagallery36","images/thumbnails/briana36.webp")
                add g.make_button("cg_brianagallery37","images/thumbnails/briana37.webp")
                add g.make_button("cg_brianagallery38","images/thumbnails/briana38.webp")
                add g.make_button("cg_brianagallery39","images/thumbnails/briana39.webp")
                add g.make_button("cg_brianagallery40","images/thumbnails/briana40.webp")
                null
                null
        showif cg_page_d == 5:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_brianagallery41","images/thumbnails/briana41.webp")
                add g.make_button("cg_brianagallery42","images/thumbnails/briana42.webp")
                add g.make_button("cg_brianagallery43","images/thumbnails/briana43.webp")
                add g.make_button("cg_brianagallery44","images/thumbnails/briana44.webp")
                add g.make_button("cg_brianagallery45","images/thumbnails/briana45.webp")
                add g.make_button("cg_brianagallery46","images/thumbnails/briana46.webp")
                add g.make_button("cg_brianagallery47","images/thumbnails/briana47.webp")
                add g.make_button("cg_brianagallery48","images/thumbnails/briana48.webp")
                add g.make_button("cg_brianagallery49","images/thumbnails/briana49.webp")
                add g.make_button("cg_brianagallery50","images/thumbnails/briana50.webp")
                null
                null


#Penny
screen gallery_e():

    default cg_page_e = 1
    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_e", 1)
        textbutton _("2") action SetLocalVariable("cg_page_e", 2)
        textbutton _("3") action SetLocalVariable("cg_page_e", 3)
        textbutton _("4") action SetLocalVariable("cg_page_e", 4)
        textbutton _("5") action SetLocalVariable("cg_page_e", 5)

        showif cg_page_e == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_pennygallery01","images/thumbnails/penny01.webp")
                add g.make_button("cg_pennygallery02","images/thumbnails/penny02.webp")
                add g.make_button("cg_pennygallery03","images/thumbnails/penny03.webp")
                add g.make_button("cg_pennygallery04","images/thumbnails/penny04.webp")
                add g.make_button("cg_pennygallery05","images/thumbnails/penny05.webp")
                add g.make_button("cg_pennygallery06","images/thumbnails/penny06.webp")
                add g.make_button("cg_pennygallery07","images/thumbnails/penny07.webp")
                add g.make_button("cg_pennygallery08","images/thumbnails/penny08.webp")
                add g.make_button("cg_pennygallery09","images/thumbnails/penny09.webp")
                add g.make_button("cg_pennygallery10","images/thumbnails/penny10.webp")
                null
                null
        showif cg_page_e == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_pennygallery11","images/thumbnails/penny11.webp")
                add g.make_button("cg_pennygallery12","images/thumbnails/penny12.webp")
                add g.make_button("cg_pennygallery13","images/thumbnails/penny13.webp")
                add g.make_button("cg_pennygallery14","images/thumbnails/penny14.webp")
                add g.make_button("cg_pennygallery15","images/thumbnails/penny15.webp")
                add g.make_button("cg_pennygallery16","images/thumbnails/penny16.webp")
                add g.make_button("cg_pennygallery17","images/thumbnails/penny17.webp")
                add g.make_button("cg_pennygallery18","images/thumbnails/penny18.webp")
                add g.make_button("cg_pennygallery19","images/thumbnails/penny19.webp")
                add g.make_button("cg_pennygallery20","images/thumbnails/penny20.webp")
                null
                null
        showif cg_page_e == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_pennygallery21","images/thumbnails/penny21.webp")
                add g.make_button("cg_pennygallery22","images/thumbnails/penny22.webp")
                add g.make_button("cg_pennygallery23","images/thumbnails/penny23.webp")
                add g.make_button("cg_pennygallery24","images/thumbnails/penny24.webp")
                add g.make_button("cg_pennygallery25","images/thumbnails/penny25.webp")
                add g.make_button("cg_pennygallery26","images/thumbnails/penny26.webp")
                add g.make_button("cg_pennygallery27","images/thumbnails/penny27.webp")
                add g.make_button("cg_pennygallery28","images/thumbnails/penny28.webp")
                add g.make_button("cg_pennygallery29","images/thumbnails/penny29.webp")
                add g.make_button("cg_pennygallery30","images/thumbnails/penny30.webp")
                null
                null
        showif cg_page_e == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_pennygallery31","images/thumbnails/penny31.webp")
                add g.make_button("cg_pennygallery32","images/thumbnails/penny32.webp")
                add g.make_button("cg_pennygallery33","images/thumbnails/penny33.webp")
                add g.make_button("cg_pennygallery34","images/thumbnails/penny34.webp")
                add g.make_button("cg_pennygallery35","images/thumbnails/penny35.webp")
                add g.make_button("cg_pennygallery36","images/thumbnails/penny36.webp")
                add g.make_button("cg_pennygallery37","images/thumbnails/penny37.webp")
                add g.make_button("cg_pennygallery38","images/thumbnails/penny38.webp")
                add g.make_button("cg_pennygallery39","images/thumbnails/penny39.webp")
                add g.make_button("cg_pennygallery40","images/thumbnails/penny40.webp")
                null
                null
        showif cg_page_e == 5:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_pennygallery41","images/thumbnails/penny41.webp")
                add g.make_button("cg_pennygallery42","images/thumbnails/penny42.webp")
                null
                null
                null
                null
                null
                null
                null
                null
                null
                null
#Rose
screen gallery_f():
    default cg_page_f = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_f", 1)
        textbutton _("2") action SetLocalVariable("cg_page_f", 2)
        textbutton _("3") action SetLocalVariable("cg_page_f", 3)
        textbutton _("4") action SetLocalVariable("cg_page_f", 4)
        showif cg_page_f == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_rosegallery01","images/thumbnails/rose01.webp")
                add g.make_button("cg_rosegallery02","images/thumbnails/rose02.webp")
                add g.make_button("cg_rosegallery03","images/thumbnails/rose03.webp")
                add g.make_button("cg_rosegallery04","images/thumbnails/rose04.webp")
                add g.make_button("cg_rosegallery05","images/thumbnails/rose05.webp")
                add g.make_button("cg_rosegallery06","images/thumbnails/rose06.webp")
                add g.make_button("cg_rosegallery07","images/thumbnails/rose07.webp")
                add g.make_button("cg_rosegallery08","images/thumbnails/rose08.webp")
                add g.make_button("cg_rosegallery09","images/thumbnails/rose09.webp")
                add g.make_button("cg_rosegallery10","images/thumbnails/rose10.webp")
                null
                null
        showif cg_page_f == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_rosegallery11","images/thumbnails/rose11.webp")
                add g.make_button("cg_rosegallery12","images/thumbnails/rose12.webp")
                add g.make_button("cg_rosegallery13","images/thumbnails/rose13.webp")
                add g.make_button("cg_rosegallery14","images/thumbnails/rose14.webp")
                add g.make_button("cg_rosegallery15","images/thumbnails/rose15.webp")
                add g.make_button("cg_rosegallery16","images/thumbnails/rose16.webp")
                add g.make_button("cg_rosegallery17","images/thumbnails/rose17.webp")
                add g.make_button("cg_rosegallery18","images/thumbnails/rose18.webp")
                add g.make_button("cg_rosegallery19","images/thumbnails/rose19.webp")
                add g.make_button("cg_rosegallery20","images/thumbnails/rose20.webp")
                null
                null
        showif cg_page_f == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_rosegallery21","images/thumbnails/rose21.webp")
                add g.make_button("cg_rosegallery22","images/thumbnails/rose22.webp")
                add g.make_button("cg_rosegallery23","images/thumbnails/rose23.webp")
                add g.make_button("cg_rosegallery24","images/thumbnails/rose24.webp")
                add g.make_button("cg_rosegallery25","images/thumbnails/rose25.webp")
                add g.make_button("cg_rosegallery26","images/thumbnails/rose26.webp")
                add g.make_button("cg_rosegallery27","images/thumbnails/rose27.webp")
                add g.make_button("cg_rosegallery28","images/thumbnails/rose28.webp")
                add g.make_button("cg_rosegallery29","images/thumbnails/rose29.webp")
                add g.make_button("cg_rosegallery30","images/thumbnails/rose30.webp")
                null
                null
        showif cg_page_f == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_rosegallery31","images/thumbnails/rose31.webp")
                add g.make_button("cg_rosegallery32","images/thumbnails/rose32.webp")
                add g.make_button("cg_rosegallery33","images/thumbnails/rose33.webp")
                add g.make_button("cg_rosegallery34","images/thumbnails/rose34.webp")
                add g.make_button("cg_rosegallery35","images/thumbnails/rose35.webp")
                add g.make_button("cg_rosegallery36","images/thumbnails/rose36.webp")
                add g.make_button("cg_rosegallery37","images/thumbnails/rose37.webp")
                add g.make_button("cg_rosegallery38","images/thumbnails/rose38.webp")
                add g.make_button("cg_rosegallery39","images/thumbnails/rose39.webp")
                add g.make_button("cg_rosegallery40","images/thumbnails/rose40.webp")
                null
                null
#Aisha
screen gallery_g():
    default cg_page_g = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_g", 1)
        textbutton _("2") action SetLocalVariable("cg_page_g", 2)
        textbutton _("3") action SetLocalVariable("cg_page_g", 3)
        textbutton _("4") action SetLocalVariable("cg_page_g", 4)
        textbutton _("5") action SetLocalVariable("cg_page_g", 5)

        showif cg_page_g == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_aishagallery01","images/thumbnails/aisha01.webp")
                add g.make_button("cg_aishagallery02","images/thumbnails/aisha02.webp")
                add g.make_button("cg_aishagallery03","images/thumbnails/aisha03.webp")
                add g.make_button("cg_aishagallery04","images/thumbnails/aisha04.webp")
                add g.make_button("cg_aishagallery05","images/thumbnails/aisha05.webp")
                add g.make_button("cg_aishagallery06","images/thumbnails/aisha06.webp")
                add g.make_button("cg_aishagallery07","images/thumbnails/aisha07.webp")
                add g.make_button("cg_aishagallery08","images/thumbnails/aisha08.webp")
                add g.make_button("cg_aishagallery09","images/thumbnails/aisha09.webp")
                add g.make_button("cg_aishagallery10","images/thumbnails/aisha10.webp")
                null
                null
        showif cg_page_g == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_aishagallery11","images/thumbnails/aisha11.webp")
                add g.make_button("cg_aishagallery12","images/thumbnails/aisha12.webp")
                add g.make_button("cg_aishagallery13","images/thumbnails/aisha13.webp")
                add g.make_button("cg_aishagallery14","images/thumbnails/aisha14.webp")
                add g.make_button("cg_aishagallery15","images/thumbnails/aisha15.webp")
                add g.make_button("cg_aishagallery16","images/thumbnails/aisha16.webp")
                add g.make_button("cg_aishagallery17","images/thumbnails/aisha17.webp")
                add g.make_button("cg_aishagallery18","images/thumbnails/aisha18.webp")
                add g.make_button("cg_aishagallery19","images/thumbnails/aisha19.webp")
                add g.make_button("cg_aishagallery20","images/thumbnails/aisha20.webp")
                null
                null
        showif cg_page_g == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_aishagallery21","images/thumbnails/aisha21.webp")
                add g.make_button("cg_aishagallery22","images/thumbnails/aisha22.webp")
                add g.make_button("cg_aishagallery23","images/thumbnails/aisha23.webp")
                add g.make_button("cg_aishagallery24","images/thumbnails/aisha24.webp")
                add g.make_button("cg_aishagallery25","images/thumbnails/aisha25.webp")
                add g.make_button("cg_aishagallery26","images/thumbnails/aisha26.webp")
                add g.make_button("cg_aishagallery27","images/thumbnails/aisha27.webp")
                add g.make_button("cg_aishagallery28","images/thumbnails/aisha28.webp")
                add g.make_button("cg_aishagallery29","images/thumbnails/aisha29.webp")
                add g.make_button("cg_aishagallery30","images/thumbnails/aisha30.webp")
                null
                null
        showif cg_page_g == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_aishagallery31","images/thumbnails/aisha31.webp")
                add g.make_button("cg_aishagallery32","images/thumbnails/aisha32.webp")
                add g.make_button("cg_aishagallery33","images/thumbnails/aisha33.webp")
                add g.make_button("cg_aishagallery34","images/thumbnails/aisha34.webp")
                add g.make_button("cg_aishagallery35","images/thumbnails/aisha35.webp")
                add g.make_button("cg_aishagallery36","images/thumbnails/aisha36.webp")
                add g.make_button("cg_aishagallery37","images/thumbnails/aisha37.webp")
                add g.make_button("cg_aishagallery38","images/thumbnails/aisha38.webp")
                add g.make_button("cg_aishagallery39","images/thumbnails/aisha39.webp")
                add g.make_button("cg_aishagallery40","images/thumbnails/aisha40.webp")
                null
                null
        showif cg_page_g == 5:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_aishagallery41","images/thumbnails/aisha41.webp")
                add g.make_button("cg_aishagallery42","images/thumbnails/aisha42.webp")
                null
                null
                null
                null
                null
                null
                null
                null
                null
                null
#Sabrina
screen gallery_h():
    default cg_page_h = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_h", 1)
        textbutton _("2") action SetLocalVariable("cg_page_h", 2)
        textbutton _("3") action SetLocalVariable("cg_page_h", 3)
        textbutton _("4") action SetLocalVariable("cg_page_h", 4)
        textbutton _("5") action SetLocalVariable("cg_page_h", 5)

        showif cg_page_h == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_sabrinagallery01","images/thumbnails/sabrina01.webp")
                add g.make_button("cg_sabrinagallery02","images/thumbnails/sabrina02.webp")
                add g.make_button("cg_sabrinagallery03","images/thumbnails/sabrina03.webp")
                add g.make_button("cg_sabrinagallery04","images/thumbnails/sabrina04.webp")
                add g.make_button("cg_sabrinagallery05","images/thumbnails/sabrina05.webp")
                add g.make_button("cg_sabrinagallery06","images/thumbnails/sabrina06.webp")
                add g.make_button("cg_sabrinagallery07","images/thumbnails/sabrina07.webp")
                add g.make_button("cg_sabrinagallery08","images/thumbnails/sabrina08.webp")
                add g.make_button("cg_sabrinagallery09","images/thumbnails/sabrina09.webp")
                add g.make_button("cg_sabrinagallery10","images/thumbnails/sabrina10.webp")
                null
                null
        showif cg_page_h == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_sabrinagallery11","images/thumbnails/sabrina11.webp")
                add g.make_button("cg_sabrinagallery12","images/thumbnails/sabrina12.webp")
                add g.make_button("cg_sabrinagallery13","images/thumbnails/sabrina13.webp")
                add g.make_button("cg_sabrinagallery14","images/thumbnails/sabrina14.webp")
                add g.make_button("cg_sabrinagallery15","images/thumbnails/sabrina15.webp")
                add g.make_button("cg_sabrinagallery16","images/thumbnails/sabrina16.webp")
                add g.make_button("cg_sabrinagallery17","images/thumbnails/sabrina17.webp")
                add g.make_button("cg_sabrinagallery18","images/thumbnails/sabrina18.webp")
                add g.make_button("cg_sabrinagallery19","images/thumbnails/sabrina19.webp")
                add g.make_button("cg_sabrinagallery20","images/thumbnails/sabrina20.webp")
                null
                null
        showif cg_page_h == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_sabrinagallery21","images/thumbnails/sabrina21.webp")
                add g.make_button("cg_sabrinagallery22","images/thumbnails/sabrina22.webp")
                add g.make_button("cg_sabrinagallery23","images/thumbnails/sabrina23.webp")
                add g.make_button("cg_sabrinagallery24","images/thumbnails/sabrina24.webp")
                add g.make_button("cg_sabrinagallery25","images/thumbnails/sabrina25.webp")
                add g.make_button("cg_sabrinagallery26","images/thumbnails/sabrina26.webp")
                add g.make_button("cg_sabrinagallery27","images/thumbnails/sabrina27.webp")
                add g.make_button("cg_sabrinagallery28","images/thumbnails/sabrina28.webp")
                add g.make_button("cg_sabrinagallery29","images/thumbnails/sabrina29.webp")
                add g.make_button("cg_sabrinagallery30","images/thumbnails/sabrina30.webp")
                null
                null
        showif cg_page_h == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_sabrinagallery31","images/thumbnails/sabrina31.webp")
                add g.make_button("cg_sabrinagallery32","images/thumbnails/sabrina32.webp")
                add g.make_button("cg_sabrinagallery33","images/thumbnails/sabrina33.webp")
                add g.make_button("cg_sabrinagallery34","images/thumbnails/sabrina34.webp")
                add g.make_button("cg_sabrinagallery35","images/thumbnails/sabrina35.webp")
                add g.make_button("cg_sabrinagallery36","images/thumbnails/sabrina36.webp")
                add g.make_button("cg_sabrinagallery37","images/thumbnails/sabrina37.webp")
                add g.make_button("cg_sabrinagallery38","images/thumbnails/sabrina38.webp")
                add g.make_button("cg_sabrinagallery39","images/thumbnails/sabrina39.webp")
                add g.make_button("cg_sabrinagallery40","images/thumbnails/sabrina40.webp")
                add g.make_button("cg_sabrinagallery53","images/thumbnails/sabrina53.webp")
                null
        showif cg_page_h == 5:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_sabrinagallery41","images/thumbnails/sabrina41.webp")
                add g.make_button("cg_sabrinagallery42","images/thumbnails/sabrina42.webp")
                add g.make_button("cg_sabrinagallery43","images/thumbnails/sabrina43.webp")
                add g.make_button("cg_sabrinagallery44","images/thumbnails/sabrina44.webp")
                add g.make_button("cg_sabrinagallery45","images/thumbnails/sabrina45.webp")
                add g.make_button("cg_sabrinagallery46","images/thumbnails/sabrina46.webp")
                add g.make_button("cg_sabrinagallery47","images/thumbnails/sabrina47.webp")
                add g.make_button("cg_sabrinagallery48","images/thumbnails/sabrina48.webp")
                add g.make_button("cg_sabrinagallery49","images/thumbnails/sabrina49.webp")
                add g.make_button("cg_sabrinagallery50","images/thumbnails/sabrina50.webp")
                add g.make_button("cg_sabrinagallery51","images/thumbnails/sabrina51.webp")
                add g.make_button("cg_sabrinagallery52","images/thumbnails/sabrina52.webp")
#Miyuki
screen gallery_i():
    default cg_page_i = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_i", 1)
        textbutton _("2") action SetLocalVariable("cg_page_i", 2)
        textbutton _("3") action SetLocalVariable("cg_page_i", 3)
        textbutton _("4") action SetLocalVariable("cg_page_i", 4)
        textbutton _("5") action SetLocalVariable("cg_page_i", 5)
        showif cg_page_i == 1:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_miyukigallery01","images/thumbnails/miyuki01.webp")
                add g.make_button("cg_miyukigallery02","images/thumbnails/miyuki02.webp")
                add g.make_button("cg_miyukigallery03","images/thumbnails/miyuki03.webp")
                add g.make_button("cg_miyukigallery04","images/thumbnails/miyuki04.webp")
                add g.make_button("cg_miyukigallery05","images/thumbnails/miyuki05.webp")
                add g.make_button("cg_miyukigallery06","images/thumbnails/miyuki06.webp")
                add g.make_button("cg_miyukigallery07","images/thumbnails/miyuki07.webp")
                add g.make_button("cg_miyukigallery08","images/thumbnails/miyuki08.webp")
                add g.make_button("cg_miyukigallery09","images/thumbnails/miyuki09.webp")
                add g.make_button("cg_miyukigallery10","images/thumbnails/miyuki10.webp")
                null
                null
        showif cg_page_i == 2:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_miyukigallery11","images/thumbnails/miyuki11.webp")
                add g.make_button("cg_miyukigallery12","images/thumbnails/miyuki12.webp")
                add g.make_button("cg_miyukigallery13","images/thumbnails/miyuki13.webp")
                add g.make_button("cg_miyukigallery14","images/thumbnails/miyuki14.webp")
                add g.make_button("cg_miyukigallery15","images/thumbnails/miyuki15.webp")
                add g.make_button("cg_miyukigallery16","images/thumbnails/miyuki16.webp")
                add g.make_button("cg_miyukigallery17","images/thumbnails/miyuki17.webp")
                add g.make_button("cg_miyukigallery18","images/thumbnails/miyuki18.webp")
                add g.make_button("cg_miyukigallery19","images/thumbnails/miyuki19.webp")
                add g.make_button("cg_miyukigallery20","images/thumbnails/miyuki20.webp")
                null
                null
        showif cg_page_i == 3:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_miyukigallery21","images/thumbnails/miyuki21.webp")
                add g.make_button("cg_miyukigallery22","images/thumbnails/miyuki22.webp")
                add g.make_button("cg_miyukigallery23","images/thumbnails/miyuki23.webp")
                add g.make_button("cg_miyukigallery24","images/thumbnails/miyuki24.webp")
                add g.make_button("cg_miyukigallery25","images/thumbnails/miyuki25.webp")
                add g.make_button("cg_miyukigallery26","images/thumbnails/miyuki26.webp")
                add g.make_button("cg_miyukigallery27","images/thumbnails/miyuki27.webp")
                add g.make_button("cg_miyukigallery28","images/thumbnails/miyuki28.webp")
                add g.make_button("cg_miyukigallery29","images/thumbnails/miyuki29.webp")
                add g.make_button("cg_miyukigallery30","images/thumbnails/miyuki30.webp")
                null
                null
        showif cg_page_i == 4:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_miyukigallery31","images/thumbnails/miyuki31.webp")
                add g.make_button("cg_miyukigallery32","images/thumbnails/miyuki32.webp")
                add g.make_button("cg_miyukigallery33","images/thumbnails/miyuki33.webp")
                add g.make_button("cg_miyukigallery34","images/thumbnails/miyuki34.webp")
                add g.make_button("cg_miyukigallery35","images/thumbnails/miyuki35.webp")
                add g.make_button("cg_miyukigallery36","images/thumbnails/miyuki36.webp")
                add g.make_button("cg_miyukigallery37","images/thumbnails/miyuki37.webp")
                add g.make_button("cg_miyukigallery38","images/thumbnails/miyuki38.webp")
                add g.make_button("cg_miyukigallery39","images/thumbnails/miyuki39.webp")
                add g.make_button("cg_miyukigallery40","images/thumbnails/miyuki40.webp")
                null
                null
        showif cg_page_i == 5:
            grid 4 3:
                style_prefix "gallery_stuff"
                add g.make_button("cg_miyukigallery41","images/thumbnails/miyuki41.webp")
                add g.make_button("cg_miyukigallery42","images/thumbnails/miyuki42.webp")
                null
                null
                null
                null
                null
                null
                null
                null
                null
                null


#Videos
screen gallery_j():

    default cg_page_j = 1
    zorder 100
    tag menu
    hbox:
        style_prefix "gallery_stuff"
        textbutton _("Reina |") action SetLocalVariable("cg_page_j", 1)
        textbutton _("Jenni |") action SetLocalVariable("cg_page_j", 2)
        textbutton _("Sabrina |") action SetLocalVariable("cg_page_j", 3)
        textbutton _("Camilla |") action SetLocalVariable("cg_page_j", 4)
        textbutton _("Briana |") action SetLocalVariable("cg_page_j", 5)
        textbutton _("Miyuki") action SetLocalVariable("cg_page_j", 6)

#Reina Videos
    showif cg_page_j == 1:
        grid 3 1:
            style_prefix "gallery_stuff"
            add g.make_button("cg_reinavideo01","images/thumbnails/reinavid01.webp")
            add g.make_button("cg_reinavideo02","images/thumbnails/reinavid02.webp")
            add g.make_button("cg_reinavideo03","images/thumbnails/reinavid03.webp")
#Jenni Videos
    showif cg_page_j == 2:
        grid 3 1:
            style_prefix "gallery_stuff"
            add g.make_button("cg_jennivideo01","images/thumbnails/jennivid01.webp")
            add g.make_button("cg_jennivideo02","images/thumbnails/jennivid02.webp")
            add g.make_button("cg_jennivideo03","images/thumbnails/jennivid03.webp")
#Sabrina Videos
    showif cg_page_j == 3:
        grid 3 1:
            style_prefix "gallery_stuff"
            add g.make_button("cg_sabrinavideo01","images/thumbnails/sabrinavid01.webp")
            add g.make_button("cg_sabrinavideo02","images/thumbnails/sabrinavid02.webp")
            add g.make_button("cg_sabrinavideo03","images/thumbnails/sabrinavid03.webp")
#Camilla Videos
    showif cg_page_j == 4:
        grid 3 1:
            style_prefix "gallery_stuff"
            add g.make_button("cg_camillavideo01","images/thumbnails/camillavid01.webp")
            add g.make_button("cg_camillavideo02","images/thumbnails/camillavid02.webp")
            add g.make_button("cg_camillavideo03","images/thumbnails/camillavid03.webp")
#Briana Videos
    showif cg_page_j == 5:
        grid 3 1:
            style_prefix "gallery_stuff"
            add g.make_button("cg_brianavideo01","images/thumbnails/brianavid01.webp")
            add g.make_button("cg_brianavideo02","images/thumbnails/brianavid02.webp")
            add g.make_button("cg_brianavideo03","images/thumbnails/brianavid04.webp")
#Miyuki Videos
    showif cg_page_j == 6:
        grid 3 1:
            style_prefix "gallery_stuff"
            add g.make_button("cg_miyukivideo01","images/thumbnails/miyukivid01.webp")
            add g.make_button("cg_miyukivideo02","images/thumbnails/miyukivid02.webp")
            add g.make_button("cg_miyukivideo03","images/thumbnails/miyukivid03.webp")



