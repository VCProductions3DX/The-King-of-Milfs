label sabrinaevent03:
    scene 01sabrina03 with fade
    sabrina "Hey [player_name]."
    if sabrinatruth in choices:
        scene 02sabrina03
        sabrina "I'm sorry about before."
        sabrina "I..was in shock."
        scene 03sabrina03
        sabrina "She's really gone. She's dead."
        main "Sabrina, I'm sorry. I really tried."
        "(I feel like shit. If only I had reached her sooner.)"
        scene 05sabrina03
        sabrina "Thank you, [player_name]."
        sabrina "We're going to hold a memorial service for her."
        main "Where will it be?"
        scene 06sabrina03
        sabrina "It'll be here. Jane always wanted to leave Sierra City."
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
                    scene 03sabrina03
                    "(She's still crying.)"
                    menu:
                        "(Leave her be.)":
                            jump mcleavessabrinasplace
                        "(Hug her.)":
                            scene 05sabrina03
                            jump mcandsabrinamakeup 
        "(Keep quiet.)":
            scene 19sabrina03
            sabrina "Thanks for being here for me, [player_name]."
            sabrina "Do you mind staying here for a while?"
            main "Sure."
            jump mcandsabrinamakeup

label mcandsabrinamakeup:
    scene 20sabrina03 with fade
    sabrina "[player_name]."
    main "How are you feeling?"
    scene 21sabrina03
    sabrina "Better."
    sabrina "You're the best, [player_name]."
    scene 23sabrina03 with Pause(2)
    scene 22sabrina03
    sabrina "What's the matter?"
    menu:
        "(Keep going.)":
            main "Nothing."
            jump mcandsabrinasex2
        "(Stop.)":
            main "This doesn't feel right."
            scene 40sabrina03
            sabrina "Huh?"
            main "I don't want to take advantage of you while you're mourning."
            if SabrinaC.c_love>=5:
                sabrina "I want this, silly."
                jump mcandsabrinasex2
            else:
                scene 41sabrina03
                sabrina "Thanks for looking out for me, [player_name]."
                sabrina "Can we go on a date when all of this is over?"
                main "Sure."
                scene 42sabrina03
                sabrina "Is there somewhere you need to be?"
                main "Yeah, actually. I'm helping my family out."
                sabrina "Ok. I'll see you at the funeral."
                scene 43sabrina03
                sabrina "Goodbye."
                jump mcleavessabrinasplace

label mcandsabrinasex2:
    if sabrinaroleplay in choices:
        scene 24sabrina03
        sabrina "Does Daddy miss his little girl?"
        sabrina "I miss Daddy so much."
        scene 25sabrina03
        sabrina "I'm ready for you, Daddy."
        scene 26sabrina03
        sabrina "Daddy's big fingers feel so inside of me."
        scene 27sabrina03
        sabrina "Daddy, maybe I cum, please? Please?"
        sabrina "Daddy, I'm so wet."
        scene 29sabrina03
        sabrina "Daddy, fuck me please."
        sabrina "I want to feel Daddy's cock inside of me."
        scene sabrinafuck03
        sabrina "Fuck me Daddy. Fuck me with your big hard cock, Daddy."
        sabrina "Daddy's cock feels so good inside of my pussy."
        sabrina "Don't stop Daddy."
        sabrina "Fuck Daddy!"
        scene 30sabrina03
        "(Damn, that was a lot.)"
        $choices.append(sabrinapregnancy)
        scene 34sabrina03
        sabrina "I needed that. Thank you, Daddy."
        main "You're welcome, princess."
        scene 35sabrina03
        sabrina "Can we fuck again?"
        main "Unfortunately Daddy has business."
        scene 36sabrina03
        sabrina "Awww."
        sabrina "But soon, right?"
        main "Of course."
        scene 38sabrina03
        sabrina "Good night, Daddy."
        main "Good night, princess."
        
        jump mcleavessabrinasplace
    else:
        scene 24sabrina03
        "(Fuck, I miss her.)"
        scene 25sabrina03
        "(Her small tits, firm ass.)"
        scene 27sabrina03
        "(And tight pussy.)"
        scene 26sabrina03
        sabrina "Fuck me, Daddy."
        scene 28sabrina03
        "(There she goes with the Daddy stuff again.)"
        "(I feel like it's important but..ugh forget it.)"
        scene sabrinafuck03
        sabrina "Fuck me, fuck your little girl!"
        "(Fuck, I can't hold it any longer.)"
        scene 30sabrina03
        sabrina "So naughty."
        sabrina "You might become a Daddy someday."
        $choices.append(sabrinapregnancy)
        "(Damn, I didn't think of that.)"
        scene 34sabrina03
        sabrina "Are you spending the night here?"
        main "I have things to do."
        scene 35sabrina03
        sabrina "Aww."
        sabrina "I'll see you soon, right?"
        main "Right."
        scene 36sabrina03
        sabrina "Good night, [player_name]."
        jump mcleavessabrinasplace
label mcleavessabrinasplace:
    scene 45sabrina03 with fade
    $sabrinaevent03.status_completed("not completed")
    "(Well, that's over.)"
    jump brianaevent05