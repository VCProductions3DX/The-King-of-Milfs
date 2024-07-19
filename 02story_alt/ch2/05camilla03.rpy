label camillaevent03:
    scene 02camilla03
    camilla "You seem to be better."
    "(Shit, my back hurts.)"
    camilla "Or did you push yourself too hard?"
    camilla "Here, let me help you."
    scene 03camilla03
    main "Thanks, Camilla."
    camilla "Did you need anything? Any medicine, do you need your cast changed?"
    main "No, I'm fine Camilla."
    if reinacare in choices:
        main "Mom helped me last night."
    else:
        main "Aunt Jenni helped last night."
    scene 04camilla03
    camilla "Did she?"
    main "Yeah, I'm doing a lot better."
    camilla "And nothing happened between the two of you?"
    menu:
        "That's none of your business.":
            camilla "Then perhaps I'll help you put up blinds."
            scene 05camilla03
            camilla "Much better."
        "No.":
            camilla "Are you sure?"
            camilla "It certainly looked like it. Because you had no blinds."
            scene 05camilla03
            camilla "This blocks out everything."
        "Were you peeping on us last night?":
            camilla "Maybe."
            camilla "You didn't put my blinds up, so anything that happened last night, anyone could see."
            scene 05camilla03
            camilla "There we go, much better."
    main "What did you see?"
    if reinacare in choices:
        scene 07camilla03
        camilla "A young man getting some extra loving from his mother."
        main "She was drunk!"
        scene 08camilla03
        camilla "And yet you didn't stop her."
        main "I did, actually."
        scene 09camilla03
        camilla "I know what I saw."
        main "She fell asleep on my lap."
        main "I'm not a creep or a weirdo."
        scene 10camilla03
        camilla "There's nothing weird about getting close to your mother."
        camilla "Between the two of us-"
        scene 11camilla03
        camilla "Did you think about it?"
        menu:
            "No.":
                main "Mom is important to me."
                main "And that's sick."
                scene 12camilla03
                camilla "Aren't you a good boy."
                jump camillaoffersherself
            "I did.":
                scene 13camilla03
                camilla "And did it turn you on?"
                camilla "The idea of fucking your own mother?"
                camilla "Would you have done it if she was sober?"
                main "What?"
                camilla "Well, would you?"
                main "No, you're crazy."
                jump camillaoffersherself
    else:
        scene 07camilla03
        camilla "Someone getting some extra attention from his aunt."
        main "She wouldn't take no for an answer."
        scene 11camilla03
        camilla "But you enjoyed it, didn't you?"
        main "We didn't do anything, I swear!"
        jump camillaoffersherself
label camillaoffersherself:
    scene 14camilla03
    camilla "So you're still sexually frustrated."
    camilla "I can help you relieve of that."
    camilla "It's better than staining the sofa again."
    scene 15camilla03
    camilla "I know you're staring at them."
    camilla "Would you like to see them up close?"
    scene 16camilla03
    "(She's coming onto me.)"
    menu:
        "(Sure.)":
            scene 17camilla03
            "(They're huge.)"
            main "Are they real?"
            scene 18camilla03
            camilla "Why don't you touch them and see how real they are."
            scene 19camilla03
            "(Damn they're soft.)"
            camilla "Nothing wrong with a little nip and tuck."
            scene 20camilla03
            camilla "Someone's hard."
            scene 21camilla03
            camilla "This looks even bigger than I thought."
            scene 22camilla03
            camilla "My tits can't smother them."
            "(Her tits feel good around my cock.)"
            scene 23camilla03
            camilla "You like these big, soft tits, don't you?"
            camilla "I can make it feel as good as my pussy."
            main "Is your ass fake as well?"
            scene 24camilla03
            camilla "No, it's real. You can look for the stretch marks and cellulite for yourself."
            scene 25camilla03
            "(It looks so perfect.)"
            "(I can't see any stretch marks and cellulite.)"
            scene 26camilla03
            camilla "Here, look a little closer."
            "(I can't breathe!)"
            scene 27camilla03
            camilla "I'm just kidding. It's just a fat transfer from my belly."
            camilla "So, which do you like more? My tits or my ass?"
            menu:
                "Tits.":
                    scene 28camilla03
                    camilla "Do you want to cum on them?"
                    main "Yeah."
                    scene camillatitjob
                    $choices.append(camillatj)
                    camilla "Don't hold back, cum all over these big bouncy titties."
                    camilla "Go on, fuck these tits you dirty little boy."
                    camilla "I want you to spray your load all over them."
                    scene 29camilla03
                    main "Fuck!"
                    camilla "Someone made a huge mess."
                    jump aftercamillasex
                "Ass.":
                    scene 30camilla03
                    camilla "Would you like to see it in action?"
                    main "Yeah."
                    scene 31camilla03
                    "(Is she really going to sit on my cock.)"
                    scene camillariding01
                    "(Fuck, her pussy feels good.)"
                    camilla "How does my ass look?"
                    camilla "Is it too big for you to handle?"
                    "(She's grinding on my cock.)"
                    scene camillariding02
                    camilla "You can't last much longer, can you?"
                    camilla "I know you're close."
                    camilla "Cum for me."
                    main "Fuck!"
                    scene 32camilla03
                    camilla "That's it, rub it all over my ass, you naughty boy."
                    jump aftercamillasex
                "No thanks.":
                    scene 33camilla03
                    camilla "You little tease."
                    main "I'm not into older women."
                    camilla "One day you'll see the light."
                    jump aftercamillasex
label aftercamillasex:
    scene 34camilla03 with fade
    main "Is something wrong?"
    camilla "Everything."
    scene 35camilla03
    camilla "Do you mind being a soundboard for me?"
    main "Sure."
    scene 36camilla03
    camilla "My husband and I divorced years ago. I got the house and enough money to start my business. Life was good."
    camilla "But then both of our children moved out. And I've been alone, running my business all by myself."
    main "And how's business?"
    scene 37camilla03
    camilla "Abysmal."
    camilla "If it isn't tourist season, I'm lucky to get a few sales on the weekend."
    camilla "During tourist season, there's a lot of sales...and a lot of theft."
    main "Ew."
    scene 38camilla03
    camilla "And now, that bitch of a city councilwoman wants to turn the entire street into a shopping complex."
    camilla "Well, not just front street. The whole fucking town."
    if camillaevent02.status == "completed":
        main "Why did she ask for your help?"
        scene 39camilla03
        camilla "Because I'm only person standing in her way."
    else:
        pass
    camilla "This is my home. I don't want this small, quaint town turned into an amusement park."
    camilla "At the same time, there are other things I want to do in life. Places to travel, events to see."
    scene 41camilla03
    camilla "Maybe it's time to close shop."
    main "What's stopping you?"
    scene 42camilla03
    camilla "If I, the most vocal person against the the project, close shop, the others will follow."
    camilla "Then all of the places that make Sierra Beach unique will go away. There will be nothing but Starbucks and Targets and-"
    main "Oh."
    camilla "It's the main reason why Sierra Beach broke away from Sierra City."
    menu:
        "You should do what you want, Camilla.":
            main "You only live once."
            scene 43camilla03
            camilla "True."
            camilla "It's a big world out there."
            camilla "That means closing the store."
            scene 44camilla03
            camilla "Will you help me with that?"
            main "Sure."
            camilla "Not now. But in a few months. I need time to prepare."
            $choices.append(camillaclosesstore)
            $camillaevent03.status_completed("not completed")
            scene 45camilla03
            camilla "Thank you, [player_name]."
            jump freeroamch2
        "You should look after this town.":
            scene 46camilla03
            camilla "What are you suggesting?"
            main "Run for office."
            camilla "Run for-"
            $choices.append(camillarunsforoffice)
            $camillaevent03.status_completed("not completed")
            scene 47camilla03
            camilla "There is an election coming up."
            scene 48camilla03
            camilla "Do you think I would make a good politician?"
            main "You care about this town, so you would be perfect for it."
            scene 49camilla03
            camilla "I'll think on it."
            scene 50camilla03
            camilla "Thank you, [player_name]."
            jump freeroamch2




   

    