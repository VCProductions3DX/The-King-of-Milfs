label kingending:
    scene 01kingending with fade
    "(Looking good.)"
    "(Better than I did a year ago.)"
    scene 02kingending
    "(Briana went back to boxing.)"
    "(She preferred the rigid rules.)"
    "(She also got a breast reduction so she can make weigh-ins.)"
    scene 04kingending
    "(Penny decided to take a break from her music and go back to extreme sports.)"
    "(She's taken up surfing at the moment.)"
    scene 05kingending
    "(Aunt Jenni is vacationing in Spain. She sends a lot of photos.)"
    scene 06kingending
    "(Sabrina closed her parents' shop and decided to stream full time.)"
    "(She's extremely popular, although for all the wrong reasons.)"
    if camillarunforoffice in choices:
        scene 03kingending
        "(Camilla and Miyuki are running for office.)"
        "(The campaign is pretty close, with Miyuki in the lead.)"
        "(Of course, being close to both of them has its advantages.)"
        jump ddoutcome
    else:
        scene 08kingending
        "(Without any competition, Miyuki became Mayor of Sierra Beach.)"
        "(Within a short amount of time, the first part of her project was completed.)"
        "(Camilla is somewhere on a yacht, enjoying herself.)"
        jump ddoutcome
    
    label ddoutcome:
        if drugdealerarrest in choices:
            "(That motherfucker is in jail.)"
            "(I never have to deal with him again.)"
            "(I'm sorry I couldn't stop her from overdosing.)"
            "(But that's life.)"
        else:
            "(John got his drug operation up and running again.)"
            "(He tries to invite me over, but I turn him down.)"
            "(I'm sure he'll do fine without me.)"
    
    scene 07kingending
    "(With the divorce finalized, Mom retired from real estate.)"
    "(She spends most of her days lounging around the house.)"
    scene 09kingending
    reina "There you are."    
    "(Of course, when I'm not busy helping the others, I spend most of my free time with her.)"  
    scene black with fade
    show text "The King of MILFs: End" with Pause (5)
    jump endingscreen
    
