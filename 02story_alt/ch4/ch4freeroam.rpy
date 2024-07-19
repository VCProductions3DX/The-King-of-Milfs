label inmcsroom:
    scene ch4freeroam
    "(My own room again.)"
    "(I never thought I would be living at home again.)"
    "(It looks so bare.)"

label freeroamch4:
    scene ch4freeroam
    "(I've got time to myself.)"
    menu:
        "Help Miyuki Again." if miyukievent02.status == "not completed":
            jump miyukievent02
        "Check on Camilla." if camillaevent05.status == "not completed":
            jump camillaevent05
        "Go to the funeral." if sabrinaevent04.status == "not completed":
            jump sabrinaevent04
        "Train with Briana." if brianaevent06.status == "not completed":
            jump brianaevent06
        "I'll sleep for a bit.":
            $miyukievent02.status_skipped("not completed")
            $camillaevent05.status_skipped("not completed")
            $sabrinaevent04.status_skipped("not completed")
            $brianaevent06.status_skipped("not completed")
            jump epilogue04