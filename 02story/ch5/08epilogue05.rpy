label epilogue05:
    scene 01epilogue05
    rose "Hello there, [player_name]."
    rose "It's been four months since you've been released from rehab."
    rose "How are you feeling?"
    main "Amazing."
    rose "And you're not taking any drugs?"
    main "No. I've found something better."
    rose "A job? A hobby?"
    main "Fucking."
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
    rose "Oh? Tell me more."
    menu:
        "I'm going to marry my girlfriend." if sabrinamarriage in choices:
            rose "Young love, isn't that something."
            if sabrinapregnancy in choices: 
                main "She's pregnant."
                rose "Ah, that explains it."
                rose "You're becoming a responsible person."
            else:
                main "She keeps me sober."
                main "Plus her best friend passed away and I want to protect her."
            rose "I'm happy for the two of you, but as you witnessed months ago, a young marriage can sour over the years."
            rose "Make sure it is something the both of you want."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm moving away from here with someone." if jennimove in choices:
            rose "And who is that?"
            main "Jenni, Reina's younger sister."
            main "I think living here tempts me to go back to using drugs."
            rose "So creating more distance will keep you sober."
            main "Yeah. At least for the time being."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm going on vacation with a sugar mama." if camillavacation in choices:
            rose "Who is that?"
            main "Camilla."
            rose "So that's what she is doing. A shame, really."
            main "Why is that?"
            rose "She seemed like the only person who cared about this little town."
            rose "Now we're going to be like every other beach town-full of high rise hotels and tourists."
            rose "Still, it's her choice in life."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm helping a retired boxer find a new career." if brianarelationship in choices:
            rose "Is that so?"
            main "She feels like she's aging out of fighting, so we're going to explore other options, together."
            main "I'm her manager, after all."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm helping someone get a record deal." if pennyrelationship in choices:
            main "She's gone through a lot over the past year."
            main "But she's finally found her passion in music and wants to put her story out there, so I'm helping her with that."
            rose "How considerate of you."
            rose "Anything else?"
            menu:
                "Yes.":
                    jump mcexplainshiscommitments
                "No.":
                    jump rosesfinaladvice
        "I'm starting a relationship with my caretaker." if reinarelationship in choices:
            rose "Is that..wise?"
            rose "She just went through a divorce, did she not?"
            main "Yeah, but she's in love with me."
            rose "[player_name]. She's the most important figure in your life, you don't want to ruin a relationship like that for a night of lust."
            main "I'll take care of her, I promise."
            main "She's the reason I'm here in the first place. I owe it to her."
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
        rose "That is a lot of commitments there."
        rose "You are a bit of a people pleaser."
        main "Just women."
        rose "[player_name]."
        rose "While I happy for your new life, I don't want you to get overwhelmed."
        rose "Or let anyone down."
        main "So what should I do?"
        rose "Commit to one and break off the rest."
        main "And if I don't?"
        rose "Deal with the consequences."
        "(Useless as always.)"
        main "Thanks Dr. Rose."
        jump epiloguestart
    else:
        rose "Make that person happy."
        rose "Don't let them down."
        main "I won't."
        "(She's so preachy.)"
        main "Thanks Dr. Rose."
        rose "Take care."
        jump epiloguestart
label secretending:
    rose "Well aren't you a Casanova."
    main "No, just keeping my options open."
    rose "I suppose there's nothing else for us to discuss."
    main "Thanks Dr. Rose."
    jump epiloguestart       
    