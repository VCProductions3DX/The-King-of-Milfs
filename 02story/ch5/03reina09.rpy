label reinaevent09:
    scene 01reina09
    "(Shit, I'm late.)"
    scene 02reina09
    "(They've already started.)"
    "(And the door's locked.)"
    "(I'll just wait until they're done.)"
    scene 03reina09 with fade
    ethan "She's all yours."
    if miyukiblackmail is choices:
        "(Should I tell him about Miyuki?)"
        menu:
            "(Yes.)":
                scene 04reina09
                main "Ethan."
                ethan "What is it?"
                main "It's about Miyuki."
                scene 05reina09
                ethan "What about her?"
                main "She's not going to give you the contract."
                ethan "What makes you say that?"
                scene 06reina09
                main "Listen."
                #
                ethan "That bitch."
                $choices.append(ethanfindsout)
                ethan "I guess you're not a bad guy after all."
                jump afterdivorcereina
            "(No.)":
                scene 07reina09
                jump afterdivorcereina
    else:
        scene 08reina09
        main "Thanks."
        jump afterdivorcereina
label afterdivorcereina:
    main "How are you doing, Reina?"
    scene 09reina09
    reina "I feel ...free."
    reina "He's not in my shadow any more."
    main "I'm sorry I didn't make it in time. I was busy."
    scene 10reina09
    reina "You've become your own man now, [player_name]."
    reina "You don't need me looking out for you any more."
    scene 11reina09
    main "Reina, are you ok?"
    reina "Yeah. I-I- I just need to go somewhere where it's quiet."
    scene 12reina09
    reina "Will you come with me for a short drive?"
    main "Sure."
    scene 13reina09 with fade
    reina "This is my favorite spot."
    main "It's nice and quiet."
    scene 14reina09
    reina "And they want to turn it into a 5-star resort."
    reina "Nothing but tourists littering the place."
    main "What's on your mind?"
    scene 15reina09
    reina "Everything these past three months."
    reina "More importantly, what happened between us."
    main "Reina-"
    if ReinaC.c_love >=5:
        scene 16reina09
        reina "I've fallen in love with you. Not as a mother, but as a woman."
        main "Oh-"
        scene 17reina09
        reina "I've just divorced my husband and here I am, obsessed with another man."
        reina "One I personally raised as a favor for a friend."
        scene 18reina09
        reina "But how do you feel about me, [player_name]?"
        reina "Do you see me as your mother or something else?"
        menu:
            "You're the most important woman in my life.":
                scene 19reina09
                $choices.append(reinarelationship)
                $commitments +=1
                reina "[player_name]."
                jump freeroamch5
            "You're the mother I wish I had.":
                scene 20reina09
                reina "Thank you."
                scene 21reina09
                reina "Do you find it weird to fuck someone you consider your mom?"
                main "Not really."
                jump freeroamch5
            "You're Reina, that's it.":
                scene 22reina09
                reina "That's it."
                reina "I'm a foolish woman."
                scene 23reina09
                reina "I'm glad you're sober, [player_name]."
                reina "And for being there for me when I needed someone the most."
                scene 24reina09
                reina "But I think...I think I need a bit of distance now."
                main "Thanks for helping me get sober, Reina."
                jump freeroamch5

    else:
        scene 25reina09
        reina "I think I've been a bad foster parent to you."
        reina "And I want to apologize for my behavior."
        main "Reina-"
        scene 26reina09
        reina "It seems like every time we're together, I become a weak sobbing mess."
        reina "I'm supposed to be a stand-in for your mother, and I'm not."
        scene 27reina09
        reina "And I'm so sorry."
        main "I forgive you, Reina."
        scene 28reina09
        reina "Do you think you and I could become more?"
        main "What do you mean?"
        scene 29reina09
        reina "Like lovers?"
        menu:
            "You're too old for me, Reina.":
                scene 30reina09
                reina "I guess I am."
                reina "It was worth a shot."
                jump freeroamch5
            "Maybe.":
                scene 31reina09
                reina "Really?"
                reina "You and me?"
                main "Yeah."
                $commitments += 1
                $choices.append(reinarelationship)
                jump freeroamch5


    