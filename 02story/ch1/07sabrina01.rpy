label sabrinaevent01:
    scene 01sabrina01 with fade
    "(Here it is.)"
    "Hello, welcome to-"
    scene 02sabrina01
    "[player_name]!"
    "It's really you!"
    scene 03sabrina01
    main "Sabrina?"
    scene 04sabrina01
    sabrina "So you {i}do{/i} remember me."
    main "You look completely different. You used to have black hair."
    main "And you were much shorter."
    scene 05sabrina01
    sabrina "Well it has been six months since we've seen each other."
    scene 06sabrina01
    sabrina "You look different as well. You're a lot bigger."
    main "I'm not that fat, am I?"
    scene 07sabrina01
    sabrina "No, just a little chubby. Like a teddy bear."
    main "Oh thanks."
    sabrina "I think you're cute."
    sabrina "And you don't look as sick. Are you...sober?"
    scene 08sabrina01
    main "Yeah, I'm clean. I went to rehab."
    scene 09sabrina01
    sabrina "You really did it."
    main "What are you doing here?"
    scene 10sabrina01
    sabrina "This is my parents' shop. They opened it 5 years ago."
    sabrina "Three months ago they decided to go on a trip. An extended honeymoon. So they left me in charge."
    sabrina "And you? Do you live here now?"
    scene 11sabrina01
    main "Yes. My caretakers live here, so here I am."
    sabrina "Starting over."
    $sabrinaevent01.status_completed("not completed")
    scene 12sabrina01
    sabrina "Well, do you want to hangout sometime? My apartment is upstairs."
    sabrina "We can hangout and play video games like we used to."
    scene 13sabrina01
    sabrina "What do you say? It'll be old times."
    menu:
        "Accept.":
            scene 15sabrina01
            sabrina "Yay!"
            scene 16sabrina01
            $choices.append(sabrinadate)
            sabrina "Just so you know, I've gotten a lot better."
            sabrina "I even stream from time to time."
            main "You're a streamer?"
            scene 20sabrina01
            sabrina "That's how I came up with the name PinkPrincess."
            sabrina "But I won't stream when you come over."
            sabrina "I don't want people thinking you're my boyfriend."
            scene 08sabrina01
            sabrina "I need to finish cleaning before customers come in."
            sabrina "I'll see you later, [player_name]."
            stop music
            jump freeroamch1
        "Reject.":
            scene 18sabrina01
            sabrina "Aww, ok."
            scene 19sabrina01
            sabrina "Maybe we can hangout at your place, then."
            sabrina "I need to finish cleaning before customers come in."
            scene 21sabrina01
            sabrina "I'll see you around, [player_name]."
            stop music
            jump freeroamch1
