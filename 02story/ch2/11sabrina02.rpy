
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
    main "No."
    scene 21sabrina02
    sabrina "Are you getting tired?"
    main "No, horny."
    scene 22sabrina02
    "(Her lips are so soft.)"
    scene 25sabrina02
    "(I'm getting fucking hard.)"
    scene 26sabrina02
    sabrina "Someone's hard."
    scene 27sabrina02
    sabrina "Do you need someone to take care of you,Daddy?"
    main "Daddy?"
    scene 28sabrina02
    sabrina "You don't remember?"
    menu:
        "No, I don't.":
            sabrina "Ok, how about sir?"
            main "My name would be nice."
            scene 29sabrina02
            sabrina "Ok, [player_name]."
            scene sabrinahandjob01
            sabrina "Do you miss me doing this?"            
            sabrina "Stroking your cock up and down."
            sabrina "Or how about this?"
            scene sabrinablowjob01
            "(She's the perfect girlfriend.)"
            scene sabrinablowjob02
            "(Why did I ever break up with her.)"
            $choices.append(sabrinafuck)
            scene 30sabrina02
            sabrina "Did you miss that?"
            main "I miss your pussy more."
            scene 31sabrina02
            sabrina "Fuck me, [player_name]."
            scene sabrinafuck01
            sabrina "Mmm, that feels so good, daddy."
            "(Why is she still calling me daddy?)"
            "(I feel like I'm missing something.)"
            "(Fuck, who cares.)"
            scene sabrinafuck02
            sabrina "Fuck me, [player_name]. Fuck me hard."
            "(Fuck she feels so good.)"
            "(This will help keep those cravings away.)"
            sabrina "Oh,[player_name] don't stop! "
            main "Fuck!"
            "(Shit, didn't use protection. But she's on birth control, I hope.)"
            jump aftersabrinalove
        "Fine, you can call me Daddy..":
            $choices.append(sabrinaroleplay)
            scene 29sabrina02
            sabrina "You'll remember soon, Daddy."
            sabrina "What would like Daddy's little girl to do?"
            sabrina "Do you want to her stroke your cock with her hands?"
            scene sabrinahandjob01
            sabrina "Daddy's cock is so big and hard."
            sabrina "Mmmm, may I suck Daddy's cock, please Daddy? Please?"
            main "Yes."
            scene sabrinablowjob01
            "(Fuck, her mouth feels good.)"
            "(I can't believe I dumped her.)"
            scene sabrinablowjob02
            "(Did we really roleplay before? Why can't I remember?)"
            "(Fuck,I'll go along with it.)"
            scene 30sabrina02
            sabrina "What does Daddy want to do now?"
            $choices.append(sabrinafuck)
            main "Daddy wants you to ride his cock. Can you do that for me?"
            sabrina "Yes, Daddy's little girl can!"
            scene sabrinafuck01
            sabrina "Daddy's cock is so big. "
            sabrina "Do you like your girl's tight pussy, Daddy?"
            main "Yeah."
            scene sabrinafuck02
            sabrina "Fuck me, Daddy. Fuck me hard."
            "(Fuck she feels so good.)"
            "(This will help keep those cravings away.)"
            sabrina "Oh, Daddy don't stop! "
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
    if aishacooperate in choices:
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



   



   
