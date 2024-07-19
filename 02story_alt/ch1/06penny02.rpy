label pennyevent02:
    scene 01penny02
    "(This is a huge skatepark. Where is she?)"
    scene 02penny02
    "(There she is.)"
    scene 03penny02
    penny "[player_name]!"
    if pennymeet in choices:
        penny "You came to see me, like you promised!"
        main "Yeah, I came to see the next family star athlete."
    else:
        penny "You're really alive! And you came to see me!"
        main "Yeah, Mom told me you were here."
        main "Planning on becoming a pro skater?"
    scene 04penny02
    penny "Haha, very funny."
    scene 05penny02
    penny "Over here."
    scene 07penny02
    penny "I just wanted to get away from the crowd."
    scene 08penny02
    main "What are you looking at?"
    penny "Skating Videos, duh."
    scene 09penny02
    penny "Mostly a bunch of dudes doing crazy tricks."
    penny "I want to upload a few videos myself but I don't know if I should."
    menu:
        "You should.(+ 2 Penny Love)":
            scene 10penny02
            $PennyC.love_up(2)
            penny "Hmm."
            penny "I can't do it on my own. And not right now, when I'm still learning."
        "It's time-consuming.(+ 2 Penny Trust)":
            $PennyC.trust_up(2)
            scene 10penny02
            penny "Is it?"
            main "You could be spending more time editing videos than skateboarding."
            penny "Oh, true."
    scene 11penny02
    penny"I'll never be as popular as her, will I, [player_name]?"
    main "Who?"
    penny"Bri."
    main "Penny."
    scene 14penny02
    penny"She's tall, athletic, and pretty."
    penny"Not to mention she's Dad's favorite."
    penny"Everything goes her way and I'm just invisible to him."
    if brianaevent01.status=="completed":
        main "Bri has her own share of problems."
        main "She's not perfect."
        penny"She's good enough!"
        penny"But you're not! But I'm not!"
    else:
        main "No you're not."
        penny"You really don't know, do you?"
    scene 12penny02
    penny"Dad didn't  want to pay for your rehab."
    penny"He called you useless and said I would turn out the same way."
    penny"He only pays attention to Bri! He doesn't even talk to Mom- he just yells at her."
    scene 13penny02
    penny"Sometimes..I wish he would just leave and never come back."
    penny"I wish he and Mom would get a divorce already."
    main "Penny you don't mean that-"
    scene 15penny02
    penny "I do."
    penny "I hate him with all of his guts. He kicked you out, then blamed Mom for everything."
    penny "And in return Mom became mean, just like him."
    penny "If he doesn't move out soon, I'll just run away."
    scene 16penny02
    main "Where are you going?"
    penny "I'm going to skate this frustration off."
    penny "Will you hold my phone for me?"
    main "Sure."
    scene 17penny02
    penny "Don't drop it! That's my third one this year."
    show pennyskate4 with Pause (3)
    scene pennyskate2
    main "Smile!"
    scene pennyskate1
    if pennyevent01=="completed":
        scene 23penny02
        penny "Hey, what-what are you doing?"
        main "I'm going to upload this."
        penny "No, please don't!"
        main "Just kidding."
        scene 22penny02
        penny "Not funny, [player_name]."
        penny "Give me my phone back."
    else:
        menu:
            "Upload the videos.":
                scene 23penny02
                penny"Hey, what are you doing?"
                main "Uploading your videos."
                $choices.append(pennyvideoupload)
                penny"But-but-but-hey!!!"
                main "And done."
                penny"Oh my god-"
                main "It's processing now. But it'll be online shortly."
                main "Just try it out. One video. Unedited. Unfiltered."
                scene 22penny02
                penny"Fine."
                penny "Give me my phone back."
            "Don't upload the videos.(+2 Penny Trust)":
                $PennyC.trust_up(2)
                scene 22penny02
                penny "Hey, what were you doing with my phone?"
                main "Taking a few videos."
                main "I didn't upload them."
                scene 20penny02
                penny "Oh really? Thanks."
                main "Take a look at them. If you like them, keep it. If not, we can take more later."
                penny "Ok, I will."
    scene 19penny02
    penny "Thanks for coming to visit me, [player_name]."
    penny "I'm sorry about earlier."
    scene 24penny02
    $pennyevent02.status_completed("not completed")
    penny"It's getting late. I don't want to miss the bus again."
    penny"See you later, [player_name]."
    stop music
    jump freeroamch1