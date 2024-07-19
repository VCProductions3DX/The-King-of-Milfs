label ruinedending:
    scene black with fade
    "(It's so late.)"
    "(What's that commotion I'm hearing?)"
    scene 01ruinedending
    ethan "I've hired an agency to take those pictures offline."
    ethan "But unfortunately the damage is done. We'll have to move."
    scene 02ruinedending
    ethan "There you are."
    main "What's going on?"
    scene 03ruinedending
    ethan "Don't act dumb. You were a part of this."
    main "What?"
    scene 04ruinedending
    ethan "How much money did you get?"
    main "What? I don't know what you're talking about!"
    scene 07ruinedending
    ethan "Give me one reason why I shouldn't beat you to a pulp."
    ethan "Your own family!"
    ethan "Your mother, your aunt, your sisters!"
    ethan "After everything they've done for you!"
    ethan "And you sell them like a sick joke!"
    "(Fuck. He really did release those photos.)"
    main "It wasn't me, I swear."
    scene 05ruinedending
    ethan "Oh? I don't see how it was anyone else."
    ethan "Unless you think one of them can vouch for you, I think you should leave."
    scene 06ruinedending
    ethan "Or better yet, turn yourself into the police."
    scene 01ruinedending
    "(Fuck.)"
    "(Who can I depend on?)"
    menu:
        "(Mom.)":
            if ReinaC.c_love >=8:
                scene 08ruinedending
                reina "[player_name] would never do something like this."
                scene 09ruinedending
                reina "He's not the person you think he is."
                scene 10ruinedending
                reina "He is my son. My joy."
                scene 11ruinedending
                reina "For all of his faults, [player_name] is good man."
                scene 12ruinedending
                reina "And as his mother, I will do anything for him."
                scene 13ruinedending
                reina "He means everything to me."
                reina "And I will take care of him if no one else will."
                ethan "So that's how it is."
                scene 14ruinedending
                reina "The house is yours. We will find a new place together."
                jump reinaending
            else:
                scene 08ruinedending
                main "Mom?"
                ethan "I think your mom's generosity has run out."
                scene 06ruinedending
                ethan "As should you."
                ethan "Leave."
                jump outonthestreet
        "(Aunt Jenni.)":
            if JenniC.c_love >8:
                scene 17ruinedending
                jenni "I'll take him in."
                scene 18ruinedending
                jenni "I know [player_name] isn't the type of person to do this."
                jenni "We'll find the person who will."
                scene 19ruinedending
                ethan "That's nice of you Jenni for stepping up."
                scene 20ruinedending
                ethan "I hope he doesn't take advantage of you like the rest of us."
                jenni "I know him the best. He won't."
                scene 21ruinedending
                jenni "Let's go, [player_name]."
                jump jenniending
            else:
                main "Aunt Jenni?"
                jenni "I'm sorry, [player_name]."
                ethan "That settles it."
                ethan "Leave."
                jump outonthestreet
        "(Briana.)":
            if BrianaC.c_love >8:
                scene 22ruinedending
                briana "Stop it."
                briana "I'm so tired of this."
                briana "Why do you hate [player_name] so much?"
                ethan "Briana, look what he has done to you. You can't compete."
                scene 23ruinedending
                briana "That's all you care about! My career! Not me!"
                briana "He cares about me!"
                briana "And I care about him!"
                scene 24ruinedending
                briana "If he leaves, so do I."
                ethan "What about your mom? Your sister? She's still recovering."
                briana "That's for you to figure out."
                briana "Let's go, [player_name]."
                jump brianaending
            else:
                scene 22ruinedending
                main "Briana?"
                ethan "I hope you feel good about ruining a champion's career."
                ethan "Now leave."
                jump outonthestreet
        "(No one.)":
            main "I'll leave."
            ethan "That's what I thought."
            ethan "Don't bother getting your things. The sooner you leave, the better."
            jump outonthestreet

label outonthestreet:
    scene 25ruinedending
    "(Alone again.)"
    "(I wonder if someone will take me in.)"
    menu:
        "(Call Sabrina.)":
            sabrina "Hello?"
            main "Hey Sabrina, it's me."
            sabrina "Oh hey, [player_name]."
            main "Do you think I could come crash at your place for a while?"
            if SabrinaC.c_love >=7:
                sabrina "Sure!"
                sabrina "We're practically married at this point."
                jump sabrinaending
            else:
                sabrina "Did you get kicked out again?"
                main "Yeah."
                sabrina "Are you doing drugs again?"
                main "No, it's not like that."
                sabrina "I thought you changed, [player_name]."
                sabrina "But you're just the same. Ruining everyone's lives."
                sabrina "This is it, [player_name]."
                sabrina "Goodbye."
                "(Fuck.)"
                jump badendingstart
        "(Call Camilla.)":
            camilla "Hello?"
            main "Hi Camilla, it's me."
            camilla "And why are you calling me this late at night?"
            camilla "Craving a little company?"
            main "I..need a place to stay."
            if Camilla.c_love >=7:
                camilla "Of course. Anything for my little helper."
                camilla "I'll help you get back on your feet."
                camilla "For a small price."
                jump camillaending
            else:
                camilla "I'm afraid not."
                main "Why not?"
                camilla "I barely know you. You're a stranger."
                camilla "My generosity has boundaries."
                main "But-"
                camilla "There's a bus station to the city, I'm sure you can find shelter there."
                "(Shit.)"
                jump badendingstart
        "(Don't call anyone.)":
            jump badendingstart

label badendingstart:
    scene black 
    show text "6 months later" with Pause (5)

    if aishacooperate in choices:
        jump homelessending
    else:
        jump druggieending

label homelessending:
    scene 01badending with fade
    "Oh my god, another homeless encampment."
    "Look away and walk fast."
    scene 02badending
    "Useless shits. They need to get a job."
    "They're probably all drug addicts."
    "Or mentally ill."
    scene 03badending
    "Yeah. I wonder if they have any friends or family."
    "I doubt anyone would want to take them in."
    "Oh here come the police."
    scene 05badending
    aisha "Excuse me, you need to leave the premises."
    scene 06badending
    aisha "....[player_name]? Is that you?"
    "(Just leave me alone.)"
    scene 07badending
    aisha "There's a men's shelter two blocks down. You can spend the night there."
    scene 08badending
    aisha "But this place is being cleaned up. So you have to leave."
    scene 09badending
    aisha "Where are you going?"
    main "Fuck off!"   
    scene black with fade
    show text "A Bum: The End" with Pause (5)
    jump endingscreen

label druggieending:
    scene 10badending with fade
    "This place is a fucking mess."
    scene 11badending
    "What is this doing over here?"
    scene 12badending
    "I just got this place, do you mind not turning it to shit?"
    scene 13badending
    "Earth to [player_name]."
    scene 14badending
    "Hey man, are you already fucking wasted?"
    "The party hasn't even started yet."
    "You need to clean this shit up."
    scene 15badending
    main "Yeah sure, just one more hit."
    scene 16badending
    "(Damn this feels good.)"
    scene 17badending
    "(Shit what's happening??)"
    "(My heart's racing, I can barely breathe.)"
    scene 18badending
    "(Fuck.)"
    "You ok man?"
    scene 19badending
    "What the fuck dude?"
    scene 20badending
    "Fuck!!! Not you too!"
    scene black with fade
    show text "Overdosed: The End" with Pause (5)
    jump endingscreen

