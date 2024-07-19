label reinaevent07:
    scene 01reina07 with fade
    "(She's nervous.)"
    scene 02reina07
    reina "I can do this."
    scene 03reina07
    ethan "I'm ho-"
    ethan "What are you doing here?"
    scene 04reina07
    ethan "Reina, I thought we had an agreement."
    scene 05reina07
    reina "We did. But we don't have an agreement anymore. "
    scene 06reina07
    reina "I want a divorce."
    jump ethansreaction

label ethansreaction:
    scene 07reina07
    ethan "Did you convince her to do this?"
    reina "No, Ethan. This was my decision and mine alone."
    scene 08reina07
    ethan "I never expected this from you. "
    scene 09reina07
    reina "I've given every part of me to you and all I've received is nothing but resentment."
    reina "I've tried so hard to make this relationship work. But it just isn't."
    scene 10reina07
    reina "I never expected anything from you. Except for your love."
    if reinafindsout in choices:
        scene 11reina07
        reina "AND NOW YOU'VE GIVEN IT TO SOMEONE ELSE!"
        jump reinatellsethantoleave
    else:
        scene 12reina07
        reina "And you don't love me anymore."
        jump reinatellsethantoleave
label reinatellsethantoleave:
    scene 13reina07
    reina "It's over Ethan. Leave."
    scene 14reina07
    ethan "So this is what you want. Fine."
    scene 15reina07
    ethan "Good luck with her."
    show 16reina07 with Pause(2)
    scene 17reina07
    reina "He's gone. "
    scene 18reina07
    reina "Just like that."
    scene 19reina07
    "(She grabbed a bottle of wine.)"
    if reinacare in choices:
        scene 20reina07
        "(I know what she's like when she's drunk.)"
        "(She'll come onto me again.)"
        menu:
            "Follow her.":
                "(I'll take that risk.)"
                jump mcfollowsreina
            "Stay here.":
                jump mcstaysinlivingroom
    else:
        scene 20reina07
        "(I don't know what she's like when she's drunk.)"
        "(But I don't want to leave her alone in the house.)"
        menu:
            "Follow her.":
                jump mcfollowsreina
            "Stay here.":
                jump mcstaysinlivingroom
label mcstaysinlivingroom:
    scene 71reina07 with fade
    "(I think I'll check on Mom now.)"
    $reinaevent07.status_completed("not completed")
    scene 72reina07
    "(She's completely wasted.)"
    "(I'll check on her in the morning.)"
    jump endofchapter3
label mcfollowsreina:
    scene 21reina07 with fade
    main "Mom, are you ok?"
    scene 22reina07
    reina "[player_name],  I forgot you were here. Come sit down."
    scene 23reina07
    reina "Want a sip?"
    $choices.append(reinafuck)
    main "No, I'll pass. I want to stay clean. "
    scene 24reina07
    reina "Aren't you precious. Even when offered, you refuse."
    reina "Despite everything  you've been through, you turned out to be a good, decent man."
    reina "Even if the journey was rough, you became better than your father.. "
    scene 25reina07
    reina "I'm sorry I couldn't be a good mother when you needed me the most."
    reina "But that changes now."
    scene 26reina07
    reina "I will always be there for you, no matter what."
    scene 27reina07
    reina "Let me give you a kiss."
    show 28reina07 with Pause(2)
    scene 29reina07
    reina "[player_name]."
    reina "My sweet son."
    show 30reina07 with Pause(2)
    if reinabj in choices:
        scene 31reina07
        reina "Do you need your mommy's love again?"
        reina "There's no one here to interrupt or watch us."
        scene 32reina07
        reina "You can even play with mommy's tits this time."
        scene 33reina07
        reina "Is that what you want? To play with your mommy's tits?"
    else:
        scene 31reina07
        reina "[player_name], you're a frisky one tonight."
        scene 32reina07
        "(She's taking off her shirt.)"
        scene 33reina07
        reina "You like mommy's big, soft tits, don't you? "
        reina "Don't by shy, feel them."
    scene 34reina07
    reina "They feel nice and squishy, don't they?"
    reina "You can kiss them."
    "(This is a dream come true.)"
    scene 35reina07
    reina "Go on, lick mommy's tits."
    reina "That's a good boy."
    scene 36reina07
    reina "Suck those nipples hard."
    scene 37reina07
    reina "Your tongue feels so good."
    scene 38reina07
    reina "I want you to please me, [player_name]."
    scene 39reina07 
    reina "Show me how to please  your mommy."
    scene 40reina07
    reina "Mommy wants to know what a man her baby boy has become."
    menu:
        "Finger-fuck her to an orgasm.":
            scene 41reina07
            reina "How does mommy's pussy feel?"
            reina "Is it as warm and wet as you remember?"
            scene 42reina07
            reina "Go a little faster, baby."
            scene 43reina07
            reina "Mmmmm."
            scene 44reina07
            "(She's a squirter.)"
            menu:
                "(I have to taste her.)":
                    jump eatingreinaout
                "(I want her to suck my cock.)":
                    jump reinablowjob
        "Eat her out.":
            label eatingreinaout:
                scene 45reina07
                reina "Do you like the taste of mommy's pussy?"
                scene 46reina07
                reina "Do you?"
                scene 47reina07
                reina "Don't stop, please stop."
                scene 48reina07
                reina "Yes! Your tongue feels so good on your mommy's pussy!"
                reina "You're such a good little boy. Making your mom cum with your mouth."
                jump reinablowjob
    label reinablowjob:
        scene 49reina07
        if reinabj in choices:
            reina "There's my baby boy's cock."
            reina "And it's so big and hard."
            reina "Mommy can't wait to taste it again."
        else:
            reina "Look at my baby boy's cock."
            reina "It's so big and hard."
            reina "Mommy is going to take care of it."
        scene reinablowjob05 with Pause(7) 
        scene 51reina07
        reina "So rough."
        scene 52reina07
        reina "You're naughtier than I thought."
        scene 53reina07
        reina "Fuck me, [player_name]."
        scene 54reina07
        reina "I want to feel my baby boy inside of me."
        jump reinafirstfuck
    label reinafirstfuck:
        scene reinafuck01
        reina "Oh, [player_name] you feel so good inside of me."
        show text "I'm such a bad woman." at thoughtsright with Pause(5)
        show text "I'm fucking my own son." at thoughtsright with Pause(10)
        show text "And he feels so fucking good."at thoughtsright with Pause(10)
        scene reinafuck02
        reina "Fuck me faster, [player_name]."
        reina "Don't hold back against your mother."
        scene reinafuck03
        reina "Yes, that's it! Don't stop, don't stop!"
        main "I'm going to cum!"
        main "Fuck, I'm cumming!"
        reina "Cum inside of me, [player_name]!"
        reina "Cum inside your mommy!"
        scene 67reina07
        reina "Oh, that feels so good."
        jump mcfirstcreampie
    label mcfirstcreampie:
        scene 68reina07
        reina "Thank you, [player_name]."
        reina "You've given your mother what she's wanted for a long,long time."
        $reinaevent07.status_completed("not completed")
        "(I can't believe I fucked her.)"
        "(My own fucking mother.)"
        scene 69reina07
        "(I even came inside of her.)"
        scene 70reina07
        "(I hope she doesn't regret it.)"
        jump middleofthenightfuck
    label middleofthenightfuck:
        scene 75reina07
        "(Shit,I'm horny again.)"
        scene 76reina07
        "(And Mom's lying there asleep.)"
        menu:
            "(Fuck her again.)":
                scene 77reina07
                "(She's mine now.)"
                scene reinanipples
                "(Her tits are so soft and warm.)"
                "(Fuck, she's waking up.)"
                scene reinapussy01
                "(Her legs are spread. I'll just finger her.)"
                scene reinapussy02
                reina "Mmm, that tickles. "
                scene reinapussy03
                reina "Fuck, that feels so good, baby."
                reina "Don't stop."
                scene reinapussy04
                reina "Yes. Please don't stop."
                reina "Faster. Please. Please"
                scene reinapussy05
                reina "Oh yes, that's it."
                reina "Fuck me. Fuck my pussy."
                reina "Fuck me."
                "(With pleasure.)"
                scene reinafuck05
                "(Mom's pussy feels good.)"
                reina "Mmmm, such a big, hard cock."
                reina "Fuck me. Faster. Deeper."
                scene reinafuck04
                reina "Don't stop, you feel so good!"
                reina "Fuck!"
                scene reinafuck06
                reina "That's it."
                reina "Cum inside of me."
                reina "Kiss me goodnight,baby."
                scene reinakiss
                "(I hope she doesn't think I'm Dad.)"
                scene black with fade
                jump endofchapter3
            "(Wait until the morning.)":
                "(No, I'll just rub it out.)"
                scene black with fade
                jump endofchapter3
label endofchapter3:
    show text "End of Chapter 3" with Pause (5)
    "Would you like to save your progress?"
    menu:
        "Yes":
            call screen save
            jump reinaevent08
        "No":
            jump reinaevent08