
label sabrinaevent02:
    if sabrinaevent02.status == "not completed":
        scene 01sabrina02
        $SabrinaC.love_up(5)
        $sabrinaevent02.status_completed("not completed")
        sabrina "Hey [player_name]."
    else:
        scene 01sabrina02
        sabrina "Hey [player_name]."
    sabrina "Hey [player_name]."
    sabrina "Was it hard getting up here? The stairs are pretty rough."
    main "No, it's fine."
    scene 02sabrina02
    sabrina "Come in, I'll show you around."
    scene 03sabrina02
    sabrina "My parents converted this floor and the next into an apartment."
    sabrina "They didn't want to live too far from the store."
    scene 04sabrina02
    sabrina "What do you think of my streaming setup?"
    main "It's great."
    scene 05sabrina02
    sabrina "My bedroom and private gaming space is over here."
    scene 06sabrina02
    sabrina "It's not very big, but it's perfect for me."
    main "You seem pretty serious about your streaming."
    scene 07sabrina02
    sabrina "It beats standing around in the store all day."
    sabrina "Business is slow these days."
    scene 08sabrina02
    sabrina "When my parents get back, I might change it into a PC cafe."
    sabrina "You're spacing out, [player_name]."
    main "Oh, sorry. "
    sabrina "Let's play a few games."
    scene 10sabrina02
    sabrina "I'm no longer a noob you can stomp over."
    main "Yeah sure."
    scene 11sabrina02
    "(She's right.)"
    scene 12sabrina02
    sabrina "Haha! I told you I've gotten better."
    main "I was going easy on you."
    scene 13sabrina02
    sabrina "Don't lie, [player_name]. You were really trying."
    sabrina "I'm just good now, admit it."
    main "If you can beat me in another game, I will."
    sabrina "You're on!"
    scene 14sabrina02 with Pause (1)
    scene 15sabrina02
    sabrina "Aww man."
    main "Don't be a sore loser. You have gotten better."
    scene 17sabrina02
    sabrina "I'll show you who is a sore loser!"
    scene 19sabrina02
    sabrina "I got you now!"
    scene 20sabrina02
    sabrina "Giving up so soon?"
    main "No. I like the view from down here."
    sabrina "What else do you miss?"
    sabrina "Do you miss me doing this?"
    sabrina "Stroking your cock up and down."
    "(Fuck, she's good.)"
    sabrina "Your cock is so hard, [player_name]."
    $choices.append(sabrinafuck)
    sabrina "Oh fuck me, daddy."
    "(A Freudian slip?)"
    "(Fuck, who cares.)"
    sabrina "Fuck me, [player_name]. Fuck me hard."
    "(Fuck she feels so good.)"
    "(This will help keep those cravings away.)"
    sabrina "Oh,[player_name] don't stop! "
    main "Fuck!"
    "(Shit, didn't use protection. But she's on birth control, I hope.)"
    jump aftersabrinalove
label aftersabrinalove:
    scene 35sabrina02 with fade
    sabrina "[player_name]."
    main "Yes?"
    scene 32sabrina02
    sabrina "Do you know what happened to Jane?"
    "(Fuck, not this again.)"
    "(Should I lie or tell the truth?)"
    if aishacooperate is in choices:
        "(I'm already working with the police on the case.)"
        "(Still, should she hear it from me?)"
    else:
        "(I refused to work with police. )"
        "(Fuck. It's her cousin though.)"
    menu:
        "(Lie.)":
            main "No, I don't know."
            scene 39sabrina02
            sabrina "Really? Before she disappeared, she said she was at your place."
            main "Yeah, and I-I went out for a few hours."
            scene 40sabrina02
            sabrina "[player_name]."
            main "When I came back, she was gone. I don't know where she went."
            main "I left, went to the store to buy a few things, came back, and got wasted."
            main "Then her fucking boyfriend came home and went apeshit on me."
            main "I don't remember the rest."
            scene 41sabrina02
            sabrina "I hope you're not lying to me, [player_name]."
            main "I'm not."
            scene 33sabrina02
            sabrina "Will you stay the night?"
            main "Not now."
            scene 34sabrina02
            sabrina "Aww. Let me just lie here for a little longer."
            scene 36sabrina02
            sabrina "I'm glad you came over, [player_name]."
            main "Me too."
            scene 37sabrina02
            sabrina "So we're dating again, right?"
            main "Right."
            scene 38sabrina02
            sabrina "Love you."
            jump freeroamch2pt2
        "(Tell the truth.)":
            main "Sabrina. She's dead."
            scene 42sabrina02
            sabrina "No..."
            sabrina "Dead? How? "
            main "She overdosed."
            $choices.append(sabrinatruth)
            scene 43sabrina02
            sabrina "But-but she said she was clean!"
            main "She lied. Why do you think she was still with Jon?"
            main "He was her supply."
            scene 44sabrina02
            sabrina "And you didn't do anything? You didn't call an ambulance or anything?"
            main "She was already dead. And Jon didn't allow anyone to call 911 from his place."
            scene 46sabrina02
            sabrina "Get away from me!"
            main "Sabrina, I'm sorry!"
            scene 47sabrina02
            sabrina "She's missing for over 6 months, [player_name]."
            sabrina "Six months!"
            scene 48sabrina02
            sabrina "I thought she ran away from home for good but...she's dead."
            scene 49sabrina02
            sabrina "Dead."
            sabrina "She was my best friend."
            main "Sabrina."
            scene 50sabrina02
            sabrina "Just go, [player_name]."
            sabrina "I don't want to talk to you again."
            scene 45sabrina02
            "(I fucked that up.)"
            jump freeroamch2pt2



   



   
