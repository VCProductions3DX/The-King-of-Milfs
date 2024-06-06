label aishaevent02:
    scene 01aisha02
    main "What are you doing here?"
    aisha "Recently, the body of a young woman appeared in the River Basin."
    main "Yeah, I heard."
    scene 02aisha02
    aisha "After performing a DNA test, it came back to the young woman I was tracking."
    main "My condolences."
    if aishacooperate is in choices:
        scene 03aisha02
        aisha "I'll need an affadavit in regards to your previous statement."
        main "A what?"
        scene 04aisha02
        aisha "A written form of your statement."
        main "Why?"
        scene 05aisha02
        aisha "The autopsy performed on her determined the cause of death to be asphyxication."
        aisha "However, there were also trace amounts of heroin in her blood. More than the lethal amount."
        aisha "She died due to heroin overdose, not drowning."
        main "What does that have to do with me?"
        scene 06aisha02
        aisha "Mr. [player_name], let's not make this complicated."
        aisha "It's obvious that her boyfriend played a role in her death."
        aisha "According to what you said before, he's a drug dealer and the police did confiscate a large amount of drugs from his apartment."
        aisha "We just need a written statement linking him to the crime so we issue a warrant for his arrest."
        "(Fuck.)"
        "(I don't have a fucking choice here.)"
        jump afteraffadavit
    else:
        scene 07aisha02
        aisha "I wanted to follow up on your case here. Have they caught the perpetrator yet?"
        main "No."
        aisha "Do you still remember anything from that night?"
        aisha "Anything you don't mind telling the authorities?"
        main "I-"
        if sabrinatruth is in choices:
            scene 08aisha02
            aisha "When we notified the young woman's family over her body discovery, a relative of hers mentioned that she passed away due to a drug overdose."
            aisha "It was before the autopsy was performed."
            "(Damn it, I shouldn't have told Sabrina the truth.)"
            scene 09aisha02
            aisha "If you don't want to complicate things for yourself, I would suggest writing an affadavit."
            "(Fuck, I don't have a choice.)"
            jump afteraffadavit
        else:
            aisha "Anything at all?"
            menu:
                "Tell Aisha everything.":
                    main "Yeah."
                    scene 10aisha02
                    main "I know quite a bit."
                    aisha "I'll take it all down."
                    jump afteraffadavit
                "Say nothing.":
                    main "No, nothing."
                    jump aftersilence
label afteraffadavit:
    scene 12aisha02 with fade
    aisha "Thank you for your cooperation, Mr. [player_name]."
    main "You're welcome."
    scene 13aisha02
    aisha "Have a nice day."
    scene 14aisha02
    "(Shit. I can't believe I did that.)"
    "(I just hope he doesn't find out.)"
    if sabrinatruth is in choices:
        scene 15aisha02
        "(Who's calling me?)"
        main "Hello?"
        scene 16aisha02
        sabrina "[player_name]. It's me. Sabrina."
        main "Oh hey, Sabrina."
        scene 17aisha02
        sabrina "I'm sorry about what happened three months ago."
        sabrina "It looks like you were telling the truth."
        scene 18aisha02
        sabrina "Do you mind coming over? I need someone to talk to."
        menu:
            "Accept.":
                scene 19aisha02
                sabrina "Thanks, [player_name]."
                jump sabrinaevent03
            "Decline.":
                scene 20aisha02
                sabrina "What?"
                main "I'm sorry, Sabrina. It's over between us."
                scene 21aisha02
                sabrina "But-but [player_name]."
                main "I think it's best for us. Being together will just make the pain worse."
                scene 22aisha02
                sabrina "[player_name]!"
                main "Goodbye, Sabrina."
                jump afterdecline
    else:
        "(Should I call Sabrina and tell her the truth?)"
        "(She deserves to hear it from me.)"
        menu:
            "Call her.":
                scene 23aisha02
                sabrina "Hello?"
                main "It's me."
                scene 16aisha02
                sabrina "Oh, hey, [player_name]."
                sabrina "Sorry, I'm a little depressed right now."
                main "It's about your cousin."
                scene 24aisha02
                sabrina "Do-do you know something?"
                main "Yeah. Can I come over?"
                sabrina "Sure."
                jump sabrinaevent03
            "Don't call her.":
                "(No, it will just make things worse.)"
                "(Besides I rather not deal with her anymore.)"
                jump afterdecline
label aftersilence:
    scene 25aisha02
    aisha "Thank you, Mr. [player_name]."
    main "Yeah, sorry I can't help. "
    scene 26aisha02
    "(She's gone.)"
    "(Who's calling me?)"
    main "Hello?"
    scene 27aisha02
    sabrina "[player_name]. It's me. Sabrina."
    main "Oh hey, Sabrina."
    sabrina "Do you have time to come over to my place? I need someone to talk to."
    menu:
        "Accept.":
            scene 28aisha02
            sabrina "Thanks, [player_name]."
            jump sabrinaevent03
        "Decline.":
            scene 29aisha02
            sabrina "Huh? Why not?"
            main "It's over between us, Sabrina."
            scene 30aisha02
            sabrina "But-but-"
            main "Sorry, goodbye."
            jump afterdecline
label afterdecline:
    "(That takes care of that.)"
    "(One less thing I have to take care of.)"
    "(Now to prepare for Briana's debut.)"
    jump brianaevent05






           
