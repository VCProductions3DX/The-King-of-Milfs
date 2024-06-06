label reinaevent06:
    scene 01reina06 with fade
    "(She's here.)"
    scene 03reina06
    reina "[player_name]."
    scene 02reina06
    main "Sorry I'm late, Reina."
    play sound "sfx/dooropenclose.ogg"
    scene 04reina06
    "Reina Lopez?"
    stop sound
    reina "Yes, that's me. "
    maxine "I'm Maxine, nice to finally meet you. Please come inside."
    scene 05reina06
    reina "May he come in with me?"
    maxine "Yes, he may."
    scene 06reina06 with fade
    maxine "Please sit down."
    scene 07reina06
    maxine "You're here to discuss about a legal separation from your spouse. Is that correct?"
    reina "Yes."
    scene 08reina06
    maxine " I understand that this is a difficult decision to make. How long have you been married to your husband?"
    scene 09reina06
    reina "20 years. Since I was ..24. "
    maxine "How many children do you have together? Are there any under 18?"
    reina "I have 2 daughters over the age of 18."
    scene 10reina06
    maxine "Thank you. We can skip the everything regarding custody. Let's start on your financial assets. "
    scene 15reina06
    reina "Before we start- may I ask about divorce?"
    scene 14reina06
    maxine "Divorce is a big leap from legal separation. It will require a court hearing. Your spouse will need to hire a lawyer if he desires to contest the divorce."
    maxine "Separation is for couples who feel their marriage might be repaired some day. Do you feel that is the case?"
    scene 16reina06
    if reinaevent07.status == "completed":
        reina "I'm not sure."
        reina "I'll go with a divorce."
        jump reinapicksdivorce
    else:
        menu:
            "I think the marriage is beyond repair.":
                scene 13reina06
                reina "Yes. You're right."
                reina "He no longer loves me."
                scene 14reina06
                maxine "Take your time over this decision, Reina."
                menu:
                    "Ask for a divorce." if divorcesuggest in choices: 
                        scene 12reina06
                        reina "Yes, I think I'll go with a divorce."
                        jump reinapicksdivorce
                    "Let Reina decide.":
                        scene 12reina06
                        reina "I think.."
                        if ReinaC.c_love >= 3:
                            reina "I'll go with a divorce."
                            jump reinapicksdivorce
                        else:
                            reina "I'll go with a separation."
                            jump reinapicksseparation
            "Think about how miserable he makes everyone.":
                reina "That is true."
                maxine "Have you made up your mind?"
                reina "I think so."
                reina "I'll go with a divorce."
                reina "For my daughters."
                jump reinapicksdivorce
            "He has a mistress.(Reina Trust + 3)" if  miyukiethanphoto in choices:
                stop music
                scene 19reina06
                reina "What?"
                $choices.append(reinafindsout)
                maxine "A third party-"
                reina "I want to know more."
                scene 17reina06
                main "Her name is Miyuki. I overheard a conversation between the two of them."
                scene 21reina06
                reina "I want a divorce."
                scene 18reina06
                maxine "Reina, without proof it would be difficult to win everything in a contested divorce."
                scene 20reina06
                maxine "Do you have any physical evidence of this affair?"
                main "Here."
                reina "Oh my god."
                reina "I remember that trip. I wanted to go but he told me no."
                reina "He took her instead."
                maxine "Reina-"
                scene 15reina06
                reina "I've made up my mind."
                jump reinapicksdivorce
    label reinapicksdivorce:
        reina "I want a divorce."
        $choices.append(reinadivorcepick)
        scene 22reina06
        reina "Here is a folder with all of my financial assets."
        scene 23reina06
        reina "I want to keep everything I own, and the house we bought.It is the only asset we share."
        scene 24reina06
        maxine "I will make a note of that."
        jump maxineprintsdocuments
    label reinapicksseparation:
        scene 22reina06
        $choices.append(reinaseparationpick)
        reina "I want a legal separation."
        scene 24reina06
        maxine "Are these your financial assets?"
        reina "Yes, mine and mine alone."
        jump maxineprintsdocuments
    label maxineprintsdocuments:
        scene 25reina06
        maxine "Please make yourselves comfortable while I go prepare the documents."
        if reinafindsout in choices:
            scene 26reina06 with fade
            reina "[player_name]."
            scene 27reina06
            reina "How long have you known this?"
            reina "This affair?"
            main "Since the Town Hall meeting."
            scene 28reina06
            reina "The Town Hall meeting."
            scene 29reina06
            reina "Everything makes sense now."
            reina "She has him wrapped her finger."
            jump maxinereturns
        else:
            scene 26reina06 with fade
            main "Reina."
            main "What are you thinking?"
            scene 27reina06
            reina "If I made the right choice."
            scene 28reina06
            reina "This isn't something I can rewind if it goes wrong."
            scene 29reina06
            reina "But..I think I made the right decision. For everyone."
            jump maxinereturns
    label maxinereturns:
        scene 30reina06
        maxine "Here are the documents. Who will be serving them? "
        scene 31reina06
        reina "I will."
        maxine "Once the documents have been served, let me know. Then there will be 90 days for him to respond."
        scene 32reina06
        reina "And if he doesn't?"
        if reinadivorcepick in choices:
            maxine "Then the judge will order a default settlement and the divorce will be finalized. "
        else:
            maxine "We will have to go to mediation."
        maxine "I will call you if and when I receive a response."
        scene 34reina06
        reina "Thank you, Maxine."
        maxine "You're welcome, Reina. Call me if you have any more questions or concerns."
        scene 33reina06
        reina "I will."
        maxine "Have a nice day."
        scene 35reina06 with fade
        reina "I'm really doing this."
        $reinaevent07.status_completed("not completed")
        main "Are you scared of him?"
        scene 36reina06
        reina "A little."
        scene 38reina06
        reina "I still feel like the young, naive girl that I was when I married him. "
        main "You're not her anymore."
        scene 37reina06
        reina "It's because I have you. "
        scene 39reina06
        reina "Thank you so much for being there for me, [player_name]."
        scene 40reina06
        reina "I will give him this tonight when he comes home."
        reina "I want you there with me when it happens."
        jump reinaevent07