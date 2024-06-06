label brianaending:
    scene brianaending01
    "(Briana and I are supposed to go on a hike today.)"
    "(I'll check up on her.)"
    briana "Hey [player_name]."
    briana "You're finally awake."
    main "Sorry, I overslept."
    briana "I'm ready to go when you are."
    main "I'm ready. Are you going to dress to like that?"
    briana "No. Shoo. Out."
    scene brianawalk
    briana "The air is so nice, clean and crisp."
    briana "Just look at this view."
    briana "And these waterfalls."
    briana "We finally made it to camp."
    briana "I'll grab some wood then I'll help you set up."
    if brianapregnancy in choices:
        main "So, what are you going to do?"
        briana "Take a break, of course."
        briana "I don't want to go in labor during a fight."
        briana "I should probably tell Mom."
        main "We'll tell Reina, together."
        briana "Do you think she'll approve of us?"
        main "She won't have a choice."
    else:
        main "So, what happens next?"
        briana "I'm going to take a break."
        briana "I went into MMA too eagerly."
        briana "I just wanted to get away from Dad and I did."
        briana "After I clear my mind, I'll come back."
        briana "With you by my side."
    
    "(It's quiet and peaceful.)"
    "(The cravings are gone.)"
    "(There's just Briana.)"
    scene black with fade
    show text ("Queen of Hearts: End") with Pause(5)
    jump endingscreen