label reinaevent03:
    scene 01reina03 with fade
    reina "Here we are."
    reina "I installed a home security system with surveillance cameras while you were in the hospital."
    reina "So if your attacker comes by again, we can catch them on camera."
    main "Are you not spending the night here?"
    reina "I am. But just for tonight. I have a lot of paperwork to do."
    scene 02reina03
    reina "Are you tired? Do you want to lay on the couch or on the bed in the bedroom?"
    main "The-the bedroom."
    scene 03reina03
    reina "Is something wrong?"
    main "No."
    scene 04reina03
    reina "This way."
    scene 05reina03
    reina "Are you comfortable?"
    main "Yes, thanks Mom."
    scene 06reina03
    reina "Since I'm spending the night here, I need to go grab a few things."
    reina "Would you like something to eat?"
    main "Yeah, that would be great."
    scene 07reina03
    reina "Anything in particular?"
    main "No."
    scene 08reina03
    reina "I'll be back."
    scene 09reina03
    "(Fuck, I didn't expect to see him.)"
    "(How does he know where I live? Am I being followed?)"
    "(I don't want Mom to get involved in this shit.)"
    "(Fuck.)"
    scene 10reina03
    reina "I'm back."
    reina "I brought you your food."
    scene 11reina03
    reina "Now don't make a mess. This place needs to stay as clean as possible."
    main "I won't."
    show screen eyeclosing
    scene 12reina03
    reina "I'll be in the living room. Good night."
    if reinakiss in choices:
        "(Mom is really distant.)"
        "(I wonder if she remembers our kiss the other night.)"
        "(Maybe she forgot.)"
    else:
        "(I hope Mom is ok after that fight.)"
        "(She looks so heartbroken.)"
    "(Fuck, I'm getting sleepy.)"
    hide screen eyeclosing
    scene 13reina03 with fade
    "(What time is it?)"
    "(Is Mom still awake?)"
    scene 14reina03
    "(She is.)"
    "(And she's drinking.)"
    scene 15reina03
    reina "[player_name]."
    reina "Can't sleep either?"
    scene 16reina03
    reina "Come sit down."
    scene 17reina03
    reina "I would offer you some wine but there's no more."
    "(She drank a whole bottle of wine?)"
    "(She's never done that.)"
    scene 18reina03
    reina "I hope my laughing didn't wake you up."
    main "No, it didn't."
    scene 19reina03
    "(She's staring off.)"
    main "What's on your mind, Mom?"
    scene 20reina03
    reina "I wish I was young again."
    scene 21reina03
    reina "I was quite popular in high school."
    scene 22reina03
    reina "I even had my fanclub."
    reina "I had so many guys ask me out. Offer to drive me home. Do my homework."
    scene 24reina03
    reina "Then I got married,had kids, and gained weight."
    #$jennievent03.status_skipped("not completed")
    scene 25reina03
    reina "All for a man who never loved me in the first place."
    scene 26reina03
    reina "I lost my beauty."
    if reinaevent03.status  == "completed":
        main "You're still beautiful, Mom."
        main "And you have us now."
        scene 27reina03
        reina "Is that what you think of me, [player_name]?"
        scene 28reina03
        reina "I didn't know you were into older women."
        reina "We're a lot more experienced."
        main "Mom-"
        scene 29reina03
        reina "Would you like to see?"
        main "MOM!!!!"
        scene 30reina03
        "(what is she doing?)"
        scene 31reina03
        reina "So warm."
        scene 32reina03
        "(She fell asleep.)"
        scene 33reina03
        "(I'll just leave her here.)"
        jump aishaevent01
    else:
        menu:
            "You are still beautiful, Mom.(Mom Love+5)": 
                if reinakiss in choices: 
                    scene 34reina03
                    reina "Is that why you kissed me the other night?"
                    main "I-"
                    $ReinaC.love_up(5)
                    scene 35reina03
                    reina "I can't remember the last time your father kissed me like that."
                    main "I'm really sorry Mom, I didn't mean to kiss you."
                    scene 36reina03
                    reina "I think every son wants to kiss his mother at some point in his life."                    
                    scene 37reina03
                    reina "As long as no one sees it, what's the harm in another kiss?"
                    jump reinasecondkiss                    
                else: 
                    scene 27reina03
                    reina "Is that what you think of me, [player_name]?"
                    scene 28reina03
                    $ReinaC.love_up(5)
                    reina "I didn't know you were into older women."
                    reina "Especially one as old as your mother."
                    scene 37reina03
                    reina "How about a little kiss?"
                    reina "From your first love?"
                    jump reinasecondkiss
            "But you have us now.": 
                scene 45reina03
                reina "You have a point, [player_name]."
                reina "Still, a nice body to hold would be nice."
                $reinaevent03.status_completed("not completed")
                scene 46reina03
                reina "I'm getting sleepy. I'm going to lay down here."
                main "Yeah, I'm going back to bed."
                reina "Good night, [player_name]."
                jump aishaevent01
label reinasecondkiss:
    menu:
        "(Kiss her.)":
            scene 38reina03
            "(Her lips are warm.)"
            "(Where are her hands going?)"
            main "Mom-"
            scene 39reina03
            reina "Shhh, I want to make at least one man in my life happy."
            reina "My sweet baby boy."
            scene 40reina03
            "(She's not going to remember this in the morning.)"
            "(Still, this doesn't feel right.)"
            scene 41reina03
            reina "Let mommy take care of you."
            menu:
                "(Take advantage of the situation.)(Mom Love + 5)":
                    reina "Such a good little boy."
                    reina "Look how big it is."
                    reina "Mommy's going to treat it just nice."
                    scene reinablowjob01
                    "(Fuck, Mom's mouth feels good.)"
                    "(This feels so wrong, getting a blowjob from Mom.)"
                    scene reinablowjob02
                    "(But I wasn't going to stop her.)"
                    "(I wish I could fuck her.)"
                    "(I can't even touch her pussy, fuck.)"
                    scene reinablowjob03
                    "(Fuck,I'm cumming.)"
                    scene bj01reina03
                    $ReinaC.love_up(5)
                    "(I came in her mouth.)"
                    $choices.append(reinabj)
                    scene bj02reina03
                    "(Shit, she's drooling and she's going to roll off of the floor.)"
                    "(This is bad. I have to get her on the couch.)"
                    $reinaevent03.status_completed("not completed")
                    scene bj03reina03
                    "(There. Let's hope she doesn't remember what happened tonight.)"
                    main "Good night, Mom."                 
                    jump aishaevent01
                "(Pull away.)(Mom Trust + 5)":
                    main "I-I'm really tired."
                    scene 42reina03
                    reina "Aww, you don't need help going back to sleep?"
                    $ReinaC.trust_up(5)
                    main "I don't."
                    $reinaevent03.status_completed("not completed")
                    scene 43reina03
                    reina "Good night, then."
                    main "Night, Mom."
                    scene 51jenni03
                    "(Shit, that was a close call.)"
                    "(My mom could have given me a blowjob.)"
                    "(I want one, but only if she's sober.)"
                    jump aishaevent01
        "(Pull away.)": 
            scene 42reina03
            reina "You're such a heartbreaker, [player_name]."
            main "I'm going back to bed."
            $reinaevent03.status_completed("not completed")
            scene 43reina03
            reina "Ok. Good night, [player_name]."
            main "Good night, Mom."
            scene 51jenni03
            "(That could have gone differently.)"
            jump aishaevent01






