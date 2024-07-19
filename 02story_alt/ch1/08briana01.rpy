label brianaevent01:
    scene 01briana01 with fade
    play sound "sfx/TrainingPunchingBag.ogg"
    "(This gym is huge.)"
    "(Is that Briana?)"
    "(She used to be so tiny.)"
    scene 03briana01
    "(She's changed in seven years.)"
    scene 04briana01
    briana "Hah!!"
    scene 05briana01
    main "Excuse me."
    scene 06briana01
    "(She's not paying any attention.)"
    scene 07briana01
    main "Hello??"
    scene 08briana01
    briana "None of the trainers are here today."    
    stop sound
    scene 09briana01 
    briana "[player_name]????"
    scene 10briana01
    briana "[player_name]!!!!"
    scene 11briana01
    main "Hello to you too."
    scene 12briana01
    briana "It's really you."
    briana "My big brother's gotten fat."
    scene 13briana01
    main "That's rude."
    briana "Watch who you're talking to!"
    scene 14briana01
    main " Ow, shit that hurt."
    main "You know how to pack a punch."
    scene 15briana01
    briana "Hit me again, I dare you."
    main "I'm sorry Briana."
    "(She hasn't lost her temper.)"
    scene 16briana01
    briana "You're back."
    briana "And..you're clean. I don't smell any weed on you."
    main "I haven't smoked weed in months."
    scene 17briana01
    briana "What about other drugs, [player_name]?"
    main "I'm clean, I promise. It was part of the deal with Mom and Dad."
    scene 18briana01
    briana "But you're not living with us, are you?"
    main "No, I'm staying at one of Mom's properties."
    briana "Of course Dad would keep you out of the house."
    briana "He's always hated you."
    briana "I can't concentrate any more. Let's go get something to eat."
    main "Right now?"
    scene 20briana01
    briana "Yeah, I need to change first but let's go."
    briana "I have so much to tell you."
    "(She's still as energetic as ever.)"
    scene 21briana01 with fade
    main "So, what happened after I left?"
    scene 22briana01
    briana "Dad's business was going well. He started getting jobs across the country and he was away from home weeks at a time."
    briana "Mom got really lonely, so she decided to take some real estate estates and get her license."
    briana "And I..got into a lot of trouble in high school."
    main "Uh oh."
    scene 23briana01
    briana "There was a group of girls who bullied me all of the time. One day they grabbed my hair and I punched back."
    briana "I ended up breaking her nose. It looked so digusting."
    briana "But it felt so good."
    main "I bet Mom wasn't pleased."
    scene 24briana01
    briana "Yeah, I was suspended for 2 weeks. Mom was really upset, but Dad was intrigued. So he signed me up for boxing classes."
    briana "Which turned into matches and eventually 3 championships."
    main "Wow, that's amazing."
    scene 25briana01
    briana "Yeah, it is. Well, save for the overprotective father part."
    briana "He's not going to like what I'm going to do next."
    scene 26briana01
    briana " I'm retiring from boxing."
    main "What? But you're still young."
    scene 27briana01
    briana "And my competitors are younger."
    briana "Also, I learned my dad had a lot of ...say in my matchups."
    briana "If he didn't think I could beat an opponent, he would have the match cancelled."
    briana "It made me feel like a cheater. Like my titles were bought, not earned."
    scene 28briana01
    briana "I want to be able to fight anyone I want, on my own terms."
    briana "So I'm quitting."
    scene 29briana01
    briana "Do you think I'm making the right decision, [player_name]?"
    if brianaevent01.status == "completed":
        main "It's your decision and your life, Bri. I'll support you no matter what."
        scene 30briana01
        briana "Thanks, [player_name]."
    else:
        menu:
            "It's your life, Briana.(+2 Briana Love)":
                $BrianaC.love_up(2)
                main "You should do what you want."
                scene 30briana01
                briana " Thanks [player_name], I knew I could trust my older brother."
            "I'll stand by you no matter what. (+2 Briana Trust)":
                $BrianaC.trust_up(2)
                scene 30briana01
                briana "Aww, thanks [player_name]."
    main "Have you thought about what you want to do?"
    scene 31briana01
    briana "Hmm, I don't know."
    briana "At first I thought about Mixed Martial Arts, but I think I'm a little too heavy for that."
    scene 32briana01
    briana "So wrestling maybe? Or perhaps bodybuilding? I think that will suit me better."
    briana "What do you think?"
    if brianaevent01.status=="completed":
        main "You should do what you want, Briana."
        scene 33briana01
        briana "Yeah, you're right."
    else:
        menu:
            "You should do what you want.(+2 Briana Trust)":
                scene 33briana01
                $BrianaC.trust_up(2)
                briana "I don't want to give up fighting."
                briana "So maybe I can lose enough weight to do MMA."
            "Wrestling suits you.(+Wrestling Choice)":
                scene 33briana01
                $choices.append(wrestlingsuggest)
                briana "Wrestling, huh?"
                briana "I do like a good fight. But the crowds, the lights..I don't know."
                main "What about acting?"
                briana "Acting- it's still fighting, [player_name]."
                briana "I'll think about it."
            "I can picture you as a bodybuilder.(+Bodybuilder Choice)":
                scene 33briana01
                $choices.append(bodybuildersuggest)
                briana "A bodybuilder."
                briana "I would be under so much scrutiny."
                briana "Even the slightest imperfection would be noticed. I'm just not sure."
                briana "I need some time to think about it."
    scene 34briana01
    briana "Whew, I'm stuffed."
    scene 35briana01
    briana "Ugh, I don't want to go home just yet."
    main "Because of Dad?"
    scene 36briana01
    briana "Yeah. And Mom. And Aunt Jenni."
    briana "It's so loud there sometimes."
    briana "Wish I could spend the night at your place."
    main "There isn't much there."
    scene 37briana01
    briana "Not even a bed?"
    main "There is, but not much else."
    briana "Aww. I bet there isn't any internet there either."
    scene 38briana01
    briana "I guess I'll go back home."
    scene 39briana01
    briana "You're finally home, [player_name]."
    scene 40briana01
    briana "We should hang out again sometime."
    $brianaevent01.status_completed("not completed")
    main "Yeah, sure. Will you be at the gym?"
    briana "Always."
    briana "But I'll call you next time, okay?"
    main "Sure."
    scene 41briana01
    briana "Bye, [player_name]."
    jump freeroamch1






