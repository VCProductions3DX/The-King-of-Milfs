label reinaevent05:
    scene black
    scene 01reina05 with fade
    play sound "sfx/Reina5Restaurant.ogg"
    "(I hope everything goes as planned.)"
    scene 03reina05
    "(What's taking her so long?)"
    stop sound
    scene 02reina05
    "[player_name]?"
    scene 06reina05 with Pause(2)
    scene 08reina05
    "(Mom looks completely different.)"
    scene 10reina05
    reina " Hello [player_name]."
    reina "My baby boy looks so handsome."
    scene 07reina05 with fade
    "(This is awkward.)"
    scene 09reina05
    reina "So, what do you think of this place?"
    main "It's fancy."
    scene 11reina05
    reina "It certainly is. The best restaurant in town."
    reina "I can't believe three months have passed since we've last seen each other."
    scene 09reina05
    reina "Like this, anyway."
    scene 12reina05
    reina "I want to enjoy it before I have to go back to work again."
    show 14reina05 with Pause(3)
    scene 12reina05
    reina "And the wine is delicious."
    scene 13reina05
    "(She's not wearing her wedding ring.)"
    "(How long has she not worn it?)"
    scene 16reina05
    reina "You look so much healthier."
    reina "What have you been doing lately?"
    "(What should I talk about?)"
    if reinaevent05.status == "completed":
        main "Nothing much, really."
        scene 15reina05
        reina "Are you by yourself all of the time?"
        main "No, I visit other people."
        reina "I'm glad."
        reina "I do care about you, [player_name]."
        reina "I want you to stay sober."
        scene 17reina05
        reina "Do you mind helping your aunt Jenni move to her new apartment tomorrow?"
        reina "I don't want her to move everything by herself."
        main "Sure."
    else:
        menu:
            "Talk about Briana. (Briana Love + 3)":
                main "I'm helping Briana with her new career."
                $BrianaC.love_up(3)
                scene 15reina05
                reina "Is that so? What has she decided to do?"
                main "MMA- Mixed Martial Arts."
                scene 17reina05
                reina "How is that different from boxing?"
                main "She's able to do a lot more."
                reina "I'm worried about her."
                reina "I don't want her to get seriously injured."
                reina "She has her whole life ahead of her. I don't want it cut short due to this fighting."
                main "I'll keep her safe, I promise."
            "Talk about Penny. (Penny Love + 3)":
                main "Penny is getting really at playing the guitar."
                $PennyC.love_up(3)
                scene 15reina05
                reina "Really? I never her practice when I'm home."
                reina "Is she good?"
                main "In the beginning she wasn't, but she's getting hang of it."
                main "She records herself all of the time and does a few livestreams."
                scene 16reina05
                reina "Really? Can I see them?"
                main "Penny is a bit shy about anyone in the family watching her perform.."
                reina "Why not?  It's just music, right?"
                main "It is."
                scene 17reina05
                reina "I'll respect her wishes for now. But if anything bad happens to her-"
                main "Don't worry, I'll protect her."
            "Talk about Jenni. (Jenni Love + 3)":
                $JenniC.love_up(3)
                main "Aunt Jenni stops by the cottage to check on me."
                reina "How nice of her."
                main "Last week we went shopping, again."
                scene 15reina05
                reina "Oh I'm sorry she dragged on one of her shopping sprees."
                reina "I asked her to look after you, not make her personal assistant."
                main "I don't mind, really."
                scene 17reina05
                reina "Are you helping her to her new apartment move tomorrow?"
                main "Yes."
                scene 16reina05
                reina "Thank you, [player_name]."
            "Talk about Sabrina. (Sabrina Love + 3)" if sabrinaevent02.status== "completed":
                main "I ran into an old friend a few weeks ago."
                $SabrinaC.love_up(3)
                scene 15reina05
                reina "Who are they? Did they offer you any drugs?"
                main "No-no."
                reina "Is it a girl?"
                main "Yes."
                scene 16reina05
                reina "What's her name?"
                main "Sabrina. She runs a store in town."
                reina "Sabrina. I think I've seen that girl around town. Bright pink hair and freckles?"
                main "Yes."
                scene 17reina05
                reina "I hope she doesn't mind you going on a date with an older woman like myself."
                main "No we're not like that."
                scene 16reina05
                reina "Are you sure she thinks the same way?"
                reina "Maybe next time properly ask her out."
    scene 20reina05
    "Here is your soup and salad."
    reina "Soup and salad?"
    scene 18reina05
    reina "What did you order for us?"
    main "A 5-course meal. Chef's specialty."
    scene 19reina05
    reina "A five course meal."
    scene 21reina05
    reina "I haven't eaten this much in years."
    scene 23reina05
    reina "I'm so full."
    scene 24reina05
    reina "So, what's next on the menu?"
    stop music
    reina "What's that sound?"
    scene reinafireworks
    reina "Fireworks?"
    main "It's something new."
    scene 26reina05
    main "Is something wrong?"
    reina "It's nothing. It just reminded me of your father."
    scene 27reina05
    reina "He proposed to me underneath the fireworks."
    scene 29reina05 with fade
    reina "Thank you [player_name] for this dinner and the fireworks show."
    scene 28reina05
    reina "Would you like to escort me home?"
    scene 30reina05
    "(She seems a little happier now.)"
    scene 31reina05 with fade
    reina "And we're home."
    scene 32reina05
    reina "I'm going to change into something more comfortable."
    scene 33reina05
    reina "I'm back."
    scene 34reina05
    reina "My feet hurt so much from those shoes."
    scene 35reina05
    reina "This feels much better."
    show 36reina05 with Pause (2)
    scene 37reina05
    reina "Is there something wrong?"
    main "No."
    scene 38reina05
    reina "One day you will comfortable with telling me everything that's on your mind."
    reina "I guess it's not today."
    scene 39reina05
    reina "I'm so tired."
    scene 41reina05
    reina "I haven't had a chance to rest since coming home."
    reina "This couch feels so comfortable."
    scene 45reina05
    reina "[player_name]."
    scene 40reina05
    reina "Do you think it is possible to find love a second time?"
    scene 42reina05
    reina "This past month I've had a lot of time to myself."
    reina "And I've decided to visit a lawyer."
    main "By yourself?"
    scene 46reina05
    reina "Well yes but-would you come with me? Please? As a voice of reason."
    main "Of course."
    scene 48reina05
    reina "I reflected on everything that's happened since you've came home."
    reina "No, before that."
    scene 47reina05
    reina "I've caused so much for pain and turmoil for everyone trying to keep this marriage alive."
    reina "Our family in tact."
    scene 46reina05
    $reinaevent05.status_completed("not completed")
    reina "I'm just scared about what happens if I go through with this."
    scene 49reina05
    reina "I'll be all alone, by myself."
    reina "Your sisters will leave, Jenni will move out..it will just be me."
    main "I'll stay with you if you want me to."
    scene 50reina05
    reina "That's kind of you, dear."
    scene 51reina05
    reina "I'm just thinking about my own selfish needs."
    scene 52reina05
    reina "That's something you don't need to know."
    scene 53reina05
    reina "I'm going to bed. There are blankets in the pantry."
    scene 54reina05
    reina "Goodnight, [player_name]."
    jump freeroamch3