label epilogue05:
    scene 01epilogue05 with fade
    rose "Hello there, [player_name]."
    rose "It's been four months since you've been released from rehab."
    scene 02epilogue05
    rose "How are you feeling?"
    main "Amazing."
    scene 03epilogue05
    rose "And you're not taking any drugs?"
    main "No. I've found something better."
    rose "A job? A hobby?"
    main "Fucking."
    scene 05epilogue05
    rose "Certainly your life is more than that."
    main "It is, but I like it."
    if commitments >=2:
        main "Maybe a little too much."
        rose "How so?"
        jump mcexplainshiscommitments
    elif commitments == 1:
        main "I have someone I care for very much now."
        jump mcexplainshiscommitments
    else:
        main "I'm a free bird."
        jump secretending
label mcexplainshiscommitments:
    scene 04epilogue05
    rose "Oh? Tell me more."
    menu:
        "I'm going to marry my girlfriend." if sabrinamarriage in choices:
            scene 08epilogue05
            rose "Young love, isn't that something."
            if sabrinapregnancy in choices: 
                main "She's pregnant."
                scene 07epilogue05
                rose "Ah, that explains it."
                rose "You're becoming a responsible person."
            else:
                main "She keeps me sober."
                main "Plus her best friend passed away and I want to protect her."
            scene 09epilogue05
            rose "I'm happy for the two of you, but as you witnessed months ago, a young marriage can sour over the years."
            rose "Make sure it is something the both of you want."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm moving away from here with my aunt." if jennimove in choices:
            scene 06epilogue05
            main "I think living here tempts me to go back to using drugs."
            scene 09epilogue05
            rose "So creating more distance will keep you sober."
            main "Yeah. At least for the time being."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm going on vacation with a sugar mama." if camillavacation in choices:
            scene 06epilogue05
            rose "Who is that?"
            main "Camilla."
            scene 07epilogue05
            rose "So that's what she is doing. A shame, really."
            main "Why is that?"
            scene 08epilogue05
            rose "She seemed like the only person who cared about this little town."
            rose "Now we're going to be like every other beach town-full of high rise hotels and tourists."
            scene 05epilogue05
            rose "Still, it's her choice in life."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm helping my sister with her career." if brianarelationship in choices:
            scene 09epilogue05
            rose "Is that so?"
            main "She feels like she's aging out of fighting, so we're going to explore other options, together."
            main "I'm her manager, after all."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm helping my younger sister get a record deal." if pennycareer in choices:
            main "She's gone through a lot over the past year."
            main "But she's finally found her passion in music and wants to put her story out there, so I'm helping her with that."
            scene 09epilogue05
            rose "How considerate of you."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm just helping my mom out." if reinarelationship in choices:
            main "Now that dad's gone and Aunt Jenni's moving away, Mom needs someone close to her."
            rose "Not too close, I hope."
            main "Close enough. She's the reason I'm here now instead of the street. I just want to repay her for all she's done."
            scene 09epilogue05
            rose "Very well."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "Nothing else.":
            jump rosesfinaladvice

label rosesfinaladvice:
    if commitments >=2:
        scene 10epilogue05
        rose "That is a lot of commitments there."
        rose "You are a bit of a people pleaser."
        main "Just women."
        scene 11epilogue05
        rose "[player_name]."
        rose "While I happy for your new life, I don't want you to get overwhelmed."
        rose "Or let anyone down."
        main "So what should I do?"
        scene 12epilogue05
        rose "Commit to one and break off the rest."
        main "And if I don't?"
        scene 13epilogue05
        rose "Deal with the consequences."
        "(Useless as always.)"
        main "Thanks Dr. Rose."
        jump epiloguestart
    else:
        scene 14epilogue05
        rose "Make that person happy."
        rose "Don't let them down."
        main "I won't."
        scene 15epilogue05
        "(She's so preachy.)"
        main "Thanks Dr. Rose."
        rose "Take care."
        jump epiloguestart
label secretending:
    scene 10epilogue05
    rose "Well aren't you a Casanova."
    main "No, just keeping my options open."
    scene 16epilogue05
    rose "I suppose there's nothing else for us to discuss."
    main "Thanks Dr. Rose."
    jump epiloguestart   