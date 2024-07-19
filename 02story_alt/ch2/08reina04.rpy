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
    reina "I think the last time I wore any kind of swimsuit was before you were born."
    main "Really?"
    reina "Yes. I have a swimsuit but...I've never worn it in public."
    main "You should wear one sometime."
    scene 07reina04
    reina "Thanks. Now let's go to your appointment."
    scene 08reina04 with fade
    main "I'm fine by myself, Mom."
    reina "I'm sure she won't mind my presence."
    scene 09reina04
    rose "Just one second."
    scene 10reina04
    rose "Welcome back, [player_name]."
    main "Thanks, Dr. Rose."
    scene 11reina04
    reina "Hello Dr. Rose. I'm Reina, [player_name]'s mother."
    reina "Do you mind if I sit with him? He's recovering from an injury."
    rose "Sure."
    scene 12reina04
    rose "So, how have you been? Why is your arm in a cast?"
    main "I was attacked the other night."
    scene 13reina04
    rose "Oh dear."
    scene 14reina04
    reina "It was awful. He was in the hospital for four days."
    reina "If only he was in my house, then it wouldn't have happened."
    scene 15reina04
    rose "Ms. Reina-"
    scene 16reina04
    reina "But he wasn't and he got attacked! It was my fault! I shouldn't have agreed to his terms!"
    rose "His?"
    scene 17reina04
    reina "My husband! I've never stood up to him when it mattered most!"
    scene 18reina04
    reina "I've failed as a mother!"
    scene 22reina04
    rose "Reina, you don't need to blame yourself for [player_name]'s accident."
    rose "You are not a bad mother."
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
    main "Mom?"
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
    reina "Or sign up for that weight loss program."
    main "Mom, it's not your fault."
    scene 49reina04
    reina "You always knew this side of him, didn't you?"
    main "I was his punching bag."
    scene 50reina04
    reina "Why didn't I see this earlier."
    reina "If I had, you wouldn't have-"
    main "Mom."
    scene 52reina04
    reina "I won't cry again."
    scene 53reina04
    reina "We've lost so much time together."
    if reinakiss in choices:
        scene 54reina04
        reina "I still remember our kiss."
        main "Mom, I'm sorry-"
        if reinabj in choices:
            scene 55reina04
            reina "I think we made out as well."
            "(She doesn't remember the blowjob?)"
            main "Yeah, we did. I'm really sorry, Mom."
            scene 56reina04
            reina "My baby boy is all grown up. A man now, with manly desires."
            reina "It feels like yesterday I was sending you to kindergarten all by yourself."
            reina "A kiss just isn't a kiss any more."
            jump reinasresolution
        else:
            scene 56reina04
            reina "It was a very sweet kiss."
            reina "It made me realize that my baby boy isn't a baby anymore."
            reina "I need to keep that in mind now."
            jump reinasresolution
    else:
        reina "And I need to find a way to make this up to you."
        jump reinasresolution
label reinasresolution:
    scene 57reina04
    reina "I need time and space to think about everything that happened last week."
    main "Yeah, sure."
    reina "But, when the time is right, we can go on a date and talk about it."
    main "A date?"
    scene 58reina04
    reina "Yes, a date. A nice, relaxing restaurant. Just the two of us."
    main "Sure."
    scene 59reina04
    reina "I'm so happy that you're healthy and sober."
    main "Thanks, Mom." 
    if pennyevent03.status == "completed":
        main "Penny wants to buy a guitar."
        scene 60reina04
        reina "Does she? I never took her to be the musical type."
        reina "Are you out of money already?"
        main "Uh-"
        scene 61reina04
        reina "I'll extend your credit limit just for her."
        main "Thanks Mom."
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
    main "Thanks Mom."
    scene 66reina04
    reina "You're welcome. I need to go back to work."
    reina "I'll see you later."
    jump freeroamch2pt2



    

