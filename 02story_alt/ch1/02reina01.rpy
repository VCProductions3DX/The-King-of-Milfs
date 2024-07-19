
label reinaevent01:
    scene 01reina01 with fade
    reina "Hello, [player_name]."
    reina "You look so much better now."
    scene 02reina01
    main "Where are we going?"
    reina "To your new home. For now."
    reina "I wanted you to move into our new home, but your aunt Jenni is currently staying with us."
    reina "She's staying in your room for the time being, so you're house-sitting a cottage I just bought."
    reina "I hope that's alright with you."
    menu:
        "House-sitting?":
            reina "I need someone to live there while I fix it up and resell it."
            reina "Town ordinances and all."
        "Why did you buy a cottage?":
            reina "It was a steal of the lifetime. It's close to the oceanfront, small, and quaint. The perfect getaway."
            reina " The owner was behind on taxes, so I paid off the tax lien and now it's mine. Its land value is over 1 million dollars. "
    scene 04reina01
    reina "To be honest, this is my first time here since I bought it."
    scene 05reina01
    reina "I don't think the owners really lived here either; they just kept the property until they couldn't. "
    reina "Let's go."
    play sound "sfx/dooropenclose.ogg"
    scene 06reina01
    reina "Home sweet home."
    stop sound
    scene 07reina01 with fade
    reina "It's not nearly as dirty nor dusty as I thought."
    scene 08reina01
    reina "Seems like the owners were making some renovations to the kitchen."
    scene 09reina01
    reina "Hmm..they left some wine here."
    scene 10reina01
    reina "It's Marlot."
    menu:
        "I didn't know you liked wine.(+1 Mom Love)":
            scene 11reina01
            $ReinaC.love_up(1)
            reina "Your mother has become a bit of a wino."
            reina "A few years ago, I was invited to a wine tour in Napa Valley."
            reina "I really learned to appreciate the subtle flavor of wine."
            reina "I just don't care for Marlot."
            scene 12reina01
            reina "I'm taking this with me. Just to be safe."
            main "But Mom-"
            scene 13reina01
            reina "No. You're not allowed anything, ok? No drugs, no alcohol. Nothing. "
            reina "Those were your dad's terms."
            reina "Thankfully, there's only one bottle in here."

        "What do you like,Mom?(+1 Mom Trust)":
            scene 10reina01
            $ReinaC.trust_up(1)
            reina "I prefer white wines- Chardonnay, Pinot Grigio, Riesling."
            reina "And Moscato, of course. "
            reina "Still, Marlot isn't too bad either."
            reina "It would be bad if this bottle of wine stayed here."
            scene 12reina01
            reina "I'll be taking it with me."
            reina "I can't have you relapsing because of me."
            main "Mom, I have never had a problem with alcohol, I'm fine."
            scene 13reina01
            reina "Do you understand the situation that you're in, [player_name]?"
            reina "Your father wanted you to rot on the street. But I begged him to give you another chance."
            reina "This is your second chance. Your last chance to get it together. If you relapse, that's it. I can't help you anymore."
            scene 14reina01
            reina "I'm taking this with me."

    scene 15reina01
    reina "I wonder what else is here."
    scene 16reina01
    reina "Mostly empty, I see. But that's not a problem. There's a grocery store a few blocks from here."
    reina "Let's see if there's running water."
    scene 17reina01
    reina "There is!"
    reina "The kitchen is in good condition so far."
    scene 18reina01
    reina "This area is completely empty. I was thinking of maybe a dining room or a small den."
    scene 19reina01
    reina "Let's go to the bedroom."
    scene 22reina01
    reina "Wow..this is quite pleasant. A nice rustic and romantic feel to it."
    reina "I don't see any cabinets ..but there is a nightstand."
    scene 20reina01
    play sound "sfx/WaterWaves1.ogg"
    reina "Oh! This bed is soft. I could use a nap right now."
    main "Mom..."
    reina "Shhh...you can hear the ocean from here. It's perfect."
    stop sound
    scene 21reina01
    reina "Ok, naptime over. Now for the bathroom."
    scene 23reina01
    reina "Looks like they renovated the bathroom as well."
    scene 24reina01
    reina "Lucky you, there's a shower and a sauna."
    scene 25reina01
    reina "I just need to make sure that the water is running here as well. "
    scene 26reina01
    reina "Basic inspection completed. I'll need to hire an actual inspector to check everything else."
    scene 27reina01
    reina "Now where is it..."
    reina "Ah, here it is!"
    scene 28reina01
    reina "Here, it has 2000 on it. It should be more than enough to get food, clothes, whatever you need. "
    menu:
        "Will I have to pay rent?":
            reina "No, no, honey. I would never force you to pay rent. "
            reina "But you shouldn't be freeloading here either. Take as long as you need to get back to normal."
            reina "I think getting a job would help you get back on your feet. I'll call a few friends and see if they need any help."
            reina "Then you can help clean this place up and buy furniture before I sell it."
            scene 29reina01
            reina "I'm just glad you're back home."
        "Thanks, Mom.(+1 Mom Love)":
            reina " You're welcome, sweety. I'm just so glad that you're back home. "
            $ReinaC.love_up(1)
            scene 29reina01
            reina "I've missed you so much. And ..I'm sorry.  "
            scene 30reina01
            reina "I'm sorry I didn't call or text you all those years you were gone."
            scene 31reina01
            reina "I promise I'll be a better mother. "
    $reinaevent01.status_completed("not completed")
    scene 32reina01
    reina "Well, I have a few things to finish up at my office, but I will swing by tomorrow. "
    reina "Get some rest, [player_name]. You deserve it."
    scene 33reina01
    "(I'm finally alone.)"
    "(Fuck, I have a headache. I could really use something right now- a cigarette would be nice.)"
    play sound "sfx/cellvibe.ogg"
    "(Who's texting me?)"
    scene 34reina01
    "(PinkPrincess?)"
    stop sound
    scene 35reina01
    "Hey, [player_name], are you there? We haven't talked in six months!"
    "Are you ok? I miss you. Sabrina."
    scene 36reina01
    "(Sabrina. We broke up before all of this shit happened.)"
    "(She looks completely different now with pink hair.)"
    menu:
        "(She looks fucking hot.)":
            scene sabrinaglow
            "(Her soft skin, her tiny nipples.)"
            "(She was the perfect girlfriend.)"
            "(I can imagine fucking her now.)"
            "(I need to see her again.)"
            jump afterfap
        "(I'm not attracted to her anymore.)":
            "(Our relationship is over.)"
            "(She was too clingy.)"
            "(But Mom on the other hand.)"
            scene reinaglow 
            "(She looks hot now that she's lost weight.)"
            "(Her big tits and fat ass look amazing on her.)"
            "(I bet she gets hit on everyday.)"
            "(I wouldn't mind fucking her if I got the chance.)"
            jump afterfap
    label afterfap:
        scene 37reina01 with fadewhite
        "(Damn that felt good.)"
        "(I haven't fapped in months.)"
        "(It took the edge off and the craving's gone.)"
        scene 38reina01
        "(Is someone looking at me?)"
        scene 39reina01
        "(Shit!)"
        jump camillaevent01





