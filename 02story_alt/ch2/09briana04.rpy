label brianaevent04:
    play sound "sfx/TrainingPunchingBag.ogg"
    scene 01briana04
    "(It's just Briana again, by herself.)"
    scene 02briana04
    main "Briana?"
    scene 03briana04
    main "Bri?"
    stop sound
    scene 04briana04
    briana "Get out of my way!"
    show 05briana04 with Pause(2)
    scene 06briana04
    briana "I said-"
    scene 07briana04
    briana "[player_name]!"
    briana "I'm sorry, I didn't see you."
    main "You were getting a bit carried away there."
    scene 07briana04
    briana "I can't take a day off, even when I'm training my older brother how to fight."
    briana "Are you ready to start?"
    main "Yes."
    scene 08briana04
    briana "I just need to grab your gloves."
    scene 09briana04
    briana "Here, these are yours."
    main "You bought these for me? "
    briana "I did. "
    scene 10briana04
    briana "Let's start with your stance. "
    scene 11briana04
    briana "Not bad. Now hit the dummy with a few jabs."
    scene 12briana04
    briana "Weak. Hit it harder."
    scene 13briana04
    briana "Harder.Put all of your energy into it. Think of someone who you really want to punch."
    show ethanenters with Pause(2)
    scene 14briana04
    briana "That's it! Now start moving. No one stays still for long. "
    scene 15briana04
    briana "There we go!"
    scene 16briana04
    briana "Keep it up!"
    scene 17briana04
    briana "Let it all out, [player_name]!"
    scene 18briana04
    briana "Woah there!"
    scene 19briana04
    briana "Good job. Your footwork is messy, but that's to be expected. Let's end the session with a bit of cardio."
    scene 20briana04 with fade
    briana "[player_name]."
    scene 21briana04
    briana "We need to start working on my debut. Registration, Marketing, Press- Do you have a business suit? "
    main "I do, actually."
    briana "And what about a watch? Your hair could use a trim too."
    stop music
    main "Bri- "
    briana "[player_name], this is a big deal for me. Everything has to be perfect."
    scene 22briana04
    briana "I'm sorry, [player_name]. I wasn't myself."
    scene 23briana04
    briana "I need some fresh air to clear my head."
    scene 24briana04
    briana "Let's go outside."
    show 30briana04 with Pause (2)
    scene 31briana04
    show 38briana04 with Pause(2)
    scene 39briana04
    main "Briana."
    scene 40briana04
    briana "Every time I think about Dad, I have flashbacks and and and-"
    scene 41briana04
    briana "I feel so small and weak compared to him!"
    scene 42briana04
    briana "I wish-I wish I was strong enough to punch him in the face. Just once."
    scene 43briana04
    briana "Will you punch him for me, [player_name]?"
    scene 44briana04
    briana "Please?"
    menu:
        "That's a lot to ask.":
            scene 45briana04
            main "I'm not that strong."
            scene 46briana04
            briana "I'll just go harder on you during training until you are."
        "Yes. (Briana Love + 2)":
            scene 42briana04
            $BrianaC.love_up(2)
            briana "Thank you, [player_name]."
    stop music
    scene 48briana04
    briana "I feel better now."
    main "When are you going to debut?"
    briana "In three months. There's an amateur fight exhibition I want to go to. A lot of scouts will be there. "
    main "When do we sign up?"
    scene 47briana04
    briana "Registration is opening soon."
    main "Are you ready?"
    scene 49briana04
    briana "Yeah, I'll be ready. "
    briana "When it happens, I want everyone to be there. Mom,Aisha, Sis."
    scene 50briana04
    briana "Thanks, [player_name]. You're the only person I can depend on right now."
    $brianaevent04.status_completed("not completed")
    scene 51briana04
    briana "It's getting late. I'll see you tomorrow."
    main "Tomorrow?"
    scene 52briana04
    briana "Yes! You have to train every day if you want to get better!"
    scene 53briana04
    briana "Goodbye, [player_name]."
    jump freeroamch2pt2

