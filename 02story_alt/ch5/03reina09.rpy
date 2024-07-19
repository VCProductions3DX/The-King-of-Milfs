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
                main "Dad."
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
    main "Mom"
    scene 14reina09
    main "Mom"
    reina "He's not looking over my shoulder any more."
    main "I'm sorry I didn't make it in time. I was busy."
    scene 15reina09
    reina "You've become your own man now, [player_name]."
    reina "This is something between your father and I."
    main "Mom, are you ok?"
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
    main "Mom-"

    if ReinaC.c_love >=5:
        scene 22reina09
        reina "I've fallen in love with you. Not as your mother, but as a woman."
        reina "I feel so dirty, falling in love with my own son."
        scene 23reina09
        reina "I don't want what we have- our time together- to get in the way of any relationship you have."
        reina "But, there's another part of me that wants you all to myself."
        reina "I'm such a greedy, selfish woman."
        scene 24reina09
        reina "[player_name], what do you want for the two of us?"
        menu:
            "I want to be as close to you as possible.":
                scene 32reina09
                reina "Even if what we do..isn't right?"
                main "It feels right to me."
                scene 36reina09
                reina "It does, doesn't it?"
                main "I love you, Mom."
                $choices.append(reinarelationship)
                $commitments +=1
                reina "I love you too, [player_name]."
                reina "I don't want to let you go."
                reina "Stay with me, always?"
                main "Always."
                scene 33reina09 with Pause(3)
                jump mcreinabeachkiss

            "Just being my mom is fine.":
                scene 29reina09
                reina "So that's it."
                reina "That's the right decision."
                main "I'll help you no matter what."
                scene 30reina09
                reina "There are some things you can't help with."
                reina "But I'm so glad you're there for me."
                reina "I need a bit of distance now."
                main "Yeah, sure Mom."
                scene 28reina09
                main "Thanks for helping me get sober."
                jump freeroamch5
    else:
        scene 20reina09
        reina "I've been a horrible mother and I want to apologize for my behavior."
        scene 23reina09
        reina "It seems like every time we're together, I become a weak sobbing mess."
        scene 24reina09
        reina "And I'm so sorry."
        main "I forgive you, Mom."
        reina "You're so kind and dependable."
        scene 29reina09
        reina "Do you think the two of us can become close?"
        main "Close?"
        scene 30reina09
        reina "Like lovers?"
        menu:
            "That's a little too close for me, Mom.":
                scene 31reina09
                reina "You're right."
                reina "A mom and her son shouldn't be this close."
                reina "I need some time to myself."
                main "Yeah, sure."
                scene 28reina09
                "(I'm sure Mom will be alright.)"
                jump freeroamch5
            "Sure, if no one else knows.(+Mom Love)":
                reina "It'll be our little secret."
                scene 33reina09 with Pause(3)
                $ReinaC.love_up(10)
                $commitments += 1
                $choices.append(reinarelationship)
                jump mcreinabeachkiss

    label mcreinabeachkiss:
        scene 37reina09
        reina "Thank you, [player_name]."
        reina "You mean everything to me."
        reina "We can start a new life together, just the two of us."
        scene 38reina09 with Pause(4)
        scene 35reina09
        "(Mom and I are back on good terms.)"
        "(We're closer than ever.)"
        jump freeroamch5

      




    