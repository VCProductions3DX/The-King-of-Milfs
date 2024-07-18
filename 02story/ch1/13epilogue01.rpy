label epilogue01event:
    scene 01epilogue01
    "(Why does it feel like someone is watching me?)"
    scene 02epilogue01
    "(It seems eerily quiet.)"
    scene 03epilogue01
    "(But I can't shake this feeling off.)"
    main"Who's there?"
    scene dropdown with Pause (2)
    play sound "sfx/FallDown1.ogg"
    stop sound
    scene 05epilogue01 with fade
    "(Fuck...)"
    scene 06epilogue01
    "Look familar, loser?"
    "Does it?"
    scene 07epilogue01
    "Answer me, you piece of shit!"
    main "Fuck off!"
    scene 08epilogue01
    "God you got fucking fat."
    main "Leave me alone, I didn't fucking kill her."
    scene 09epilogue01
    "No, you left her alone with the fucking drugs."
    scene 10epilogue01
    "If only you had- you know [i]stayed[/i] with her- she might not be dead."
    "And I wouldn't have to dispose of the body and then tell her parents that she ran away."
    "Not like they believed me, so the cops raided the police and I had to throw away all of that product."
    scene 11epilogue01
    main "Why didn't you tell them the truth?"
    "That their daughter is a junkie? Sounds nice except you're not the one being investigated for murder."
    main "What do you want from me?"
    scene 12epilogue01
    "I just wanted you to know that I'm here. Watching you."
    "I have to rebuild everything from scratch, thanks to you."
    "I could use some help getting started again, in terms of money."
    main "I don't owe you a damn thing!"
    scene 13epilogue01
    "Shit. That big bitch is awake."
    scene 14epilogue01
    "(He's gone.)"
    "(Fuck my legs hurt.)"
    scene 15epilogue01
    "(And he left the needle here- this doesn't look good.)"
    "(I need to hide it before Camilla comes over.)"
    scene black with fade
    show text "End of Chapter 1" with Pause (5)
    "Would you like to save your progress?"
    menu:
        "Yes":
            call screen save
            jump prologue02    
        "No":
            jump prologue02

