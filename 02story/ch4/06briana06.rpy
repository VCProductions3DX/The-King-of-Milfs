label brianaevent06:
    scene 01briana06
    "(What is Briana doing?)"
    main "Briana?"
    scene 02briana06
    briana "Oh, hey [player_name]."
    main "What are you doing?"
    briana "Practicing my tackling technique."
    main "Tackling?"
    scene 03briana06
    briana "Yeah. I watched my matches."
    briana "I'm ok when I'm on my feet, but when I get off of my feet, that's where I suffer."
    briana "So I'm practicing my techniques for when I'm on the ground."
    scene 04briana06
    briana "Hey, where are you going?"
    main "To warm up."
    scene 05briana06
    briana "Practice with me."
    briana "Please."
    main "I'm still heavier than you."
    briana "You're not that heavy. You don't even have to do anything, just like me hit you for a while."
    main "Sounds like fun."
    scene 06briana06
    briana "Come on, please??"
    main "Ok, ok."
    scene 07briana06
    briana "All you have to do is lie there and cover your face."
    briana "I won't hurt you too much."
    scene 08briana06
    main "Ouch!"
    briana "Don't be a wimp! You're stronger than that!"
    scene 09briana06
    main "What are you doing?"
    briana "Argghh!!"
    main "I told you, I'm too heavy!"
    scene 10briana06
    briana "Owww!!"
    main "You're stubborn."
    scene 11briana06
    briana "Shit, that hurts."
    main "Where?"
    briana "My back."
    scene 12briana06
    briana "Oh, that feels nice."
    briana "Since when did you learn how to give a massage?"
    main "Everyone knows that."
    scene 13briana06
    briana "Pfft."
    if brianamakeout in choices: 
        scene 14briana06
        briana "So are we going to continue what we started?"
        main "Bri-"
        scene 15briana06
        briana "No one comes here anyway. I'll just lock the door."
        main "Wait a minute."
        scene 16briana06
        briana "What?"
        main "Are you sure you want to do this? Here?"
        scene 17briana06
        briana "It's not like there's any other place to do it."
        scene 18briana06
        briana "There, it's closed."
        scene 19briana06
        "(Fuck, she's serious.)"
        jump brianafuck
    else:
        scene 20briana06
        briana "So are you gay?"
        main "What? No."
        scene 21briana06
        briana "It's ok, you can tell me. I won't judge."
        main "I'm not gay, I like women."
        scene 22briana06
        briana "So am I too young for your preferences?"
        menu:
            "Yes.":
                scene 34briana06
                briana "So you're into older women?"
                briana "Like...how old?"
                main "Uh-"
                scene 35briana06
                briana "Aunt Jenni's age?"
                briana "Mom's age?"
                menu:
                    "Closer to Reina's Age.":
                        scene 36briana06
                        briana "Wow, I never..I never expected that from you."
                        scene 37briana06
                        briana "Wait a minute..."
                        briana "Are you-are you fucking Mom?"
                        main "I-"
                        scene 38briana06
                        briana "No wonder Dad hates you."
                        briana "I thought this shit only happens on reality tv shows and soap operas."
                        briana "Wow, holy shit."
                        scene 39briana06
                        briana "You. My possible step dad."
                        briana "That's...wow."
                        scene 40briana06
                        main "Where are you going?"
                        briana "Out for a run before I die of laughter."
                        briana "Bye."
                        scene 41briana06
                        "(Shit, I meant to keep that a secret.)"
                        jump ch4freeroam

                    "Closer to Jenni's Age.":
                        scene 42briana06
                        briana "Is it because she was a supermodel?"
                        briana "Pfft."
                        main "Briana, she's really helping me with my addiction."
                        scene 43briana06
                        briana "Yeah, ok. I get it."
                        briana "Man I thought I was the most popular one in the family."
                        briana "Guess not."
                        scene 44briana06
                        main "Where are you going?"
                        briana "Out for a run."
                        briana "And maybe think over my life choices."
                        scene 45briana06
                        main "Bri-"
                        scene 46briana06
                        "(Fuck.)"
                        jump ch4freeroam

                    "That and older.":
                        main "I don't have a preference."
                        scene 47briana06
                        briana "Are you trying to get a sugar mommy?"
                        briana "Yikes."
                        main "No, I just like older women."
                        main "They're more experienced."
                        briana "But isn't it a lot more fun with someone that's not experienced?"
                        menu:
                            "You have a point.":
                                briana "So we can have a little bit of fun, right?"
                                main "Ok, you win."
                                jump brianafuck
                            "Not really.":
                                briana "Weirdo."
                                main "Where are you going?"
                                briana "Out for a run. Bye."
                                jump ch4freeroam
            "No.":  
                scene 23briana06
                briana "So do you have a girlfriend?"
                menu:
                    "Yes, her name is Sabrina." if SabrinaC.c_love >= 5:
                        scene 24briana06
                        briana "Sabrina..."
                        briana "Oh wait, she works at that geek store, doesn't she?"
                        briana "With the pink hair?"
                        main "Yeah."
                        scene 25briana06
                        briana "So that's your type."
                        briana "I should have known."
                        main "Where are you going?"
                        scene 26briana06
                        briana "Out for a run."
                        briana "I feel dirty now."
                        main "Bri-"
                        scene 27briana06
                        "(And I'm by myself.)"
                        jump ch4freeroam

                    "No.":
                        scene 28briana06
                        briana "So do I still have a chance?"
                        scene 29briana06
                        briana "Well??"
                        menu:
                            "Yeah, sure.":
                                scene 30briana06
                                "(She kissed me again.)"
                                jump brianafuck

                            "I'm sorry, I can't.":
                                main "You mean too much to me, Briana."
                                briana "You-"
                                scene 31briana06
                                briana "I'm sorry, [player_name]."
                                briana "I just thought since we grew up together that...we would be perfect for each other."
                                briana "I waited for you."
                                scene 32briana06
                                briana "But I guess that isn't happening."
                                main "Where are you going?"
                                scene 33briana06
                                briana "For a run, to clear my head."
                                briana "See you later, [player_name]."
                                jump ch4freeroam

label brianafuck:
    briana "So how should we do this?"
    menu:
        "Let her take control.":
            main "You decide."
            briana "Fine."
            briana "I'm on top now!"
            briana "How does it feel to be owned by a girl?"
            briana "Hmm??"
            "(Her pussy smells so good.)"
            briana "That tickles!"
            main "Take it off then. It'll feel better."
            briana "Fuck. Don't stop."
            briana "That feels good."
            main "Why did you pull away?"
            briana "That was intense. It felt like I was going to pee."
            briana "Now it's my turn."
            jump brianablowjob

        "Dominate her.":
            main "Let me take control."
            briana "Ok."
            briana "Hey! This isn't fair!"
            main "You're the one who wanted to wrestle me."    
            briana "You bully!"
            briana "I'll teach you to not underestimate me!"
            briana "Ahhh!!!"
            main "Got you."
            briana "You're too strong."
            "(Her tits are nice and firm.)"
            briana "Are you satisfied?"
            main "Nope."
            briana "Ugh!!"
            main "You're exposed."
            briana "Oh fuck."
            main "How does it feel?"
            briana "It feels good. Go deeper, please."
            briana "Oh fuck. Fuck."
            "(All of that training paid off.)"
            main "Now I want my reward."
            jump brianablowjob

label brianablowjob:
    briana "This is my first time seeing a cock in real life."
    briana "Wow."
    main "You're wasting time."
    briana "Yeah, yeah, let me just admire it."
    briana "It's so long and thick."
    briana "I'll do my best."

    "(For a virgin, she knows how to suck.)"
    "(But I still have to fuck her.)"
    main "That's enough. You're going to make me cum."
    briana "Oh-I'm sorry."
    main "Climb on top. You make yourself comfortable."
    briana "Will do."
    briana "Fuck, that's big."
    main "Don't push yourself."
    briana "Fuck!"
    "(Her pussy is so tight.)"
    "(I hope she isn't bleeding.)"
    briana "Thank you, [player_name]."
    briana "You're the best."
    "(I can't last much longer.)"
    main "Fuck!"
    briana "You came inside of me."
    main "I'm sorry."
    briana "That felt weird."
    briana "I liked it."
    "(She hasn't stopped grinding.)"
    briana "Don't tell me you're tired."
    main "I'm not like you."
    briana "Ok."
    main "Are you happy now?"
    briana "A little."
    main "A little?"
    briana "I want to try different positions next time."
    main "What?"
    briana "Please? Please?"
    main  "Ok."
    briana "Thank you, [player_name]."
    briana "I love you."
    jump ch4freeroam

    
    
