label aishaevent01:
    scene 01aisha01 with fade
    "(Who's knocking at the door?)"
    main "Yeah, I'm coming."
    scene 02aisha01
    "(Fuck. It's the police.)"
    "Are you [player_name]?"
    main "Yes."
    scene 03aisha01
    "Detective Aisha Daniels from the Sierra City Police Department."
    main "Sierra City? That's a long drive from here."
    aisha "It is."
    main "What are you doing out here?"
    scene 04aisha01
    aisha "I'll be the one asking questions, [player_name]."
    aisha "Recently you were the victim of a late-night assault, correct?"
    main "Yes."
    aisha "According to the report, the description of the suspect is of interest to our department."
    scene 05aisha01
    aisha "Do you happen to recognize this person?"
    scene 06aisha01
    "(Shit it's her.)"
    main "I-uh-"
    scene 07aisha01
    aisha "Oh, wrong picture."
    scene 08aisha01
    aisha "There we go."
    scene 09aisha01
    aisha "Here. The gentleman on the left."
    scene 10aisha01
    "(That's him alright.)"
    scene 11aisha01
    aisha "Well, do you?"
    menu:
        "(Lie)":
            main "No."
            scene 13aisha01
            aisha "Are you sure? Because he fits the description."
            main "I don't know. I don't really remember much from the other night."
            main "It was too dark to see anything."
            scene 14aisha01
            "(Is she buying my story?)"
            scene 15aisha01
            aisha "Ok. Here's my card. If your memories come back and you do remember him, don't hesitate to call."
            main "Yeah, sure thanks."
            scene 17aisha01
            "(I don't plan on calling her, ever.)"
            scene 18aisha01
            camilla "There's an unwelcome sight. Sierra City Police."
            main "Camilla!"
            scene 01camilla03
            camilla "Hello there."
            camilla "I didn't know they would get involved with our problems."
            jump camillaevent03
        "(Tell the Truth)":
            main "Yeah, I know him."
            $choices.append(aishacooperate)
            main "His name is Jon, he's a drug dealer."
            scene 12aisha01
            aisha "And what is his relationship to you?"
            main "I..lived with him."
            scene 13aisha01
            aisha "Is he the person who attacked you the other night?"
            main "Yes."
            scene 14aisha01
            aisha "Shit."
            main "Is something wrong?"
            aisha "No, it's nothing."
            scene 15aisha01
            aisha "Here's my card. If you have any more information to share, or if you see him again, don't hesitate to call."
            main "Yeah,sure thanks."
            scene 17aisha01
            "(She came all this way to see me.)"
            scene 18aisha01
            camilla "Well, that's an unwelcome surprise. Sierra City Police. "
            main "Camilla! You scared me."
            scene 01camilla03
            camilla "Hi there."
            camilla "I thought we were far away from the city to get them involved."
            jump camillaevent03



    