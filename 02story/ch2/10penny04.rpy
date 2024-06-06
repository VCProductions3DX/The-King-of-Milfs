label pennyevent04:
    scene 01penny04
    "(Sheesh, what's taking her so long.)"
    scene 02penny04
    penny "Good morning, [player_name]."
    main "It's after 12."
    scene 03penny04
    penny "Is it? I didn't realize it was so late."
    penny "What are you doing here anyways?"
    main "I came to check on you."
    scene 04penny04
    penny "You're so caring."
    penny "But I'm fine. It's not like anyone here notices me anyways."
    main "That's not true."
    scene 05penny04
    penny "Ok, so maybe Aunt Jenni a little bit."
    penny "She does make some good food."
    scene 06penny04
    penny "But Mom, Dad, Sis...I'm nothing to them."
    penny "Then again I don't think they like each other any more."
    main "Reina is going to go to therapy."
    scene 07penny04
    penny "Is she?"
    penny "About time. Better than her drinking all of the time."
    main "Penny."
    scene 08penny04
    penny "Ok, not all of the time, but enough she should stop."
    penny "It just turns her into Dad."
    scene 09penny04
    penny "And I hate him."
    "(Damn, Ethan really ruined our family.)"
    "(I need to fix things and make it better.)"
    scene 10penny04
    main "I told Reina about your music interests."
    main "She said I can buy you a guitar."
    scene 11penny04
    penny "REALLY?!?!"
    scene 12penny04
    penny "So you're going to take me now, right, right?!?!?!"
    main "Yeah, if you want."
    main "That's why I'm here."
    scene 13penny04
    penny "Yay!! You're the best."
    scene 14penny04
    "(One step at a time.)"
    jump tomusicstore
label tomusicstore:
    scene 15penny04 with fade
    "(We managed to get here in one piece.)"
    scene 16penny04
    penny "It's so big."
    main "Is this your first time to a music store?"
    penny "Yeah."
    scene 17penny04
    penny "They have both acoustic and electric guitars."
    scene 18penny04
    penny "So many different brands and styles."
    scene 19penny04
    main "Changing your mind on the guitar?"
    scene 20penny04
    penny "Mmmm, maybe."
    scene 21penny04
    penny "I've always had my heart set on a guitar but now I'm not sure."
    scene 22penny04
    penny "This looks cool, too."
    scene 23penny04
    musicclerk "Hello, are you interested in buying the xylophone today?"
    musicclerk "We're currently on a backorder for that, but I can place a reservation-"
    penny "No, no uhm."
    main "We're interested in guitars."
    scene 24penny04
    musicclerk "So, what are we in the mood for today? First off, acoustic or electric?"
    scene 25penny04
    penny "I don't know."
    musicclerk "Is this your first guitar?"
    penny "Yes."
    scene 24penny04
    musicclerk "Electric is easier on the fingers, but you'll need to buy an amplifier."
    musicclerk "Acoustic is a harsher on the fingers, but you won't need an amplifier and tuning it will be easier."
    musicclerk "It's based on your music preference."
    scene 29penny04
    penny "Uh.."
    main "Is there a way to try both before buying?"
    musicclerk "We do have a 30-day return policy so if you don't like the first guitar, you can return it as a store credit for another one."
    penny "I can have both of them?"
    main "If you don't like one, you can get the other."
    penny "Really??"
    scene 30penny04
    musicclerk "Which one would you like to try first?"
    penny "That one."
    musicclerk "Oh we just get a new shipment of those. I'll go grab one for you."
    penny "Thanks."
    main "Did you want to buy a guitar book?"
    scene 31penny04
    penny "Yeah, I guess."
    main "What's wrong?"
    penny "I don't know. I thought I would be happier."
    penny "I don't want to talk about it here."
    scene 34penny04
    musicclerk "Here we go. Everything is included."
    musicclerk "Thank you. Here is the receipt. Remember if you're not satisfied, be sure to come back in 30 days and we'll help find another one."
    main "Thank you."
    jump pennyriverside
label pennyriverside:
    scene 35penny04
    main "What's on your mind?"
    scene 36penny04
    penny "You."
    main "Me?"
    penny "Yeah. You were gone for seven years, then you come back and everything awesome is happening."
    scene 37penny04
    penny "Ick. 'Awesome.' Not the right word."
    penny "Why are you doing all of this?"
    main "I just want to set things right."
    main "And I don't want to repeat my mistakes."
    scene 38penny04
    penny "I thought about running away myself."
    penny "It's not like anyone would notice or care."
    main "Of course they would. Your mom cares about you."
    main "But you're too closed off for anyone to get close."
    scene 39penny04
    penny "Pfft. It doesn't even matter."
    scene 40penny04
    if pennyvideoupload in choices:
        penny "Thanks to you, I'm popular now."
    else:
        penny "I'm getting a lot of followers online after posting my videos."
    scene 41penny04
    penny "I recorded more videos of myself."
    scene 42penny04
    penny "And a lot more selfies."
    scene 43penny04
    penny "Though I do get some creepy requests."
    main "Requests?"
    scene 44penny04
    penny "Yeah, for my shoes. One offered to send me money to get a tattoo. It was weird."
    main "Just ignore them, they're perverts."
    penny "I blocked them. Still it's nice having attention for once."
    main "Don't let it get to your head."
    penny "I won't."
    scene 45penny04
    penny "I'm not like Aunt Jenni who takes nude photos of herself."
    main "How do you know this?"
    scene 46penny04
    penny "I saw her."
    penny "She came out of the bathroom completely naked, looking at her phone."
    penny "No one normal does that."
    scene 47penny04
    penny "It's so shiny."
    play sound "sfx/pennyfirstguitar.ogg"
    scene 48penny04
    "(I should go back to the music store and ask about guitar lessons.)"
    main "How does it feel?"
    stop sound
    scene 49penny04
    play sound "sfx/pennyguitar2.ogg"
    penny "It's rough. I think I might get an electric guitar instead."
    stop sound
    scene 50penny04
    penny "I just have to rearrange my room."
    scene 51penny04
    penny "I'm going to practice more when we get home."
    penny "Thanks, [player_name]."
    scene black
    $pennyevent04.status_completed("not completed")
    jump freeroamch2pt2
