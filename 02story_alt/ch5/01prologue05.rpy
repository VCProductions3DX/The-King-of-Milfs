label prologue05:
    scene 01prologue05 with fade
    "(Damn, I didn't think he would do this.)"
    play sound "sfx/cellvibe.ogg"
    "(And of course he would call me now.)"
    stop sound
    scene 02prologue05
    "There you are, old buddy old pal."
    main "I'm not your friend."
    "Don't be an idiot. You were my right-hand man."
    main "What the fuck is this?"
    scene 03prologue05
    "I need a bit of cash. My supplier's pretty pissed about the hideout getting raided and losing all of that product."
    "He wants five thousand from me before getting me back into business."
    main "Get it yourself."
    scene 04prologue05
    "Says the guy who got my place raided in the first place."
    "Why should I work a lame ass job when I can just get the money from you and your rich family?"
    "I had no idea you and your family were this loaded."
    "I thought you guys were trailer park trash."
    main "Leave them out of this."
    scene 05prologue05
    "You wish."
    "Okay, here's the deal. You come meet me at one of your old hangout spots with the money and I'll give you all of these photos."
    main "When?"
    "Tomorrow evening."
    main "And if I don't?"
    scene 06prologue05
    "I'm going to sell them to those celebrity leak sites."
    "The ones of the boxer chick is worth at least a thousand."
    "The other ones aren't too bad either."
    "I'm sure your mom's nudes can sell for a nice stack."
    main "Fine, I'll meet you there."
    "I know you would cooperate. See you later, loser."
    scene 09prologue05
    "(Shit.)"
    "(If he leaks those photos, Briana's career might flop.)"
    "(There's no telling how angry Dad and Mom would get.)"
    "(And Penny...she almost killed herself.)"
    "(I've got to go.)"
    "(Hmm...)"
    if aishacooperate in choices:
        jump contactaisha
    else:
        "(Should I call Aisha?)"
        "(Turning him in would make all of my problems go away.)"
        menu:
            "(Call Aisha)":
                jump contactaisha
            "(Don't call her.)":
                jump loneconfrontation
label contactaisha:
    scene 07prologue05
    aisha "Hello?"
    main "Hi, this is [player_name]."
    aisha "[player_name]? Why are you calling?"
    main "I have a lead on the primary suspect in your case."
    scene 08prologue05
    aisha "You do?"
    main "Yeah, I plan on meeting him tomorrow in Sierra City."
    aisha "And are you sure this is-"
    main "I'm positive."
    aisha "Where and what time?"
    main "The corner of Front Street and Park Avenue. Behind the old firehouse building. I'll be there after 6 PM."
    aisha "Thank you, [player_name]."
    jump setup
label loneconfrontation:
    scene 10prologue05
    "(It's just me.)"
    scene 11prologue05
    "There you are."
    scene 12prologue05
    "So, the money?"
    main "Where's the photos?"
    scene 13prologue05
    "On this little drive right here. You give me the money, I give you the drive."
    menu:
        "(Punch him.)":
            jump punchdd
        "(Give him the money.)":
            jump giveddmoney
        "(Call his bluff.)":
            main "I don't think you'll do it."
            scene 14prologue05
            "Well, look here aren't we big, bad, and tough?"
            "Don't be a retard. Of course I'm going to fucking sell the photos."
            "So are you going to give me the money are not?"
            menu:
                "No.":
                    scene 15prologue05
                    "If that's how you want it."
                    $choices.append(photosreleased)
                    "Enjoy being famous- or infamous."
                    "Maybe you'll get a TV show if you're smart."
                    scene 30prologue05
                    "(Shit.)"
                    "(He's really going to do it.)"
                    jump returnhome
                "(Punch him.)":
                    jump punchdd
                "(Give him the money.)":
                    jump giveddmoney
label giveddmoney:
    scene 16prologue05
    main "Yeah sure, I'll give you the money."
    "Now we're talking."
    scene 17prologue05
    "Here you go."
    main "And this is it? No other copies?"
    scene 19prologue05
    "Nah. None of those girls are my type anyway."
    "All of the goods are right here."
    "So, are we back in business?"
    menu:
        "Sure.":
            main "Whenever I get away from them."
            scene 20prologue05
            "Tired of the beach already? "
            main "Nothing to do there."
            scene 21prologue05
            "I don't blame you."
            "Give me a month or two to set up shop and I'll call you."
            "Just bring some extra dough in case things go south again."
            main "Yeah, sure."
            scene 22prologue05
            "Thanks man, I mean it."
            jump returnhome
        "Nah.":
            main "We're done."
            scene 28prologue05
            "Aww man, you serious?"
            main "Yeah, I don't ever want to see or hear from you again."
            scene 29prologue05
            "Your loss, buddy."
            "I hear that your little beach town is turning into an amusement park."
            "There's going to be so many tourists coming and going."
            "A lot of money to be made."
            main "It's not happening."
            scene 30prologue05
            "Whatever. Don't come crawling to me if you're back on the streets again."
            main "I won't."
            jump returnhome
    label punchdd:
        scene 24prologue05
        "Shit!"
        scene 25prologue05
        "Ow!"
        "Motherfucker!"
        "(Looks like all of that training paid off.)"
        scene 26prologue05
        main "It's mine now."
        "You are one sick motherfucker."
        main "Good luck getting that money."
        jump returnhome

label setup:
    scene 32prologue05 with fade
    "(There's no one here.)"
    scene 33prologue05
    "(Fuck.)"
    scene 35prologue05
    "Man, why are we here?"
    "You should've picked a better spot."
    main "It's just us. No one was following me."
    scene 34prologue05
    "I hope so. So-the money?"
    menu:
        "(Punch him.)":
            scene 36prologue05
            "What the fuck was that for?"
            "Motherfuck-"
            jump aishaarrestsdd
        "(Do nothing.)":
            main "I don't have it."
            scene 37prologue05
            "Wow, that's it?"
            "Your loss."
            jump aishaarrestsdd
label aishaarrestsdd:
    scene 39prologue05
    "Don't move, put your hands up in the air."
    scene 38prologue05
    "What the fu-"
    "You fucking rat!"
    aisha "You're under arrest for extortion and kidnapping. Take him to the car."
    "Motherfucker!"
    scene 40prologue05
    aisha "Thank you. We would not have caught him without you."
    main "You're welcome. What happens next?"
    scene 41prologue05
    aisha "We interrogate him, he may or may not get bail. Then trial."
    aisha "It's nice finally catching one of the bigger drug dealers around here."
    main "And me?"
    $choices.append(drugdealerarrest)
    scene 42prologue05
    aisha "We have your affadavit, but if we need witnesses you may need to get on the stand."
    aisha "This will be a long trial."
    main "So we'll see each other again?"
    aisha "Maybe. Take care, [player_name]."
    scene 43prologue05
    "(It's finally over.)"
    jump returnhome
label returnhome:
    scene 44prologue05
    "(I'm back.)"
    if photosreleased in choices:
        jump freeroamch5
    else:
        "(What to do with this.)"
        menu:
            "(Keep them for yourself.)":
                $choices.append(photosreceived)
                "(I'll keep them as a memento.)"
                jump freeroamch5
            "(Delete them.)":
                $choices.append(photosdestroyed)
                "No one will ever see them."
                "(It's the right thing to do.)"
                jump freeroamch5

label freeroamch5:
    scene ch5freeroam
    menu:
        "(Attend the Divorce Proceeding.)" if reinaevent09.status == "not completed":
            jump reinaevent09
        "(Visit Jenni.)" if jennievent07.status == "not completed":
            jump jennievent07
        "(Go to Briana's Match.)"  if brianaevent07.status == "not completed":
            jump brianaevent07
        "(Visit Penny in the hospital.)" if pennyevent05.status == "not completed":
            jump pennyevent05
        "(Visit Dr. Rose for the last time.)":
            $pennyevent05.status_skipped("not completed")
            $brianaevent07.status_skipped("not completed")
            $jennievent07.status_skipped("not completed")
            $reinaevent09.status_skipped("not completed")
            jump epilogue05



