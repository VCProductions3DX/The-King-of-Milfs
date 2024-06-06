
image ctc:
    xpos 10
    ypos 15
    alpha 0.0
    pause 0.05
    linear 0.5 alpha 1.0
    "gui/ctc_white.png"
    repeat
image vclogo = "gui/vclogo.png"
image eyeopen:
    "gui/eye.png"
    alpha 1.0
    linear 3.0 alpha 0.0
    repeat
image eyeclose:
    "gui/eye.png"
    alpha 0.0
    linear 3.0 alpha 1.0
    repeat
transform fromtheleft:
    xalign 1.0
    yalign 0.5
    linear 0.5 xalign 0.5
transform centerright:
    xalign 0.8
    yalign 0.5
transform centerleft:
    xalign 0.2
    yalign 0.5
transform topleft:
    xalign 0.2
    yalign 0.1
transform topright:
    xalign 0.8
    yalign 0.1
transform thoughtsleft:
    xalign 0.2
    yalign 0.3
transform thoughtsright:
    xalign 0.8
    yalign 0.3
transform thoughtsbottomright:
    xalign 0.8
    yalign 0.6
transform thoughtsbottomleft:
    xalign 0.2
    yalign 0.6
screen eyeopening():
    zorder 102
    add "eyeopen"
screen eyeclosing():
    zorder 102
    add "eyeclose"
image splotch:
    "gui/splotches.png"
    alpha 1.0
    linear 2.0 alpha 0.0
    repeat
screen splotches():
    zorder 102
    add "splotch"

define fade = Fade(0.5, 0.0, 0.5)
define fadewhite = Fade(0.5, 0.0, 0.5, color="#ffffff")
define fadehold = Fade(0.5, 1.0, 0.5)
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")
define blackflash = Fade(0.1,0.0,0.5, color="#000000")
define smallshake = ComposeTransition(vpunch,before=hpunch)
define slowfade = Fade(1.0, 0.5, 1.0)
define fasterfadeout = Fade(0.5, 0.5, -1)
define slowfadeout = Fade(0.5, 0.5, 1)
define fadein = Fade(1.8, 1.0, -0.5)
define slowfadein = Fade(1.8, 1.0, 1)
define fadeout = Fade(0.0, 0.5, 1.0)
define fasterfadein = Fade(0.6, 1.0, -0.5)

