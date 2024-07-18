label reinaevent04:
    scene 01reina04
    "[player_name]?"
    "[player_name]? Where are you?"
    main "Back here."
    scene 02reina04
    reina "Oh, there you are."
    scene 03reina04
    reina "How do you like the backyard?"
    main "It's nice."
    scene 04reina04
    reina "It is. I don't have a swimsuit, otherwise I would take a dip in the pool."
    main "But you live by the beach."
    scene 05reina04
    reina "I know. It's kind of shameful, really."
    scene 06reina04
    reina "I think the last time I wore any kind of swimsuit was before I had kids."
    reina "It's almost time for your appointment."
    scene 07reina04
    main "Appointment?"
    reina "Yes, with your therapist. Let's go."
    scene 08reina04 with fade
    main "I'm fine by myself, Reina."
    reina "I'm sure she won't mind my presence."
    scene 09reina04 
    rose "Just one second."
    scene 10reina04
    rose "Welcome back, [player_name]."
    main "Thanks, Dr. Rose."
    scene 11reina04
    reina "Hello Dr. Rose. I'm Reina, [player_name]'s caretaker."
    reina "Do you mind if I sit with him? He's recovering from an injury."
    rose "Sure."
    scene 12reina04
    rose "So, how have you been? Why is your arm in a cast?"
    main "I was attacked the other night."
    scene 13reina04
    rose "Oh dear."
    scene 14reina04
    reina "It was awful. He was in the hospital for two weeks."
    reina "If only he was in my house, then it wouldn't have happened."
    scene 15reina04
    rose "Ms. Reina-"
    scene 16reina04
    reina "But he wasn't and he got attacked! It was my fault! I shouldn't have agreed to his terms!"
    rose "His?"
    scene 17reina04
    reina "I can't even keep a promise to a dead friend! I've failed in every way!"
    scene 18reina04
    reina "What did I do to become such a horrible person?"
    scene 22reina04
    rose "Reina, you don't need to blame yourself for [player_name]'s accident."
    rose "You are not a horrible person."
    scene 23reina04
    reina "Then why did I marry the most selfish, ungrateful man in the world?"
    reina "Why did I build a family with him?!?!"
    reina "Tell ME!"
    scene 25reina04
    rose "Reina, this is [player_name]'s therapy session, not yours."
    rose "If you would like a session, please go outside and make an appointment at the front desk."
    scene 24reina04
    reina "I'm sorry."
    scene 26reina04 with Pause (1)
    scene 27reina04 with fade
    rose "Now that she's gone. The two of us can talk."
    scene 28reina04
    rose "Is this the first time she's acted in this manner?"
    main "She's cried before, but yelling is new. I've never known her to yell before."
    scene 29reina04
    rose "So that's how things are. "
    rose "I know a broken marriage when I see one."
    main "But-"
    scene 31reina04
    rose "Trust me, I've been a therapist for 20 years. Martial problems are the easiest to spot."
    rose "Look at the time. I'm sorry we didn't make much progress today. However, next time we can make up for it."
    scene 34reina04
    rose "I'll see you again in two weeks-and next time come by yourself."
    main "I will, thanks."
    stop music
    scene 35reina04 with fade
    main "Reina?"
    "(Is that her in the distance?)"
    scene 36reina04
    "(It is.)"
    scene 38reina04
    reina "Hey [player_name], I didn't notice you there."
    scene 39reina04
    reina "I was just enjoying the view."
    scene 40reina04
    reina "So how did your session go."
    main "It was short."
    scene 42reina04
    reina "I made quite a show back there, didn't I?"
    scene 41reina04
    reina "I'm sorry for that outburst, [player_name]. It's not right."
    scene 43reina04
    reina "I guess I need a bit of therapy myself."
    if divorcesuggest in choices:
        scene 44reina04
        reina "I thought about what you said after our fight."
        scene 46reina04
        reina "Divorce is such a huge step."
        reina "It's a lot of paperwork and so time-consuming."
        reina "We'll have to split assets- I don't even know if I'll get the house."
        reina "Then there's all of Briana's earnings, all of the properties I have, his business-"
        scene 47reina04
        main "Isn't that the attorney's job? To figure out who gets what."
        reina "You're right but we share so much together."
    else:
        reina "I signed up for a couple's therapy session but I'm not even sure if he wants to go."
        reina "I really don't want to divorce him."
    scene 51reina04
    reina "I just wonder if there was any way to avoid this."
    scene 48reina04
    reina "Maybe I shouldn't have gotten my real estate license."
    reina "Or not cut my hair."
    main "Reina, it's not your fault."
    scene 49reina04
    reina "You always knew this side of him, didn't you?"
    main "I was his punching bag."
    scene 50reina04
    reina "Why didn't I see this earlier."
    reina "If I had, you wouldn't have-"
    main "Reina."
    scene 52reina04
    reina "I won't cry again. But I need to make things up for you."
    scene 53reina04
    reina "We've lost so much time together."
    if reinakiss in choices:
        scene 54reina04
        reina "I still remember our kiss."
        main "Reina, I'm sorry-"
        if reinabj in choices:
            scene 55reina04
            reina "I think we made out as well."
            "(She doesn't remember the blowjob?)"
            main "Yeah, we did. I'm really sorry, Reina."
            scene 56reina04
            reina "I forgive you. You are a young man with no girlfriend, I'm an emotional wreck. It happened."
            reina "It's just-it's all a bit too much for me right now."
            reina "I need time and space to think about everything."
            scene 57reina04
            reina "But, when the time is right, we can go on a date."
            main "A date?"
            reina "Yes, a date. A nice, relaxing restaurant. Just the two of us."
            reina "But I'm so happy that you're healthy and sober."
            jump reinasresolution
        else:
            scene 56reina04
            reina "It was a very sweet kiss. Not unlike my husband's when we first met."
            reina "I won't forget it. Not for a while."
            reina "I just need a little space, if you don't mind."
            main "Sure."
            scene 57reina04
            reina "When I'm free, the two of us can go on a date. How does that sound?"
            main "Sounds great."
            reina "I'm just happy that you're healthy and sober."
            jump reinasresolution
    else:
        jump reinasresolution
label reinasresolution:
    scene 58reina04
    reina "It's time for me go back to work."
    reina "Will you be ok on your own?"
    if pennyevent03.status == "completed":
        main "Yes, but Penny wants to buy a guitar."
        scene 60reina04
        reina "Does she? I never took her to be the music type."
        reina "Are you out of money already?"
        main "Uh-"
        scene 61reina04
        reina "I'll extend your credit limit just for her."
        main "Thanks."
        reina "I suppose you'll need a car as well."
        reina "You can borrow one of mine."
        jump toreinasgarage
    else:
        scene 62reina04
        reina "The police still haven't found your attacker."
        "(Not this again.)"
        reina "I just don't want the person who buys the cottage to be the next victim."
        "(Fuck, she's right.)"
        scene 61reina04
        reina "If there's anything you know, don't hesitate to tell the police."
        main "I won't."
        reina "Hmm, they might have attacked because there was no car there."
        reina "You can borrow one of mine."
        jump toreinasgarage
label toreinasgarage:
    scene 65reina04 with fade
    reina "I think this one will do."
    $reinaevent04.status_completed("not completed")
    main "Thanks again, Reina."
    scene 66reina04
    reina "You're welcome. I need to go back to work."
    reina "I'll see you later."
    jump freeroamch2pt2

    

