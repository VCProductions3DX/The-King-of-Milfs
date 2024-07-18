
label reinaevent02:
    scene 02reina02 with fade
    reina "Good morning, [player_name]."
    scene 01reina02
    reina "Did you sleep well last night?"
    main "I did."
    scene 03reina02
    reina "These boxes weren't here before, did you go shopping yesterday?"
    main "No, Camilla gave them to me."
    scene 04reina02
    reina "It's time to see my home-our home. My sister Jenni wants to meet you. "
    main "Jenni? I've never met her."
    reina "No, you haven't. She was overseas when you came into our family."
    scene 05reina02 with fade
    reina "My younger sister Jenni is a natural beauty. She graduated high school early and become a model."
    reina "She travelled the world and experienced things that I can only dream of."
    reina "I must warn you, she is a bit chatty. And flirtatious."
    scene 06reina02
    main "This place is huge."
    reina "We bought it two years ago. It overlooks the ocean and there's a nice breeze. "
    scene 07reina02
    reina "We're back."
    scene 08reina02
    jenni "Hey."
    scene 11reina02
    jenni "So this is..."
    reina "Anna's son, [player_name]."
    jenni "Anna...I don't remember her."
    reina "She and her boyfriend passed away in an accident years ago.  I decided to take him in and raise him as a favor."
    jenni "That's so like you."
    jenni "Are you thirsty?"
    main "Yes."
    jenni "So am I. There's some punch in the fridge. Bring it out here, will you?"
    scene 12reina02
    reina "How long do you plan on staying here?"
    scene 13reina02
    jenni "I'm not sure. A couple of months. A few years, maybe."
    reina "Jenni-"
    jenni "Reina, both of your daughters are grown up."
    jenni "I'm sure that in a few years, this place will become one huge empty nest and you'll be yearning for company."
    scene 15reina02
    reina "I have to sell that cottage within a year."
    jenni "Do you?"
    reina "You wouldn't understand. We're in a housing bubble right now. We have to sell when the market's hot. "
    jenni "So?"
    reina "He's going to need a place to stay. He just got out of rehab."
    scene 16reina02
    jenni "And how is that my problem?"
    scene 17reina02
    jenni "You're the one who let Ethan kick him out of the house."
    scene 18reina02
    jenni "If it was me, I wouldn't have kicked him out."
    scene 19reina02
    jenni "I would have least found [player_name] a place to stay and a job."
    jenni "Lucky for you, I do have enough money to buy a small house of my own. Who knows, maybe a nice little shack in the woods is what I need after all of these years."
    scene 20reina02
    jenni "[player_name]? What's taking you so long? We're dying of thirst here."
    scene 21reina02
    jenni "So, how do you like Sierra Beach so far?"
    main "I-I don't know. It's kind of boring."
    jenni "We'll have to change that! There are so many nice beaches around here."
    scene 22reina02
    jenni "Mmm..delicious."
    scene 24reina02
    jenni "Are you looking for a job, [player_name]?"
    reina "He's just out of rehab, Jenni."
    scene 23reina02
    jenni "And he will be back in there if he isn't kept busy."
    jenni "That's what drugs do. They will lure you back into its trap if you're not careful. "
    scene 24reina02
    jenni "I could use some company. I'll pay you for your time. How does that sound?"
    main "Great. Thanks."
    scene 26reina02
    jenni "And that, Reina, is how you engage with your adult kids-even the adopted ones."
    reina "Jenni-"
    scene 25reina02
    jenni "You spend too much time working and not enough time with your family."
    jenni "You have this big huge mansion and it feels so empty."
    reina "Jenni, I'm trying. This is the first step."
    jenni "And the last if you don't follow through."
    scene 28reina02
    jenni "Time for my midday nap."
    reina "Jenni, you just woke up."
    jenni "Let a divorced woman rest, Reina."
    scene 29reina02
    jenni "It was nice meeting you,[player_name]."
    jenni "I'll swing by the cottage tomorrow and we'll spend the whole day together."
    jenni "I'm sure we'll have plenty of time to get to know each other."
    stop music
    scene 32reina02 with fade
    $reinaevent02.status_completed("not completed")
    reina "She always does this."
    reina "She always finds a way to make me look bad."
    scene 33reina02
    reina "I'm not a bad mother, am I?"
    reina "Just look. One daughter is constantly away and the other refuses to talk to me."
    main "Where are they, Penny and Briana?"
    scene 34reina02
    reina "Briana is at the gym, in the shopping area we passed by earlier."
    reina "Penny is upstairs in her room right now. But later on she'll go to the skatepark."
    scene 35reina02
    reina "Do you want to see her now?"
    menu: 
        "Yeah, I'll go upstairs.":
            jump pennyevent01
        "No, I'll talk to her later.":
            scene 36reina02
            reina "I suppose you don't want to stay here any longer, do you?"
            main "Not really."
            reina "Let's go back, then."
            jump returnhomech1
    label afterpennyvisit:
        scene 37reina02
        reina "So, how is she?"
        main "A lot different than what I remember."
        reina "True. She was so sweet and innocent. Then a year ago she dyed her hair, got a lot of piercings and became cold and distant."
        reina "Anytime I try to talk to her, she cuts it short and goes to her room."
        reina "I wish I knew what was wrong with her. Or me."
        scene 36reina02
        reina "I suppose you don't want to stay here any longer, do you?"
        main "Not really."
        reina "Let's go back, then."
        jump returnhomech1
    label returnhomech1:
        scene 38reina02 with fade
        reina "[player_name]."
        main "Yes?"
        scene 39reina02
        reina "I'm sorry."
        reina "I'm sorry I wasn't there for you when you needed me the most. "
        scene 40reina02
        reina "I'm sorry that I let my husband kick you out of the house."
        reina "I'm truly sorry."
        scene 41reina02
        reina "I want to be better than this. I've spent so much of my time advancing my career that I have neglected the one thing that matters- my own family."
        reina "If you need me for anything, please let me know.  Don't hesitate to call me, even if you want me to spend the night here with you."
        scene 42reina02
        reina "I care about you and I want you to get better and have a different life than before."
        scene 43reina02
        "(She's being a bit clingy, but her body feels so soft and warm.)"
        main "Thanks Reina. I'll keep clean, I promise."
        scene 44reina02
        reina "I'll see you later."
        reina "Don't hesitate to call if you need anything."
        main "I won't."
        jump freeroamch1

   