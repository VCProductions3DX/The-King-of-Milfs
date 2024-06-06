label brianaevent07:
    scene 01briana07
    main "Nervous?"
    briana "Yeah."
    scene 02briana07
    briana "Last time it was an exhibition, but this one is an actual match."
    briana "I'm so jittery. "
    main "We can cancel the match if you want."
    scene 03briana07
    briana "Are you stupid? I did that whole press conference and you want me to cancel?"
    briana "No. I have to do it."
    scene 10briana07
    "(There are a lot less people here.)"
    scene 11briana07
    "(Is this safe?)"
    scene 12briana07
    "(Is Briana ok?)"
    scene 13briana07
    "(This doesn't look good.)"
    scene 14briana07
    "(At all.)"
    scene 15briana07
    "(She has Briana in a headlock.)"
    scene 16briana07
    "(Is no one intervening?)"
    scene 17briana07
    "(She's walking away.)"
    scene 18briana07
    main "Briana? Are you ok?"
    "(She's knocked out cold.)"
    scene 19briana07
    main "We need some help over here!"
    scene 20briana07
    "(More people showed up.)"
    "(I'll just have to wait.)"
    jump afterthematch
label afterthematch:
    scene 21briana07
    briana "Where..am I?"
    main "In a bed. You collapsed during the fight."
    scene 22briana07
    briana "Figures. My first real match and I pass out."
    briana "I'm not looking forward to the interviews and jokes..."
    main "I'll take care of it."
    if brianapregnancy is in choices:
        scene 23briana07
        briana "Ugh."
        main "Is something wrong?"
        scene 24briana07
        briana "Dizzy for a moment. Felt like I was going to throw up."
        main "I'll get a trashcan for you."
        briana "Thanks."

    else:
        scene 25briana07
        briana "I'm dehydrated."
    scene 26briana07 with fade
    briana "I'm getting old."
    main "Briana, you're only 23."
    scene 27briana07
    briana "Old. And Fat."
    briana "I can't help if I'm a late bloomer."
    scene 28briana07
    briana "I didn't ask to grow big tits, it just happened!"
    scene 29briana07
    briana "If I want to compete seriously I...I might need to get a reduction."
    briana "Or go on steroids."
    menu:
        "(Discourage her.)":
            main "No."
            scene 30briana07
            briana "I barely made weigh-in. If I didn't dehydrate, I would have gone over and be disqualified."
            briana "It sucks but-"
            main "Steroids can ruin you if you do too much."
            scene 31briana07
            briana "So a reduction, then?"
            briana "I can always get implants later."
            main "Maybe this isn't right for you."
            scene 32briana07
            briana "But I like fighting. I want to fight."
            briana "I just can't keep doing exhibitions forever."
            briana "I have a reputation to uphold."
            main "You're more than the Knockout Queen. You're...Briana."
            scene 33briana07
            briana "Yeah. Thanks, [player_name]."
            briana "I'll think about it."
            jump freeroamch5
        "If that's what you want.":
            scene 34briana07
            briana "I ...I just want to fight."
            briana "Stupid weight classes."
            scene 35briana07
            briana "Maybe...I'm finished."
            briana "Maybe I should do something else."
            main "I'll always support you, Briana."
            scene 36briana07
            briana "Oh you."
            briana "This is it, then. The end of the Knockout Queen."
            briana "Knocked out by her own body."
            jump freeroamch5
            




    


    