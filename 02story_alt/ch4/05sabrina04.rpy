label sabrinaevent04:
    scene 01sabrina04 with fade
    "(There's not a lot of people here.)"
    scene 02sabrina04
    sabrina "[player_name]!"
    sabrina "Thanks for coming, [player_name]."
    main "There's not a lot of people here."
    scene 03sabrina04
    sabrina "Yeah. Jane was ..the black sheep of the family."
    sabrina "And she wasn't popular in high school."
    sabrina "I'm happy you came, though."
    scene 04sabrina04
    sabrina "It means a lot to me. And to her."
    scene 05sabrina04
    "Is this everyone?"
    sabrina "Yes."
    scene 06sabrina04
    $sabrinaevent04.status_completed("not completed")
    "We are gathered here today to remember Jane Smith, loving daughter, cousin and friend..."
    "(He's not here.)"
    "(I know he really loved her, but-)"
    "(Shit, they probably blame him for her death.)" 
    scene 08sabrina04
    "And now for the Eulogy."
    scene 09sabrina04
    sabrina "Passionate. Creative. Stubborn. Loving. Sincere. Honest. These are just a few words that describe Jane."
    sabrina "Though not everyone understood her as well as she understands others-"
    if sabrinapregnancy in choices:
        scene 10sabrina04
        "(Is something wrong?)"
        scene 11sabrina04
        main "Sabrina??"
        scene 12sabrina04
        sabrina "Yeah. I'm a little dizzy."
        main "Do you want me to finish the eulogy?"
        scene 13sabrina04
        sabrina "No, I can finish it."
    else:
        pass 
    scene 14sabrina04
    sabrina "Janie loved everyone equally. She cared more than you can imagine."
    sabrina "Janie cared about the environment. She worried about a future would you couldn't hear the birds chirp or the bees buzz."
    sabrina "Janie cared  and she had plans- plans to protect our forests and beaches." 
    scene 15sabrina04
    sabrina "Even if no one helped her, Janie was prepared to do everything on her own."
    sabrina "But that's over now. She can rest in peace in the place where she belongs."
    scene 16sabrina04
    sabrina "If there's one thing Jane wanted for everyone is to enjoy the present and not ruin the future."
    sabrina "So-so-so-"
    scene 17sabrina04
    main "It's ok, Sabrina."
    scene 18sabrina04
    sabrina "So we'll honor Janie today with a moment of silence, followed by planting the seeds to her garden."
    sabrina "Thank you."
    scene 19sabrina04
    "Thank you for those kind words."
    if sabrinapregnancy in choices:
        scene 20sabrina04
        main "How are you feeling?"    
        sabrina "I'm still dizzy."
        sabrina "You lost too much weight, you big teddy bear."
        scene 21sabrina04
        sabrina "So tired."
        main "What about the garden?"
        scene 22sabrina04
        sabrina "It's done, we're just going to sprinkle her ashes over it."
        sabrina "Can you help me over there? Please?"
        main "Sure."
    else:
        scene 20sabrina04
        "(I should comfort her.)"
    scene 06sabrina04
    "And now for the dedication."
    scene 24sabrina04
    sabrina "Thank you. Everyone over here please."
    scene 25sabrina04
    "(This is a nice garden. Sabrina did all of this by herself.)"
    scene 26sabrina04
    sabrina "Good bye, Janie."
    scene 29sabrina04 
    sabrina "So, how did I do?"
    sabrina "Be honest."
    main "You did well. It's a funeral. Crying is normal."
    scene 30sabrina04
    sabrina "Thanks."
    sabrina "Let's go back to my place."
    scene 31sabrina04 with fade
    sabrina "Even though I live here by myself, it feels even emptier than before."
    sabrina "I gave out hope that one day, Janie would return.."
    sabrina "With more tattoos and piercings. But she would come back."
    scene 32sabrina04
    sabrina "And we..we would have fun again, like always."
    main "Sabrina."
    scene 33sabrina04
    sabrina "But she's gone."
    sabrina "A drug overdose. She never stopped."
    sabrina "Janie, you fool."
    scene 34sabrina04
    sabrina "No, it's my fault. I should've stopped her."
    main "It's not your fault. It's-it's hard to stop."
    sabrina "How did you do it?"
    main "Rehab. Then living here. Hard to get a high when there's no drug dealers around."
    scene 35sabrina04
    sabrina "You make it sound so simple."
    main "It's not. I still get cravings."
    sabrina "And how do you deal with them?"
    main "By doing other things. Mostly working."
    scene 36sabrina04
    sabrina "That sounds horrible."
    if camillaevent04.status == "completed":
        sabrina "You work for that clothing lady, don't you?"
        main "Not anymore."
        scene 37sabrina04
        sabrina "She's really big and scary. Like a video game villain."
        main "Harsh."
        sabrina "I hope I never get as big as her."
    else:
        pass
    if miyukievent02.status == "completed":
        sabrina "I saw you talking to that mayor lady."
        main "She isn't mayor yet."
        scene 38sabrina04
        sabrina "She might as well be."
        sabrina "She pretty much bullied me into signing her form."
        sabrina "Calling me a little girl."
        main "That's not very nice."
    else:
        pass
    scene 39sabrina04
    sabrina "You hang out with that boxing star, don't you?"
    main "She's my sister."
    sabrina "Oh, that's right."
    scene 40sabrina04
    sabrina "She's really hot."
    main "Do you want to date her? I'm not sure if she's into girls, but I can ask."
    scene 41sabrina04
    sabrina "No! I'm just-"
    if sabrinapregnancy in choices:
        scene 42sabrina04
        sabrina "Ugh, I feel dizzy again."
        main "Let's get you to the toilet."
        scene 45sabrina04
        "(She's really sick.)"
        scene 46sabrina04
        "(No it can't be.)"
        "(We only had sex twice.)"
        scene 47sabrina04
        sabrina "I think I need to go to the doctor."
        main "Right now?"
        scene 49sabrina04
        sabrina "No. But maybe tomorrow."
        sabrina "Spend the night with me, [player_name]."
        jump mcspendsthenightwithsabrina
    else:
        sabrina "Nevermind."
        scene 44sabrina04
        sabrina "Will you spend the night with me, [player_name]?"
        menu:
            "Sure.":
                jump mcspendsthenightwithsabrina
            "I've got to go.":
                jump freeroamch4
label mcspendsthenightwithsabrina:
    scene 50sabrina04
    sabrina "What time is it?"
    main "It's late."
    scene 51sabrina04
    sabrina "[player_name], we need to talk."
    main "What is it?"
    scene 52sabrina04
    sabrina "I thought about our time together."
    sabrina "We had a lot of fun."
    scene 53sabrina04
    sabrina "I want us to be serious."
    if sabrinapregnancy in choices:
        sabrina "I think-no, I know I'm pregnant."
        sabrina "I've missed my period."
        "(Fuck.)"
        sabrina "I don't want to raise a baby by myself."
        sabrina "So I need to know where you stand."
        jump sabrinapressuresmc
    else:
        sabrina "I don't want to have sex with someone who doesn't care about me."
        sabrina "I want to know where you stand."
        jump sabrinapressuresmc
label sabrinapressuresmc:
    sabrina "I just want to be with you, [player_name]."
    sabrina "And only you."
    sabrina "Is that too much to ask?"
    menu:
        "I do too.":
            scene 55sabrina04
            sabrina "You do?"
            sabrina "We -we can be together?"
            main "Yes."
            $commitments +=1
            sabrina "Can we-can we get married?"
            main "Yes, we can."
            $choices.append(sabrinamarriage)
            scene 56sabrina04
            sabrina "When?"
            main "Soon."
            sabrina "I love you, [player_name]."
            main "I love you too."
            jump freeroamch4
        "Yeah, it is.":
            scene 54sabrina04
            sabrina "I see."
            if sabrinapregnancy in choices:
                sabrina "I thought we would make a nice family together."
                sabrina "But I guess not."
            else:
                sabrina "I thought we could make our relationship work."
                sabrina "I guess not."
            sabrina "This is it for us, then."
            main "I can still visit."
            sabrina "I rather not. You remind me too much of Jane."
            sabrina "Goodbye, [player_name]."
            main "Goodbye, Sabrina."
            jump freeroamch4