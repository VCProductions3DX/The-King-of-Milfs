label sabrinaevent03:
    scene 01sabrina03
    sabrina "Hey [player_name]."
    if sabrinatruth is in choices:
        scene 02sabrina03
        sabrina "I'm sorry about before."
        sabrina "I..was in shock."
        scene 03sabrina03
        sabrina "She's really gone. She's dead."
        main "Sabrina, I'm sorry. I really tried."
        scene 04sabrina03
        sabrina "I-"
        "(I feel like shit. If only I had reached her sooner.)"
        scene 05sabrina03
        sabrina "Thank you, [player_name.]"
        sabrina "We're going to hold a memorial service for her."
        main "Where will it be?"
        scene 06sabrina03
        sabrina "It'll be here. Jane always...wanted to leave Sierra City."
        sabrina "So here is nice."
        "(Hopefully he won't show up.)"
        scene 07sabrina03
        sabrina "[player_name], do you mind staying here for a while?"
        main "Sure."
        jump mcandsabrinamakeup
    else:
        jump mcandsabrinadiscusscase
label mcandsabrinadiscusscase:
    main "What's up?"
    scene 08sabrina03
    sabrina "They found Jane's body."
    main "Is that the one they found in the river?"
    sabrina "Yeah."
    scene 09sabrina03
    sabrina "She's dead."
    sabrina "She's really dead."
    sabrina "How did it happen?"
    "(Shit.)"
    "(Should I tell her?)"
    "(She might get angry.)"
    menu:
        "(Tell her the truth.)":
            main "Sabrina. Jane..died due to an overdose."
            scene 10sabrina03
            sabrina "How...how do you know that?"
            main "I..I saw her body on the couch. I thought she was asleep but-"
            scene 11sabrina03
            sabrina "You saw her and you didn't do anything!!"
            sabrina "How could you?!?!"
            main "Sabrina-"
            scene 12sabrina03
            sabrina "She was my best friend!!!!!"
            menu:
                "(Try to calm her down.)":
                    main "Sabrina, calm down."
                    scene 13sabrina03
                    sabrina "How can I calm when my best friend is dead and my ex- he didn't do anything!"
                    scene 14sabrina03
                    sabrina "You are the worst!"
                    sabrina "Get out!"
                    main "Ok, sorry. I'll leave."
                    scene 15sabrina03
                    "(Shit, she's angry.)"
                    "(She'll probably run to the police.)"
                    jump mcleavessabrinasplace
                "(Apologize.)":
                    main "I'm sorry, Sabrina."
                    main "I was scared, I didn't know what to do."
                    main "If there was a way I could've saved her, I would."
                    scene 16sabrina03
                    "(She's still crying.)"
                    menu:
                        "(Leave her be.)":
                            jump mcleavessabrinasplace
                        "(Hug her.)":
                            jump mcandsabrinamakeup
        "(Keep quiet.)":
            scene 19sabrina03
            sabrina "Thanks for being here for me, [player_name]."
            sabrina "Do you mind staying here for a while?"
            main "Sure."
            jump mcandsabrinamakeup

label mcandsabrinamakeup:
    scene 20sabrina03
    main "How are you feeling?"
    scene 21sabrina03
    sabrina "Better."
    sabrina "You're the best, [player_name]."
    scene 22sabrina03
    "(Fuck, she's warm.)"
    scene 23sabrina03
    scene 24sabrina03
    sabrina "What's the matter?"
    menu:
        "(Keep going.)":
            main "Nothing."
            jump mcandsabrinasex2
        "(Stop.)":
            main "This doesn't feel right."
            scene 25sabrina03
            sabrina "Huh?"
            scene 26sabrina03
            sabrina "It is pretty awkward."
            sabrina "Let's go on a date after the burial."
            sabrina "Promise?"
            scene 27sabrina03
            main "Promise."
            jump mcleavessabrinasplace
label mcandsabrinasex2:
    "(Fuck, I miss her.)"
    "(Her small tits, firm ass.)"
    "(And tight pussy.)"
    sabrina "Fuck me, Daddy."
    "(There she goes with the Daddy stuff again.)"
    "(I feel like it's important but..ugh forget it.)"
    sabrina "Fuck me, fuck your little girl!"
    "(Fuck, I can't hold it any longer.)"
    sabrina "So naughty."
    sabrina "You might become a Daddy someday."
    $choices.append(sabrinapregnancy)
    "(Damn, I didn't think of that.)"
    sabrina "Are you spending the night here?"
    main "I have things to do."
    sabrina "Aww."
    sabrina "I'll see you soon, right?"
    main "Right."
    sabrina "Good night, [player_name]."
    jump mcleavessabrinasplace
label mcleavessabrinasplace:
    scene 41sabrina03
    "(Well, that's over.)"
    jump brianaevent05

