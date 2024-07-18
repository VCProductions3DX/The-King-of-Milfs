label prologue:
    play sound "sfx/StereoRain.ogg"
    scene runningstart with Pause(5)
    scene runningpov
    "Where the fuck are you, you piece of shit!"
    scene 01prologue01
    "I just want to talk, [player_name]."
    scene 02prologue01    
    "Man to man, let's sort this shit out."
    scene 03prologue01
    "[player_name]???"
    "(He's gone. I finally lost him.)"
    stop sound
    scene 04prologue01
    "(Here goes nothing.)"
    scene 05prologue01
    "(Reina. You've changed.)"
    scene 06prologue01
    show screen eyeclosing
    "(I can't focus.)"
    "(Fuck.)"
    scene black with fade
    hide screen eyeclosing
    scene 07prologue01
    show screen eyeopening
    "Hey, are you ok? It's late. Do you need a ride home or something?"
    scene 08prologue01
    show text "He looks strung out." at centerright with Pause (2)
    show text "Just leave him there, I'm sure he'll be fine." at centerleft with Pause (2)
    scene 09prologue01
    "Are you kidding? I don't want to feel guilty if he dies on the street like this."
    scene 10prologue01
    "I'm calling an ambulance, hang in there,man!"
    scene 11prologue01
    hide screen eyeopening
    scene black with fade
    show text "Hang in there!" with Pause (4)
    scene 12prologue01 with fade
    erdoctor "We managed to save him in time."
    erdoctor "He didn't have any contact information on him, but we found this business card with your name on it."
    scene 13prologue01
    erdoctor "Do you know this young man?"
    erdoctor "Are you related to him?"
    scene 14prologue01
    reina "I know him, doctor. But I'm not related to him."
    erdoctor "Does he have any family?"
    scene 15prologue01
    reina "No, they all passed away."
    scene 16prologue01
    erdoctor "I'll have the front desk write you down as an emergency contact then."
    erdoctor "Based on his blood tests, there were a number of substances in his body."
    scene 17prologue01
    erdoctor "I recommend taking him to a rehabiliation center before something like this happens again."
    scene 18prologue01
    erdoctor "My staff has prepared a list of facilities to transfer him to when he is released from the hospital. Please look over them."
    scene 19prologue01
    reina "Thank you."
    scene 20prologue01
    reina "Yes. It's him. He's alive. It wasn't an overdose but they're recommending rehab for him."
    scene 21prologue01
    reina "What? No. you can't do this to him!"
    reina "Think of Anna! Would you let her down like this?"
    scene 22prologue01
    reina "Give him another chance, Ethan. Just one. "
    reina "Fine, I'll find a place for him to stay after he's out. But you pay for rehab."
    scene 23prologue01
    reina "Why is he always like this?"
    scene 24prologue01
    reina "[player_name]."
    scene 25prologue01
    reina "You left us seven years ago."
    scene 26prologue01
    reina "I'm so sorry. I'm sorry I wasn't there for you."
    scene 27prologue01
    reina "I'll make it up to you, I promise."
    stop music
    scene black with fade
    show text "4 months later" with Pause (2)
    hide text
    scene 28prologue01 with fade
    receptionist "Hello, [player_name]."
    scene 29prologue01
    receptionist "Congratulations on completing rehab. As part of your recovery program, physical and mental therapy services are offered for free for the next six months."
    scene 30prologue01
    receptionist "Your assigned therapist is Dr. Rose, which is down the hallway to your left."
    receptionist "There are group therapy sessions once a week-"
    scene 29prologue01
    main "Yeah, thanks."
    receptionist "If there is anything else you need, please don't hesitate to visit or call."
    "(Finally, I'm out.)"
    scene 31prologue01
    "(Do I go visit the therapist or leave?)"
    menu:
        "Visit the therapist.":
            jump visittherapist
        "Leave":
            jump leaverehab

label visittherapist:
    scene 32prologue01 with fade
    rose "There you are. Have a seat."
    scene 33prologue01
    rose "[player_name], age 25..."
    scene 34prologue01
    rose "Your mother passed away when you're 3."
    rose "After seven years in foster care, a friend of your mother took you in until you were 18."
    rose "Then you ran away from home when you were 18."
    main "I was kicked out."
    scene 35prologue01
    rose "You have quite a criminal record. Drug possession, illegal camping, driving under the influence-"
    main "That was years ago."
    rose "They're still on your record."
    scene 36prologue01
    rose "So, do you have any plans? A place to stay?"
    main "No."
    rose "Have you contacted your family?"
    main "I don't have a family."
    scene 37prologue01
    rose "Don't say that."
    rose "They paid for your recovery and rehab. At least thank them."
    main "They're not my family!"
    scene 38prologue01
    rose "Fine, how about {i} the people who care about you{/i}?" 
    main "No, I haven't."
    rose "That is the first thing I would do once you leave the office."
    rose "Call them. Thank them for helping you."
    "(Who does this woman think she is? My mom?)"
    scene 39prologue01
    rose "Then I would recommend spending time outside."
    rose "This is a really nice, quiet town. We have two beaches, three parks including a skate park."
    rose "And a low crime rate. The perfect place for a recovering drug addict."
    main " I wasn't an addict!"
    scene 40prologue01
    rose "Acceptance of yourself is a fundamental part of therapy."
    rose "Learning to accept your past, the mistakes you've made, and the condition you have is the first step to your recovery."
    rose "If you don't take this seriously, you will end up in rehab again. Or worse.."
    rose "You could be in jail, or in a morgue."
    main "That's a morbid way of saying things."
    scene 41prologue01
    rose "I am very serious about this, [player_name]."
    rose "It's easy for you to go back to the way you were- on the streets, looking for another high."
    "(She really rubs it in.)"
    scene 42prologue01
    rose "Once you have settled in, I recommend looking for a job.Or pick up a new hobby. Something to occupy your time."
    rose "You have been given a chance to turn your life around, [player_name]."
    rose "Make the most of it."
    rose "That's all for today. I'll see you next week."
    main "Thanks."
    scene 43prologue01
    "(Well that was unproductive.)"
    "(And she expects me to visit her next week.)"
    jump leaverehab

label leaverehab:
    scene 44prologue01
    "(It feels good to finally leave this place.)"
    scene 45prologue01
    "(Fuck, the sun is so bright.)"
    "(Where am I supposed to go?)"
    "(What am I supposed to do?)"
    "(I only have these clothes and my phone.)"
    "(No choice but to call Reina, I guess.)"
    scene 46prologue01
    reina "[player_name]? [player_name] are you there?"
    main "Reina?"
    $prologue01.status_completed("not completed")
    reina "It's really you. Are you out of rehab?"
    main "Yeah."
    reina "I'll come pick you up. I can't wait to see you."
    jump reinaevent01
