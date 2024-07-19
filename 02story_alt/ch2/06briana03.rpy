label brianaevent03:
    scene 01briana03 with fade
    briana "Hey [player_name]."
    scene 02briana03
    briana "Who did this to you?"
    main "I don't know."
    scene 03briana03
    briana "And you didn't fight back?"
    main "They attacked me from behind."
    scene 04briana03
    briana "You let your guard down."
    scene 05briana03
    briana "You need training."
    scene 06briana03
    with smallshake
    main "Are you trying to give me more injuries?"
    scene 07briana03
    briana "Why did you jump back?"
    main "I didn't want another injury!"
    scene 08briana03
    briana "I'm a girl, you could at least defend yourself."
    scene 09briana03
    briana "When you're no longer in your cast, we're going to start training."
    main "Training?"
    scene 10briana03
    briana "I thought about your advice."
    if wrestlingsuggest in choices:
        scene 11briana03wrestler
        briana "Can you imagine me as a wrestler?"
        briana "I would have to wear a ridiculous outfit."
        scene 12briana03wrestler
        briana "And have some weird gimmick."
        scene 14briana03wrestler
        briana "I would also have to parade around the stage, showing off my body before a prearranged fight."
    elif bodybuildersuggest in choices:
        scene 11briana03bodybuilder
        briana "Can you imagine me as a bodybuilder?"
        scene 12briana03bodybuilder
        briana "I would have to do all of these weird poses doused in oil."
        scene 13briana03bodybuilder
        briana "Plus I would have to compete against women on steroids."
        briana "It would be a never-ending cycle of bulking and cutting."
    else:
        scene 13briana03wrestler
        briana "I don't have the stage presence for wrestling."
        scene 14briana03bodybuilder
        briana "Nor do I have patience for bodybuilding."
    scene 15briana03
    briana "I'm just not cut out for it."
    main "So what are you going to do?"
    briana "MMA."
    main "You want to go back to fighting?"
    scene 16briana03
    briana "Yeah. But this time I'm not restricted to just punching."
    scene 17briana03
    briana "I can use what ever style of fighting I want."
    scene 18briana03
    briana "And I don't have to follow as many rules as before."
    scene 19briana03
    briana "I can fight on my own terms."
    scene 20briana03
    briana "Things are going to be so different now."
    briana "I won't have dad bullying me around, complaining about my weight."
    scene 21briana03
    briana "The actual weigh-ins weren't as stressful."
    scene 22briana03
    briana "But that's all behind me now."
    scene 23briana03
    briana "Thanks, [player_name]. I'm glad you were there with me."
    scene 26briana03
    briana "I don't know what I would do without you."
    scene 25briana03
    briana "Do you think you could be my new manager? Since I kind of fired Dad."
    main "Manager?"
    $brianaevent03.status_completed("not completed")
    scene 24briana03
    briana "Yeah, the one who sets up my fights and press conferences."
    menu:
        "Agree. (Briana Trust + 3)":
            scene 27briana03
            $BrianaC.trust_up(3)
            briana "You're the best, [player_name]."
            briana "I would hug you but your cast-"
            main "It's fine."
            scene 28briana03
            briana "Well it's time for me to go."
        "Disagree.":
            scene 29briana03
            briana "..think it over, will you?"
            briana "I really need you, [player_name]."
            briana "I can help you fight off your bullies as well."
            main "Thanks, Bri but I-"
    scene 30briana03
    briana "Next time I see you, we're going training."
    briana "You won't get attacked again."
    main "Yeah sure."
    play sound "sfx/dooropenclose.ogg"
    scene 31briana03
    stop sound
    jump readtexts