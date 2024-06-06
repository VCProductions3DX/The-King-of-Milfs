label camillaevent04:
    show 01camilla04 with Pause (2)
    scene 02camilla04
    camilla "There you are."
    camilla "Come inside."
    scene 04camilla04
    camilla "Today is officially the last day of business."
    camilla "I don't expect a lot of people, there isn't much left."
    main "What happens when you close for good?"
    scene 05camilla04
    camilla "I'll probably just donate what I don't sell to a shelter."
    main "You're not keeping any of it for yourself?"
    scene 06camilla04
    camilla "I did that before I put those signs up."
    scene 07camilla04
    camilla "Oh how I will miss this place."
    camilla "I don't miss stocking, however."
    scene 08camilla04
    camilla "Last time I have to do this."
    scene 09camilla04
    "(Wow, it's really empty.)"
    main "So what do I do?"
    scene 10camilla04
    camilla "You'll be over here by the register."
    camilla "Keep your eye out for any thieves."
    camilla "If someone needs help, point them my way."
   

    scene 11camilla04

    scene 12camilla04
    camilla "Here we go."
    scene 13camilla04

    scene 14camilla04




    scene 20camilla04
    
    camilla "How are you feeling?"
    main "Tired."
    main "Everything is almost gone."
    camilla "Indeed it is."
    camilla "It was a good run."
    camilla "Here you go. For sticking with me all day."
    "(That's a lot.)"
    camilla "Have a seat."
    camilla "It's so hot back here."
    camilla "I hope you don't mind."
    "(What is she doing?)"
    camilla "Much better."
    main "Camilla-"
    camilla "I know you're not intimidated by a woman's body, are you?"
    if camillasex is in choices:
        camilla "Besides, you've seen it before."
        camilla "You even liked it."
    else:
        camilla "I know you're not a virgin."

    main "So what are your plans now?"
    camilla "Once all of this is gone, I'm going to sell my house."
    main "But your kids-"
    camilla "They're fine. I'll put their stuff in a storage container."
    camilla "And then it's a cruise. Well, a lot of cruises."
    camilla "The Caribbean, the Mediterranean, Alaska.."
    camilla "Are you interested?"
    main "I-"
    camilla "We could have a lot of fun, just the two of us."
    camilla "I'll be your sugar mama."
    "(She's coming onto me again.)"
    menu:
        "Sure.":
            camilla "Really?"
            main "I'm free. "
            camilla "I knew you would come around."
            jump camillapropositionsmc

        "I'm busy.":
            camilla "Awww."
            camilla "You don't have to join me for all of them. But maybe one or two?"
            main "Maybe."
            jump camillapropositionsmc

label camillapropositionsmc:
    camilla ""