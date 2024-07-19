label freeroamch1:
    scene ch1freeroam
    "(I have a lot of free time now.)"
    "(Guess I'll walk around town and see what's going on.)"
    menu:
        "Visit Briana." if brianaevent01.status == "not completed":
            jump brianaevent01
        "Visit Penny at the skatepark." if pennyevent02.status == "not completed":
            jump pennyevent02
        "Visit Sabrina." if sabrinaevent01.status == "not completed":
            jump sabrinaevent01
        "Visit Camilla." if camillaevent02.status == "not completed":
            jump camillaevent02
        "Go home and wait for Jenni.":
            jump moveaheadch1
        

label moveaheadch1:
    show text "Any events not completed will be marked as 'skipped' if you continue." with Pause (5)
    show text "You can view these events in the 'Replay' section of the main menu." with Pause (5)
    "Continue?"
    menu:
        "Yes": 
            $pennyevent02.status_skipped("not completed")
            $brianaevent01.status_skipped("not completed")
            $sabrinaevent01.status_skipped("not completed")
            $camillaevent02.status_skipped("not completed")
            jump jennievent01
            
        "No":
            jump freeroamch1