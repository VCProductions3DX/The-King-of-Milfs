label ruinedending:
    "(It's late. What is Ethan doing here?)"
    ethan "Do we have any idea who is behind this?"
    briana "No."
    jenni "This is horrible."
    ethan "Where is that loser?"
    "(Fuck, he probably thinks I'm the one who released the pictures.)"
    reina "Ethan, stop it."
    ethan "I just want some answers, Reina."
    "(Fuck, I need to leave.)"
    briana "He's probably upstairs."
    "(Now's my chance.)"
    "(I'm sorry Reina. Jenni. Bri. Penny.)"
    jump badendingstart

label badendingstart:
    scene black 
    show text "6 months later" with Pause (5)

    if arrestdd in choices:
        jump homelessending
    else:
        jump druggieending

label homelessending:
    scene badending01
    "Oh my god, so many homeless people here."
    "Look away and walk fast."
    "Useless shits. They need to get a job."
    "They're probably all drug addicts."
    "Or mentally ill."
    "Yeah. I wonder if they have any friends or family."
    "I doubt anyone would want to take them in."
    "Oh here come the police."
    scene badending02 
    aisha "Excuse me, you need to leave the premises."
    aisha "....[player_name]? Is that you?"
    "(Just leave me alone.)"
    scene badending03
    aisha "There's a men's shelter two blocks down. You can spend the night there."
    aisha "But this place is being cleaned up. So you have to leave."
    scene badending04
    aisha "Where are you going?"
    main "Fuck off!"   
    screen black with fade
    show text "A Bum: The End" with Pause (5)
    jump endingscreen

label druggieending:
    scene badending05
    "Hey man, are you already fucking wasted?"
    "The party hasn't even started yet."
    main "Fuck, just one more hit."
    scene badending06
    "(Damn this feels good.)"
    "(Shit what's happening??)"
    "No more for you."
    "What the fuck dude?"
    screen black with fade
    show text "Overdosed: The End" with Pause (5)
    jump endingscreen

