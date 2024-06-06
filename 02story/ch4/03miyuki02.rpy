label miyukievent02:
    scene 01miyuki02
    miyuki "Well, isn't it my favorite employee."
    main "Your only employee."
    scene 02miyuki02
    miyuki "Touche."
    main "You seem really happy."
    scene 03miyuki02
    miyuki "Is it obvious?"
    miyuki "My boyfriend is finally divorcing his stuck-up wife."
    miyuki "Well, she handed him the divorce papers."
    main "How does he feel about it?"
    scene 04miyuki02
    miyuki "Well, he's a little upset."
    miyuki "They share a lot of assets together, including that big house of theirs."
    miyuki "But I'm sure he'll get over it. He has me, after all."
    main "Are you going to ask him to marry you?"
    scene 05miyuki02
    miyuki "Of course. It'll make me look like a better candidate."
    miyuki "Only downside is not using his company for the project, but that's politics."
    "(She intends to fuck Ethan over.)"
    menu:
        "That's a bit unfair.":
            scene 27miyuki02
            miyuki "Life is unfair."
            miyuki "Not much can be done about that."
            miyuki "Let's get to work, shall we?"
            scene 28miyuki02
            miyuki "You have a car, don't you?"
            main "Yeah."
            miyuki "I need you to put these billboards up on every major intersection."
            miyuki "If there's a light, put it there. And in the middle of a roundabout if you see one."
            main "Sure."
            scene 29miyuki02
            "(Fuck, this is heavy.)"
            miyuki "Ta-ta now."
            scene 30miyuki02 with fade
            "(That didn't take as long as I thought.)"
            main "Miyuki?"
            miyuki "[player_name]? I'm in here."
            scene 31miyuki02
            "(Woah!)"
            miyuki "You look like a virgin."
            main "Why-why are you almost naked?"
            scene 32miyuki02
            miyuki "Because I'm hot. And lonely."
            scene 33miyuki02
            miyuki "Fuck me, [player_name]."
            menu:
                "(Accept.)":
                    jump fuckmiyukisecondtime
                "(Refuse.)":
                    scene 34miyuki02
                    miyuki "You're so innocent and sweet."
                    miyuki "Oh well."
                    scene 35miyuki02
                    miyuki "You're done for the day, [player_name]."
                    jump freeroamch4            
        "I actually know Ethan.":
            scene 06miyuki02
            miyuki "WHAT?"
            scene 07miyuki02
            $choices.append(miyukiblackmail)
            miyuki "Please tell me you're joking."
            main "No, I know him."
            scene 08miyuki02
            miyuki "Wait-wait-wait-"
            miyuki "How-no, no."
            miyuki "Listen, we don't know each other that well, but you have that keep what we say and do here a secret."
            scene 09miyuki02
            miyuki "My reputation is everything to me."
            menu:
                "My silence isn't free.":
                    scene 10miyuki02
                    miyuki "Blackmailing me, are you?"
                    main "It's your reputation."
                    scene 11miyuki02
                    miyuki "What do you want?"
                    miyuki "A fancy car? A condo?"
                    miyuki "Do you think I'm made out of money?"
                    menu:
                        "Stop the project.":
                            scene 15miyuki02
                            miyuki "Stop the project?"
                            miyuki "Are you insane?"
                            scene 16miyuki02
                            miyuki "That's my life's work!"
                            miyuki "You have no idea how big this is!"
                            scene 17miyuki02
                            miyuki "This little beach town has popular tourist destination written all over it."
                            miyuki "If I don't do it, someone else will."
                            scene 18miyuki02
                            miyuki "Wait a minute.."
                            scene 19miyuki02
                            miyuki "Did that fat bitch Camilla put you up to this?"
                            main "That's not important."
                            scene 20miyuki02
                            miyuki "Yes, it is."
                            miyuki "I never thought she would stoop this low."
                            scene 21miyuki02
                            miyuki "The project will happen. People want it."
                            miyuki "You should tell me what you want before I kick you out."
                            menu:
                                "Nothing, I'm leaving.":
                                    scene 22miyuki02
                                    miyuki "Goodbye."
                                    miyuki "No harsh feelings if I bury your brand-new reputation to the ground."
                                    miyuki "You filthy drug addict."
                                    menu:
                                        "Walk away.":
                                            scene 23miyuki02
                                            miyuki "Goodbye,loser!"
                                            jump freeroamch4
                                        "Suck my cock.":
                                            scene 24miyuki02
                                            miyuki "And there it is."
                                            miyuki "No good scum like you shouldn't be here."
                                            jump fuckmiyukisecondtime
                                "Bend over.":
                                    scene 25miyuki02
                                    miyuki "Fiesty little boy."
                                    miyuki "But you're getting me all worked up."
                                    miyuki "Make it quick."
                                    jump fuckmiyukisecondtime
                        "A nice fuck.":
                            main "Anytime I want."
                            scene 12miyuki02
                            miyuki "You little horndog."
                            miyuki "You must really hate Ethan."
                            main "Do we have a deal?"
                            scene 13miyuki02
                            miyuki "And you won't tell him anything?"
                            main "Only if you refuse."
                            scene 14miyuki02
                            miyuki "It's a deal."
                            miyuki "I bet you want to fuck me right now, don't you?"
                            jump fuckmiyukisecondtime
                "You should have thought of that before talking to me.":
                    scene 36miyuki02
                    miyuki "Please don't tell Ethan, please."
                    scene 37miyuki02
                    miyuki "He means everything to me."
                    menu:
                        "Not my problem.":
                            scene 38miyuki02
                            miyuki "Wait, [player_name]! We can work this out!"
                            miyuki "[player_name], please!"
                            jump freeroamch4
                        "Enough to let someone else fuck you?":
                            scene 40miyuki02
                            miyuki "A relationship is more than just sex."
                            miyuki "He knows that better than anyone else."
                            scene 41miyuki02
                            miyuki "So that's what you want? To fuck me?"
                            jump fuckmiyukisecondtime    
label fuckmiyukisecondtime:
    scene miyukisecondfuck01
    "(I'm really fucking her.)"
    "(Ethan would hate me right now.)"
    "(But fuck him.)"
    scene miyukisecondfuck02
    "(He mistreated Reina, so I'll fuck his girlfriend too.)"
    "(Just the thought of him finding out makes this hot.)"
    scene miyukisecondfuck03
    miyuki "Fuck, your cock feels so good."
    scene miyukisecondfuck04
    "(And just to make better, I'm going to creampie her.)"
    miyuki "Wait-wait-"
    scene miyukisecondfuck05
    main "Fuck."
    miyuki "Damn it."
    scene 42miyuki02
    miyuki "There, are you happy now?"
    main "Never, but it did feel good."
    scene 43miyuki02
    miyuki "Just leave."
    main "I'll be back."
    jump freeroamch4

