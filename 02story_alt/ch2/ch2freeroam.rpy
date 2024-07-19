label freeroamch2:
    scene ch2freeroam
    "(That was crazy.)"
    "(Am I into older women now?)"
    "(Or is it just the withdrawals?)"
    "(Shit, there's a lot of texts.)"
    jump readtexts

label readtexts:
    scene ch2freeroam
    menu:
        "(Read Briana's text.)" if brianaevent03.status == "not completed":
            scene brianatext
            "(I'll invite Bri over.)"
            jump brianaevent03
        "(Read Penny's text.)" if pennyevent03.status == "not completed":
            scene pennytext
            "(I'll invite Penny over.)"
            jump pennyevent03
        "(Mark all as read.)":
            $pennyevent03.status_skipped("not completed")
            $brianaevent03.status_skipped("not completed")
            jump callreinaagain
label callreinaagain:
    "(I have an appointment with Dr. Rose)."
    "(I'll ask Mom to take me.)"
    jump reinaevent04
label freeroamch2pt2: 
    scene ch2freeroampt2
    "(I'm feeling a bit better.)"
    "(Plus I have a car now.)"
    "(What to do.)"
    menu:
        "(Visit Sabrina.)" if sabrinaevent02.status == "not completed":
            jump sabrinaevent02
        "(Train with Briana.)" if brianaevent04.status == "not completed":
            jump brianaevent04
        "(Go shopping with Penny.)" if pennyevent04.status == "not completed":
            jump pennyevent04
        "(Check Jenni's Text.)":
            scene jennitext
            $pennyevent04.status_skipped("not completed")
            $brianaevent04.status_skipped("not completed")
            $sabrinaevent02.status_skipped("not completed")
            "(Jenni is texting me.)"
            jump jennievent04