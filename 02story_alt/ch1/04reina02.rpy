label reinaevent02:
    scene 02reina02 with fade
    reina "Good morning, [player_name]."
    main "Good morning, Mom."
    scene 01reina02
    reina "Did you sleep well last night?"
    main "I did."
    scene 03reina02
    reina "These boxes weren't here before, did you go shopping yesterday?"
    main "No, Camilla gave them to me."
    scene 04reina02
    reina "How nice of her."
    scene 05reina02 with fade
    reina "Your Aunt Jenni is dying to see you again. The last time she did, you were a little kid."
    main "How is she?"
    reina "She's adjusting."
    main "What happened?"
    reina "She recently got divorced. Because she doesn't have any children, she only got alimony and nothing else."
    reina "She's staying with me until she gets back on her feet."
    scene 06reina02
    main "This place is huge."
    reina "We bought it two years ago. It overlooks the ocean and there's a nice breeze. "
    scene 07reina02
    reina "We're home!"
    scene 08reina02
    jenni "[player_name]! There you are! You're so big now!  Come give your Aunt Jenni a hug."
    scene 09reina02
    jenni "It's so good to see you again."
    scene 10reina02
    jenni "How are you feeling? Are you hungry? Thirsty? "
    main "A little thirsty. "
    jenni "Well so am I. I think your mother is as well. "
    jenni "There's a pitcher of punch in the fridge. Be a dear and bring it out for us, will you? "
    scene 12reina02
    reina "How long do you plan on staying here?"
    reina "And why are you still dressed in pajamas?"
    scene 13reina02
    jenni "I'm not sure. Months, a few years, maybe."
    jenni "And why should I be dressed up? Why are {i}you{/i} dressed up? It's your day off. Wear something more relaxing."
    scene 14reina02
    reina "Jenni-"
    jenni "What's the special occasion? Are you finally happy that your son is home?"
    scene 15reina02
    reina "I have to sell that cottage within a year."
    jenni "Do you?"
    reina "You wouldn't understand. We're in a housing bubble right now. We have to sell when the market's hot. "
    jenni "So?"
    reina "He's going to need a place to stay. He just got out of rehab."
    scene 16reina02
    jenni "And how is that my fault?"
    jenni "{i}You're{/i} the one who let Ethan kick him out of the house."
    scene 17reina02
    jenni "If I were here, I wouldn't permit it to happen. He's my nephew after all."
    jenni "Lucky for you, I do have enough money to buy a small house of my own. Who knows, maybe a nice little shack in the woods is what I need after all of these years."
    scene 20reina02
    jenni "[player_name]? What's taking you so long, dear? We're dying of thirst here."
    scene 21reina02
    jenni "So, how do you like Sierra Beach so far?"
    main "I-I don't know. It's kind of boring."
    jenni "We'll have to change that! There are so many nice beaches around here."
    scene 22reina02
    jenni "Mmm..delicious."
    scene 24reina02
    jenni "Are you looking for a job, [player_name]?"
    jenni "Or are you going to go back to school?"
    scene 23reina02
    reina "He's just out of rehab, Jenni."
    scene 25reina02
    jenni "And he will be back in there if he isn't kept busy."
    jenni "That's what drugs do. They will lure you back into its trap if you're not careful. "
    jenni "I could use some company. How about we hang out and explore the town tomorrow?"
    main "Yeah, sure."
    scene 24reina02
    jenni "Have you talked to your sisters?"
    reina "Jenni-"
    scene 26reina02
    jenni "Here you go, being overbearing again, Reina."
    jenni "[player_name] is an adult now. He can do things without your constant supervision."
    jenni "Besides, your sisters want to see you."
    main "They do?"
    scene 24reina02
    jenni "Of course they do. Penny is upstairs in her room. Briana is at the boxing gym- where is it, Reina?"
    reina "It's near the cottage."
    jenni "Go visit them. And try to get on their good side."
    scene 28reina02
    jenni "Time for my midday nap."
    reina "Jenni, you just woke up."
    jenni "Let a divorced woman rest, Reina."
    scene 30reina02
    jenni "Nice seeing you again,sweety."
    jenni "I'll swing by the cottage tomorrow and pick you up."
    scene 31reina02
    jenni "It will be like old times again, just you and I."
    scene 32reina02 with fade
    main "Mom? Is something wrong?"
    reina "No...no...she always does this."
    reina "She always finds a way to make me look bad."
    scene 33reina02
    $reinaevent02.status_completed("not completed")
    reina "I'm not a bad mother, am I?"
    main "No, I don't think so."
    reina "You were always my favorite, you know."
    reina "Your father said I was too soft. That I needed to be tougher on you like I was with your sisters."
    reina "But then you would alienate me too."
    scene 34reina02
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
        reina "I'm sorry that I let your father kick you out of the house."
        reina "I'm truly sorry."
        scene 41reina02
        reina "I want to be better than this. I've spent so much of my time advancing my career that I have neglected the one thing that matters- my own family."
        reina "If you need me for anything, please let me know.  Don't hesitate to call me, even if you want me to spend the night here with you."
        scene 42reina02
        reina "I care about you and I want you to get better and have a different life than before."
        scene 43reina02
        "(She's being a bit clingy, but her body feels so soft and warm.)"
        main "Thanks Mom, I'll keep clean, I promise."
        scene 44reina02
        reina "I'll see you later."
        reina "Don't hesitate to call if you need anything."
        main "I won't."
        jump freeroamch1



    


