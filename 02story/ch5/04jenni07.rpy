label jennievent07:
    scene 01jenni07 with fade
    jenni "Hello [player_name]."
    main "Are you moving again?"
    scene 02jenni07
    jenni "Yes. This town is way too small for my liking."
    main "Where are you going?"
    scene 03jenni07
    jenni "Not sure yet. Not LA. Maybe somewhere overseas."
    jenni "Spain sounds nice."
    main "But what about Reina?"
    scene 04jenni07
    jenni "She doesn't need me anymore."
    jenni "She has her life and identity. I'm proud of her."
    scene 05jenni07
    jenni "The girls as well. They're not shadows of a man, but actual people."
    jenni "Not much more I can ask for."
    main "But-"
    if JenniC.c_love >=5:
        scene 07jenni07
        jenni "But there's you."
        jenni "You have become quite a stud."
        main "Thanks, Jenni."
        if jennipregnancy in choices:
            scene 06jenni07
            jenni "So much so that I'm pregnant."
            main "What?"
            jenni "You heard me. I'm pregnant."
            main "I-"
            scene 10jenni07
            jenni "After all this time, I thought I was the one with fertility problems."
            jenni "But no, it was them."
            scene 09jenni07
            jenni "I just needed a younger, fit man to prove them wrong."
            jenni "From the look on your face, you're shocked as well."
            main "Jenni, I'm sorry, I-"
            scene 08jenni07
            jenni "Well, I'm going to give you a choice, [player_name]."
            jenni "You can come with me and be a father."
            jenni "Or never see me or our child ever again."
            main "Ever?"
            scene 14jenni07
            jenni "I mean it. I don't want my child to have a half-ass father."
            jenni "I'll just give it up for adoption."
            scene 15jenni07
            jenni "The choice is yours."
            menu:
                "Go with Jenni.":
                    scene 16jenni07
                    $commitments +=1
                    jenni "Are you sure about this?"
                    $choices.append(jennimove)
                    $JenniC.love_up(10)
                    main "I'm sure."
                    scene 17jenni07
                    jenni "Because it would be pretty horrible if I find out you're abandoning another girl for me."
                    main "I'm positive."
                    scene 18jenni07
                    jenni "We leave next week."
                    jenni "That's more than enough time to say goodbye to everyone, isn't it?"
                    main "Yeah."
                    jump freeroamch5
                "Stay here.":
                    scene 19jenni07
                    jenni "It's someone else, isn't it?"
                    main "No, I just-"
                    scene 20jenni07
                    jenni "You're still young. But you won't be forever."
                    jenni "Just remember that."
                    jenni "It was nice knowing you, [player_name]."
                    main "Thanks Jenni, for everything."
                    scene 19jenni07
                    jenni "Thank you, [player_name]."
                    jenni "Goodbye."
                    jump freeroamch5
        else:
            scene 07jenni07
            jenni "I think I've gotten a little too attached to you."
            jenni "You're like a personal sex toy to me."
            main "Is that what you think of me?"
            scene 10jenni07
            jenni "It's a good thing I'm not pregnant."
            jenni "That would make this situation worse."
            scene 11jenni07
            jenni "I do want to have a little more fun before I leave though."
            jenni "Do you?"
            menu:
                "Sure.":
                    scene 12jenni07
                    jenni "Follow me."
                    jump jennithirdfuck
                "No thanks.":
                    jenni "Thank you, [player_name]."
                    jenni "Goodbye."
                    jump freeroamch5
    else:
        scene 08jenni07
        jenni "Is something wrong?"
        main "No, nothing's wrong."
        scene 09jenni07
        jenni "Will you miss me?"
        main "A little bit."
        scene 11jenni07
        jenni "Want to make another memory before I leave?"
        menu:
            "Sure.":
                scene 12jenni07
                jenni "Follow me."
                jump jennithirdfuck
            "No thanks.":
                jenni "Thank you, [player_name]."
                jenni "Goodbye."
                jump freeroamch5

label jennithirdfuck:
    scene 25jenni07 with fade
    main "You're ready to go."
    scene 26jenni07
    jenni "Fuck me before I change my mind."
    scene jennifuck05
    jenni "Yes, that's it. Fuck me, baby."
    jenni "Fuck my pussy with your big cock."
    scene jennifuck04
    jenni "Fuck! You feel so good. Don't stop, baby."
    jenni "Fill my pussy with your cum."
    jenni "I want to feel you cum inside of me."
    scene jennifuck03
    jenni "Yes, that's it. Don't pull out."
    jenni "Pour it all inside of me."
    jenni "Impregnate me."
    scene 33jenni07
    jenni "Fuck. That felt good."
    jenni "We should stay in contact."
    jenni "You have my number, right?"
    main "I do."
    scene 27jenni07
    jenni "Don't ignore my phone calls."
    jenni "Goodbye for now."
    jump freeroamch5