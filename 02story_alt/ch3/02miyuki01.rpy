label miyukievent01:
    scene 01miyuki01 with fade
    "(This is the building.)"
    scene 02miyuki01
    "(Her office is on the third floor.)"
    scene 03miyuki01
    "(Looks like I got it right.)"
    scene 04miyuki01
    miyuki "So Thursday at 11 AM? Yes, I am available at that time. "
    scene 05miyuki01
    miyuki "There you are. [player_name]? Did I get that right?"
    main "Yeah."
    scene 06miyuki01
    miyuki "Welcome to my office. We're in the early stages of campaigning, so it's not battle-ready yet."
    main "Battle-ready?"
    scene 07miyuki01
    miyuki "First time getting involved in politics?"
    miyuki "This is what we call our battle-station. Even though it's a small town election, it's important if you want to succeed."
    scene 08miyuki01
    miyuki "We're going to need lots of flyers, posters, billboards. I want my name on every corner of this town."
    "(She talks exactly like Dad.)"
    miyuki "We'll also need mail-in posters."
    scene 09miyuki01
    miyuki "Are you paying attention?"
    main "Yeah, that's a lot."
    scene 10miyuki01
    miyuki "It's not a national election. It isn't much."
    scene 11miyuki01
    miyuki "Ugh, someone is calling me again. I have to take this."
    scene 12miyuki01
    "(She is certainly a busy woman.)"
    scene 13miyuki01
    "(What's that on her desk?)"
    scene 14miyuki01
    "(It's a picture of her...and Dad!)"
    "(So she really is dating Dad.)"
    menu:
        "Take a picture for Mom.":
            with flash
            "(I have to let her know.)"
            scene 15miyuki01
            $choices.append(miyukiethanphoto)
            "(I'll give it to her when I see her next time.)"
            jump afterpicture
        "Do nothing.":
            "(It's not my place to get in between Mom and Dad.)"
            "(Still, I'll tell her when I see her next time.)"
            jump afterpicture
label afterpicture:
    scene 16miyuki01
    miyuki "I'm sorry about that, it's one of the contractors for the project."
    main "There's more than one?"
    scene 17miyuki01
    miyuki "Well, they're all competing for the project."
    miyuki "Who wouldn't love to be in charge of transforming a sleepy town into a tourist attraction."
    miyuki "It helps them get more contracts."
    scene 18miyuki01
    miyuki "I intended for my boyfriend to take the contract."
    main "Boyfriend?"
    scene 19miyuki01
    miyuki "Yeah, Ethan. Ambitious guy. We've talked about developing this plot of land for years."
    scene 20miyuki01
    miyuki "But..I don't know. I think he's getting old and stuck in his ways."
    miyuki "And it's a little expensive. "
    scene 21miyuki01
    miyuki "So I'm talking to other contractors. Encourage a little competition."
    miyuki "There's nothing wrong with a little competition."
    scene 22miyuki01
    miyuki "I bet his wife is trying to impress him."
    main "You're ok dating a married man?"
    scene 23miyuki01
    miyuki "One that's stuck in a loveless marriage with a greedy bitch?"
    miyuki "It's not that bad when you look at it from my point of view."
    scene 24miyuki01
    miyuki "Ethan and I..we just get each other."
    $miyukievent01.status_completed("not completed")
    scene 25miyuki01
    miyuki "Though he is lacking in the...sexual department."
    main "Maybe he needs some competition."
    scene 26miyuki01
    miyuki "You catch on quick!"
    scene 27miyuki01
    miyuki "Would you like to compete against an older, wealthy man little boy?"
    "(She has no idea that Ethan is my dad.)"
    "(I could use this to my advantage.)"
    menu:
        "(Accept.)":
            main "Are you that desperate for attention?"
            scene 28miyuki01
            miyuki "Trying to gaslight me? That won't work on me, little boy."
            miyuki "You asked first."
            scene 29miyuki01
            miyuki "I'll be waiting."
            "(She's impatient.)"
            scene 30miyuki01
            "(But I could use this to my advantage.)"
            jump miyukifuck
        "(Refuse.)":
            main "Not into older women."
            scene 31miyuki01
            miyuki "Why not? We're more experienced. And you don't have to worry about that little thing called pregnancy."
            main "No thanks. I came here to work, not to fuck around."
            scene 32miyuki01
            miyuki "Then get to work. Your desk is over there."
            scene 33miyuki01
            miyuki "If you change your mind, I'll be in my office."
            main "Sure."
            scene 34miyuki01
            "(I've gotten what I needed from her.)"
            "(I could just leave, I doubt she cares.)"
            menu:
                "(Take up her offer.)":
                    "(But I could blackmail her.)"
                    "(And piss off Dad.)"
                    scene 35miyuki01
                    "(Why not.)"
                    scene 36miyuki01
                    miyuki "I knew you would change your mind."
                    miyuki "I'm irresistable."
                    jump miyukifuck
                "(Leave.)":
                    jump mcleavesmiyukisoffice
label miyukifuck:
    scene 37miyuki01
    $choices.append(miyukifuck)
    miyuki "Did you lock the door?"
    main "Yeah."
    scene 38miyuki01
    main "Wow, you're really horny."
    miyuki "I haven't had any for two weeks."
    miyuki "Don't keep me waiting."
    scene 39miyuki01
    "(Shit I need to be quick.)"
    "(There. I hope she doesn't notice.)"
    scene 40miyuki01
    miyuki "Oh..oh my."
    miyuki "I think I lucked out asking you to come here."
    scene 41miyuki01
    miyuki "This is impressive."
    scene 42miyuki01
    "(Her mouth feels great.)"
    "(I can't believe this is happening.)"
    scene 44miyuki01
    "(I'm going to fuck Dad's girlfriend.)"
    scene 45miyuki01
    miyuki "Come on, fuck me big boy."
    scene miyukifuck01
    miyuki "That's it, fuck me."
    miyuki "I want to feel that big cock inside of me."
    miyuki "Fuck, that feels so good."
    scene 46miyuki01
    main "Fuck!"
    miyuki "Oh you naughty little boy."
    scene 47miyuki01
    miyuki "But you're good."
    scene 48miyuki01
    miyuki "I think I can get used to you."
    scene 49miyuki01
    "(I need to check my phone.)"
    scene 53miyuki01
    "(Shit, I don't think I got anything.)"
    "(Hmmm. Quality is terrible but it shows what's important.)"
    scene 50miyuki01
    miyuki "Don't tempt me."
    main "Oh, I'm sorry."
    scene 51miyuki01
    miyuki "I have an appointment soon. Even though I really like you, I don't trust you."
    miyuki "You're going to have to leave."
    main "Yeah sure."
    scene 52miyuki01
    miyuki "Do come back..tomorrow preferably."
    miyuki "Good bye, my little stallion."
    jump mcleavesmiyukisoffice
label mcleavesmiyukisoffice:
    scene 54miyuki01
    "(That was awkward.)"
    "(One thing I know for certain- Dad is cheating on Mom with her.)"
    "(And the main reason for the project.)"
    "(I just have to figure out what to do with the information.)"
    jump freeroamch3







