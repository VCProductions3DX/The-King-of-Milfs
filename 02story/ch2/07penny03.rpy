label pennyevent03:
    scene 01penny03 with fade
    penny "Hey [player_name]."
    main "Hey Penny."
    scene 02penny03
    penny "What happened to you? Why do you have a cast on your arm?"
    main "I was attacked."
    penny "By my dad?"
    main "No. By strangers."
    scene 03penny03
    penny "That sucks."
    penny "So what happened between my parents? How long did they argue after I left?"
    main "Pretty long. Ethan told Reina he never loved her."
    penny "He said that?"
    main "Yeah."
    scene 04penny03
    penny "How did she react?"
    main "She cried a lot."
    penny "Do you think she will divorce?"
    if divorcesuggest in choices:
        main "I told her to."
        scene 05penny03
        penny "You told her?"
        penny "Pretty bold there, [player_name]."
    else:
        main "I don't know."
    scene 06penny03
    penny "I don't think my mom's the type to divorce  my dad."
    penny "She's very old-fashioned and traditional."
    scene 07penny03
    penny "{i}'No sex before marriage.'{/i} Blah blah blah."
    penny "She doesn't realize it's the 21st century."
    scene 08penny03
    penny "I think we would all be happier if they would divorce."
    menu:
        "Lecture her.":
            main "What are you doing?"
            scene 09penny03
            penny "What does it look like?"
            penny "It's just a vape."
            scene 10penny03
            penny "Are you going to lecture me?"
            penny "I thought at least you would understand."
            penny "It's not even that bad. No smell, no stains."
            main "It can get worse."
            scene 11penny03
            penny "It's not like weed or anything you've tried."
            penny "I'm not like you."
            scene 13penny03
            penny "I can handle myself."
        "Sympathize with her. (Penny Trust + 3)":
            main "I wish I had that when I was your age."
            scene 09penny03
            $PennyC.trust_up(3)
            penny "I bet my dad would've treated you the same, though."
            scene 10penny03
            main "Why did you start?"
            scene 11penny03
            penny "I have my reasons, ok?"
            penny "Mostly my dad just berating my existence."
            scene 12penny03
            main "That's it?"
            main "Did he hit you?"
            penny "No. Just called me fat all of the time."
            penny "I barely eat as it is."
            main "Reina didn't intervene?"
            scene 13penny03
            penny "Mom was too busy studying and working."
            penny "Even when I tried to tell her, she was too scared and too tired to do anything."
    scene 14penny03
    penny "It's not like anyone cares about me, anyway."
    penny "I just think about what I could be doing if Mom and Dad actually gave a shit about me."
    main "What did you want to do?"
    scene 15penny03
    penny "I wanted to learn music. To play an instrument and eventually start my own band."
    penny "But neither Mom nor Dad wanted to pay for lessons, sheet music or even an instrument ."
    penny "When I asked, it was always '{i}We don't have enough money.{/i}' or '{i} It's a waste of time{/i}' "
    scene 16penny03
    penny "Eventually I just stopped asking. I just began spending time at the records store. Then the skatepark."
    penny "Everyone was vaping so I just picked it up."
    main "That's still not a reason to vape."
    scene 17penny03
    penny "It's the only thing that stops me from just ending it all sometimes."
    play sound "sfx/cellvibe.ogg"
    main "Is that Reina?"
    stop sound
    scene 25penny03
    penny "No, it's just my email."
    penny "Hmm, my video is getting views."
    if ch1pennyvideoupload in choices:
        penny "Thanks for uploading it."
        $PennyC.love_up(2)
        main "You're welcome."
    else:
        penny "I guess it was a good idea uploading it."
    scene 27penny03
    penny "I need to upload more videos."
    penny "Then I'll be famous on my own."
    scene 28penny03
    penny "Will you help me, [player_name]?"
    penny "You took those videos, you can help me take more."
    penny "Please, please???"
    if pennyevent03.status== "completed":
        main "I can."
        scene 23penny03
        penny "Really?"
        main "If you stop vaping."
        scene 29penny03
        penny " Ugh, fine, I'll stop."
        scene 24penny03
        penny "So what kind of videos should I do?"
        penny "More skateboarding? Or should I play some pranks on people?"
        main "Both. And whatever else you want."
        scene 22penny03
        penny "Whatever else."
        main "If you start to make money from it, you can buy a musical instrument and record yourself practicing it."
        penny "Oh my god, you're right, [player_name]."
        penny "I can pay for my own music lessons."
        scene 30penny03
        penny "Get well soon, [player_name]."
        penny "I'll upload a few more videos while you're still recovering."
        main "Thanks Penny."
        penny "Bye, I'll stop by later."
        scene 31penny03 with Pause (1)
        jump readtexts
    else:
        menu:
            "If you stop vaping. (Penny Love +1, Penny Trust + 2)":
                scene 29penny03
                penny "Really?"
                main "I don't think it fits you, Penny."
                $PennyC.love_up(1)
                $PennyC.trust_up(2)
                main "Plus, it might not be advertiser-friendly."
                penny "You have a point."
                $pennyevent03.status_completed("not completed")
                scene 30penny03
                penny "I'll quit. Just for you."
                penny "I'll come up with video ideas."
                main "What about more skateboarding?"
                penny "Mmmhmm..."
                main "Then after that, we can buy whatever instrument you want."
                scene 23penny03
                penny "Even a guitar? Or a drum set?"
                main "Yes."
                penny "Oh my god, that sounds awesome. Then record playing it, making songs."
                penny "I already have the perfect outfit for those videos."
                scene 19penny03
                penny "I can finally be a rock star!"
                main "Penny-"
                scene 24penny03
                penny "I'm going to record a few videos while you get better."
                penny "But text me when you're all healed."
                main "I will."
                scene 30penny03
                penny "Thanks [player_name]. I'll stop vaping for good."
                penny "I'll see you later."
                scene 31penny03 with Pause(1)
                stop music
                jump freeroamch2
            "Yes, when I can. (Penny Love + 2, Penny Trust + 1)":
                scene 24penny03
                penny "You will?"
                penny " You're the best, [player_name]."
                $PennyC.love_up(2)
                $PennyC.trust_up(1)
                scene 22penny03
                penny "Hmmmm, what should I make."
                penny "I guess more skateboarding videos while you recover."
                penny "But after that-"
                main "What about music videos?"
                scene 29penny03
                penny "I need an instrument, duh."
                main "We can buy one- once the money comes in."
                penny "Oh my god, you're right."
                $pennyevent03.status_completed("not completed")
                scene 27penny03
                penny "I can buy a guitar- pay for music lessons- upload it online."
                penny "I can be a rockstar."
                main "Penny?"
                scene 30penny03
                penny "I got carried away for a bit. I'm sorry, [player_name]."
                penny "It's time for me to go. I'll stop by sometime next week."
                penny "Get well soon, [player_name]."
                scene 31penny03 with Pause (1)
                stop music
                jump readtexts