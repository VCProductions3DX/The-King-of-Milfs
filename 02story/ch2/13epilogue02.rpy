label epilogue02event:
    scene 01epilogue02 with fade
    "(There's nothing good on TV.)"
    play sound "sfx/knocknock.ogg"
    scene 02epilogue02
    "(Who's there?)"
    stop sound
    scene 03epilogue02
    main "Jenni,What are you doing here?"
    jenni "Tonight is the Town Hall meeting, remember?"
    scene 04epilogue02
    jenni "Let's go. I don't want to be late."
    play sound "sfx/crowdtalking.ogg"
    scene 05epilogue02 with fade
    jenni "There are so many people here."
    scene 06epilogue02
    jenni "There are no seats up front."
    scene 08epilogue02
    jenni "Let's sit back here."
    "(I see a lot of familar faces here.)"
    scene 09epilogue02 
    "(There's Sabrina.)"
    scene 10epilogue02 
    "(Dr. Rose.)"
    scene 11epilogue02
    "(And Camilla.)"
    show 12epilogue02 with Pause(2)
    scene 13epilogue02
    stop sound
    if camillaevent02.status == "completed":
        "(I've seen that woman before.)"
        scene 14epilogue02
        "(She was one pestering Camilla.)"
    else:
        main "Who is this woman?"
        scene 14epilogue02
        jenni "She's a City Councilwoman."
    play sound "sfx/microfeedback.ogg"
    scene 15epilogue02
    "May I have everyone's attention please?"
    stop sound
    scene 16epilogue02
    "Good evening everyone, my name is Miyuki Hayashibara."
    miyuki "Thank you all for coming to tonight's town meeting."
    scene 17epilogue02
    miyuki "This will be first of many Town Hall meetings regarding the Sierra Beach Revitalization Project."
    miyuki "If you could all direct your attention to the screen behind me, please."
    scene 18epilogue02
    miyuki "The Sierra Beach Revitalization Project is a proposed project to bring new businesses to Sierra Beach."
    scene 19epilogue02
    miyuki "The first part of the Revitalization Project is adding over 100 businesses to Sierra Beach."
    scene 20epilogue02
    miyuki "This will involve building a new shopping and lifestyle plaza along the beach."
    jenni "You've got to be kidding me."
    scene 21epilogue02
    miyuki "The second part of the Revitalization Project will be the development of North Sierra Beach."
    miyuki "This area will turn into a world-class luxury resort."
    scene 23epilogue02
    miyuki "We project the annual revenue of this project, once completed, to be over 20 million dollars."
    jenni "That's outlandish."
    scene 25epilogue02
    miyuki "This Revitalization Project will bring much needed business and life back to Sierra Beach."
    scene 26epilogue02
    miyuki "The first step is getting the community onboard with the project."
    scene 27epilogue02
    miyuki "We cannot start this project without the support of you, the residents of Sierra Beach."
    scene 28epilogue02
    miyuki "If you look at the current map, this is proposed area for the project."
    scene 29epilogue02
    camilla "How will the first part of the project affect current business owners?"
    scene 30epilogue02
    miyuki "The first phase of the project will occur in different phases. Business owners will have adequate time to move from their old location to the new one."
    scene 31epilogue02
    miyuki "Tonight is the beginning of many more Town Hall meetings. The next Town Hall meeting will discuss rezoning proposals for the project."
    miyuki "Thank you for your time and have a good night."
    scene 32epilogue02
    jenni "That wasn't much of a meeting at all."
    jenni "I'm going to talk to Camilla to get more details."
    scene 33epilogue02
    play sound "sfx/crowdtalking.ogg"
    "(I won't interrupt their conversation.)"
    scene 34epilogue02
    miyuki "Things went as you expected, Ethan."
    miyuki "A lot of confusion and shock."
    "(She's talking to Ethan?!)"
    miyuki "We'ved worked on this project for 5 years."
    miyuki "I will continue to lobby the town council for approval on next year's ballot."
    scene 35epilogue02
    miyuki "I'll see you later. I love you."
    stop sound
    scene 36epilogue02
    miyuki "Oh hello."
    scene 37epilogue02
    miyuki "Have we met before?"
    if camillaevent02.status == "completed":
        main "Yes, we have."
    else:
        main "No, we haven't."
    scene 38epilogue02
    miyuki "It's a pleasure to meet you."
    scene 39epilogue02
    miyuki "Campaign season is starting soon, I could use some volunteers."
    scene 40epilogue02
    miyuki "Here is my business card, my office is located on the back."
    scene 41epilogue02
    miyuki "I have to go now."
    scene 42epilogue02
    "(Miyuki Hayashibara. So she's Ethan's mistress.)"
    scene 43epilogue02
    jenni "There you are."
    main "Hi Jenni."
    scene 44epilogue02
    jenni "Is something wrong?"
    main "I have something important to tell you."
    scene 45epilogue02
    jenni "Let's go to my car."
    scene 46epilogue02 with fade
    jenni "So what did you want to tell me?"
    scene 47epilogue02
    main "I overheard a conversation between that chairwoman ..and Ethan."
    main "I think they're in a relationship."
    scene 48epilogue02
    jenni "Her? Of all people?"
    scene 49epilogue02
    jenni "Do not tell anyone, especially not Reina."
    scene 50epilogue02
    $epilogue02event.status_completed("not completed")
    jenni "I will tell her when I think the time is right."
    scene black with fade
    show text "End of Chapter 2" with Pause (5)
    "Would you like to save your progress?"
    menu:
        "Yes":
            call screen save
            jump prologue03
        "No":
            jump prologue03
