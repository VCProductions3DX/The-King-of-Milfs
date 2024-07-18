label reinaevent09:
    scene 01reina09
    "(Shit, I'm late.)"
    "(They've already started.)"
    "(And the door's locked.)"
    "(I'll just wait until they're done.)"
    scene 02reina09 with fade
    "(They're done.)"
    scene 03reina09
    "(It looks a funeral procession.)"
    scene 05reina09 
    "(There's Ethan.)"
    scene 06reina09
    ethan "She's all yours."
    if miyukiblackmail is choices:
        "(Should I tell him about Miyuki?)"
        menu:
            "(Yes.)":
                main "Ethan."
                scene 07reina09
                ethan "What is it?"
                main "It's about Miyuki."
                scene 08reina09
                ethan "What about her?"
                main "She's not going to give you the contract."
                ethan "What makes you say that?"
                main "Listen."
                scene 09reina09
                ethan "That bitch."
                $choices.append(ethanfindsout)
                scene 10reina09
                ethan "I guess you're not a bad guy after all."
                jump afterdivorcereina
            "(No.)":
                scene 11reina09
                jump afterdivorcereina
    else:
        scene 11reina09
        main "Thanks."
        jump afterdivorcereina
label afterdivorcereina:
    scene 12reina09
    maxine "She's still in shock."
    maxine "She'll need a shoulder to lean on. But it's done."
    scene 13reina09
    main "Reina?"
    scene 14reina09
    main "Reina?"
    reina "He's not in my shadow any more."
    main "I'm sorry I didn't make it in time. I was busy."
    scene 15reina09
    reina "You've become your own man now, [player_name]."
    reina "This is something I had to do by myself."
    main "Reina, are you ok?"
    reina "Yeah. I-I- I just need to go somewhere where it's quiet."
    scene 16reina09
    reina "Will you come with me for a short drive?"
    main "Sure."
    scene 17reina09 with fade
    reina "This is my favorite spot."
    main "It's nice and quiet."
    scene 18reina09
    reina "And they want to turn it into a 5-star resort."
    reina "Nothing but tourists littering the place."
    main "What's on your mind?"
    scene 19reina09
    reina "Everything these past three months."
    reina "More importantly, what happened between us."
    main "Reina-"
    if ReinaC.c_love >=5:
        scene 22reina09
        reina "I've fallen in love with you. Not as a mother, but as a woman."
        main "Oh-"
        scene 23reina09
        reina "I've just divorced my husband and here I am, obsessed with another man."
        reina "One I personally raised as a favor for a friend."
        scene 24reina09
        reina "But how do you feel about me, [player_name]?"
        reina "Do you see me as your mother or something else?"
        menu:
            "You're the most important woman in my life. (+Love)":
                scene 32reina09
                $choices.append(reinarelationship)
                $commitments +=1
                reina "[player_name]."
                jump mcreinabeachkiss
            "You're the mother I wish I had.":
                scene 26reina09
                reina "Thank you."
                scene 27reina09
                reina "Do you find it weird to fuck someone you consider your mom?"
                main "Not really."
                reina "I'll never understand men, I suppose."
                reina "I need some time alone."
                main "Yeah, sure."
                scene 28reina09
                "(I'm sure Reina will be alright.)"
                jump freeroamch5
            "You're Reina, that's it.":
                scene 29reina09
                reina "That's it."
                reina "I'm a foolish woman."
                scene 30reina09
                reina "I'm glad you're sober, [player_name]."
                reina "And for being there for me when I needed someone the most."
                reina "But I think...I think I need a bit of distance now."
                scene 28reina09
                main "Thanks for helping me get sober, Reina."
                jump freeroamch5
    else:
        scene 20reina09
        reina "I think I've been a bad foster parent to you."
        reina "And I want to apologize for my behavior."
        main "Reina-"
        scene 23reina09
        reina "It seems like every time we're together, I become a weak sobbing mess."
        reina "I'm supposed to be a stand-in for your mother, and I'm not."
        scene 24reina09
        reina "And I'm so sorry."
        main "I forgive you, Reina."
        scene 29reina09
        reina "Do you think you and I could become more?"
        main "What do you mean?"
        scene 30reina09
        reina "Like lovers?"
        menu:
            "You're too old for me, Reina.":
                scene 31reina09
                reina "I guess I am."
                reina "It was worth a shot."
                reina "I need some time to myself."
                main "Yeah, sure."
                scene 28reina09
                "(I'm sure Reina will be alright.)"
                jump freeroamch5
            "Of course.(+ Reina Love)":
                scene 32reina09
                reina "Really?"
                reina "You and me?"
                $ReinaC.love_up(10)
                main "Yeah."
                $commitments += 1
                $choices.append(reinarelationship)
                jump mcreinabeachkiss

    label mcreinabeachkiss:
        scene 33reina09 with Pause(3)
        scene 37reina09
        reina "Thank you, [player_name]."
        reina "You mean everything to me."
        reina "We can start a new life together, just the two of us."
        scene 38reina09 with Pause(4)
        scene 35reina09
        "(I'm sure my real mom won't mind us together.)"
        "(At least until Reina is completely over Ethan.)"
        jump freeroamch5


    