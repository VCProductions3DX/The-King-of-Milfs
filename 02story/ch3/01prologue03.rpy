label prologue03:
    scene black 
    show text "3 months later" with Pause(5)
    scene 01prologue03 with fade
    "Good afternoon, Sierra Beach. Here are the top stories for this afternoon."
    scene 02prologue03
    "(I've lost a bit of weight in the past 3 months.)"
    "(Still a bit heavy, though.)"
    scene 03prologue03
    "(More importantly, {i}he{/i} hasn't visited me.)"
    "Breaking news, a body has washed up in the Sierra River Basin."
    "Authorities have identified the body as a young female. An autopsy is being performed on her cause of death."
    "We will update you once we have more information."
    "(A body?)"
    "(Could it be her?)"
    scene 04prologue03
    "(Shit, this isn't good.)"
    "(But I have a couple of things to do.)"
    label freeroamch3:
        scene 04prologue03
        menu:
            "Volunteer for Miyuki." if miyukievent01.status == "not completed":
                jump miyukievent01
            "Help Camilla close her store." if camillaclosesstore in choices and camillaevent04.status == "not completed":
                jump camillaevent04
            "Take Reina out to dinner." if reinaevent05.status == "not completed":
                jump reinaevent05
            "Help Jenni move." if jennievent05.status == "not completed":
                jump jennievent05
            "I've finished everything.":
                $prologue03.status_completed("not completed")
                $miyukievent01.status_skipped("not completed")
                $camillaevent04.status_skipped("not completed")
                $reinaevent05.status_skipped("not completed")
                $jennievent05.status_skipped("not completed")
                jump proceedch3
    label proceedch3:
        "(I should check up on Sabrina.)"
        if sabrinatruth in choices:
            "(But I doubt she wants to talk to me again.)"
            "(I'll just wait for her to text me.)"
        else:
            "(I don't even know what to say to her.)"
        play sound "sfx/knocknock.ogg"
        main "I'll be right there."
        stop sound
        jump aishaevent02





    