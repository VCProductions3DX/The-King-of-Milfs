label brianaevent02: 
    scene 00briana02
    "(Man it's a long day.)"
    "(There's sand in my shoes.)" 
    if brianaevent01.status == "skipped":
        play sound "sfx/knocknock.ogg"
        main "Who's there?"
        stop sound
        scene 02briana02
        "[player_name]?"
        main "Who are you?"
        "It's me, [player_name]. Briana!"
        scene 03briana02
        "(Briana?)"
        "(Holy shit- she's changed a lot.)"
        scene 04briana02
        briana "Do you remember me now?"
        main "Yeah-I-I'm sorry."
        scene 05briana02
        briana "I missed you, [player_name]."
        briana "You were like that protective older brother I've always wanted."
        main "Your dad thought otherwise."
        scene 06briana02
        briana "Yeah. Him."
        main "Is something wrong?"
        scene 07briana02
        briana "I-I have a huge announcement to make for everyone."
        briana "Including him."
        main "Ok-"
        scene 08briana02
        briana "I waited until you were out of rehab because-it's really important that you're there, [player_name]."
        main "What's the announcement?"
        briana "You'll know at the same time as everyone else."
        scene 09briana02
        briana "Please, come with me. I need you."
        main "Sure."
        jump brianadrivesmchome
    else:
        "(Someone's calling me.)"
        scene 01briana02
        briana " Hey [player_name], it's me."
        main "Hey Briana, how are you?"
        briana "Nervous. I'm on my way to your house. Where is it?"
        main " I'll come outside."
        jump brianadrivesmchome
label brianadrivesmchome:
    scene 10briana02
    briana "Get in, the pizza's getting cold."
    briana "I was so worried I couldn't find the right house but it's closer to the gym than I thought. "
    scene 11briana02
    briana "For the first time in years, everyone will be together in the same room."
    briana "I thought some pizza would make the announcement go over more smoothly."
    briana "And I got a pizza of every variety, so no complaining."
    scene 12briana02 with fade
    briana "Dad's not home. I think I can do this."
    briana "Time to face the music."
    scene 13briana02
    briana "Pizza's here!!!"
    scene 14briana02
    jenni "Finally, I'm starving."
    jenni "[player_name]? It's good to see you again."
    scene 15briana02
    penny "Pizza?"
    scene 16briana02
    reina "Briana? [player_name]? What are you two doing here?"
    scene 17briana02
    jenni "Let's see, there's pepperoni, supreme,"
    jenni "And what's that over there?"
    scene 18briana02
    briana "It looks like cheese pizza. Strange, I didn't order that."
    briana "I guess we got an extra pizza!"
    scene 19briana02
    jenni "No complaints here!"
    scene 20briana02
    "(Everyone is so relaxed.)"
    scene 21briana02
    penny "So why are we here? Why did you buy pizza for everyone?"
    penny "This isn't like you."
    scene 22briana02
    briana "I have an announcement to make."
    scene 23briana02
    stop music
    briana "I'm retiring from boxing."
    reina "But Bri..."
    scene 24briana02
    briana " I want to do something else. Six years, three championships. That's good enough for me."
    scene 25briana02
    "And who gave you permission to retire?"
    show ethanenters with Pause (3)
    scene 26briana02
    ethan "Do you know how much is riding on your career? And you decide to retire, just before the Olympics?"
    scene 27briana02
    briana "Dad-"
    ethan "Don't {i}dad{/i} me. If it wasn't for me, we would still be living in that shack in shit hole town! It's because of me we're living here!"
    scene 28briana02
    ethan " ou're NOT retiring. You're GOING to compete in the Olympics!"
    scene 29briana02
    penny "This was a waste of time."
    penny "Thanks for the pizza, sis."
    scene 30briana02
    ethan "So the whole peanut gallery is here?"
    ethan "I had a good day at work and I come home to this bullshit."
    ethan "For once can I have a nice, quiet evening at home?"
    scene 31briana02
    briana "Stop It!"
    briana "You always do this! Why do you have to control my life? Why do you have to discard theirs? They are just as important as I am!"
    scene 32briana02
    ethan "Because I make the money in this household. And therefore I get to make all of the decisions."
    ethan "And if I say you don't retire. You don't."
    briana "It's too late. The deadline to apply for the Olympic trials was weeks ago."
    ethan "And I already signed you up."
    scene 33briana02
    briana "I'm not going."
    briana "Bye."
    scene 34briana02
    ethan "Ungrateful brat."
    scene 35briana02
    reina "That's enough, Ethan."
    reina "We were all getting along fine until you arrived."
    reina "Briana is an adult now. She should be able to make her own decisions."
    ethan "Not while she's living in my house."
    scene 36briana02
    ethan "Did you talk her into this?"
    reina "Ethan no, he had nothing to do with it."
    ethan "An-You know what, don't even answer me."
    scene 37briana02
    ethan "Reina, I thought we had an agreement."
    reina "We did. Briana was the one who brought him here."
    reina "It's obvious he means a lot to her."
    scene 38briana02
    ethan "Because of him, we just lost our golden goose, our golden egg."
    reina "Oh, so now you admit it's because of her that we have this house."
    scene 39briana02
    ethan "Don't start Reina-"
    reina "Don't start? We were all laughing, happy, having a good time until you arrived."
    ethan "You always do this-"
    scene 40briana02
    reina "You're the one making everyone miserable, Ethan! Maybe, for once, be happy."
    ethan "Happy? Happy?"
    reina "Yes. Happy. Everything is paid off. We have a big house with an oceanfront view, just like we said we would when we got married."
    scene 41briana02
    ethan "I don't remember saying that. That was all you."
    reina "Ethan.."
    ethan "Do you really think I wanted to marry you?"
    scene 42briana02
    ethan "I only did it because everyone pressured me to!"
    scene 43briana02
    ethan "{i}'Reina is a good woman' 'Reina would make the perfect wife' 'Reina would be a great mother.'{/i}"
    scene 44briana02
    ethan "All fucking bullshit. Just one headache after another."
    scene 45briana02
    ethan "If I wasn't such a pussy, I would have never married you!"
    scene 46briana02
    ethan "So there is your 'happy'."
    scene 47briana02
    ethan "Now I'm going to my 'happy'. And don't bother calling."
    play sound "sfx/dooropenclose.ogg"
    show 48briana02 with Pause(2)
    stop sound
    scene 49briana02
    jenni "Reina."
    scene 50briana02
    jenni "Reina."
    scene 51briana02
    reina "Just leave me alone!"
    play sound "sfx/dooropenclose.ogg"
    show 52briana02 with Pause (2)
    stop sound
    scene 53briana02
    jenni "Well that turned out exactly like I thought it would."
    main "Does this happen often?"
    scene 54briana02
    jenni "Almost every night he decides to come home. Although, this is the first time he said that to her."
    jenni "He came close to saying it."
    main "Saying what?"
    jenni "That he wants a divorce."
    jenni "It is getting late. I'll drive you home."
    if brianaevent02.status == "completed":
        main "No, I want to see Reina."
        jenni "[player_name]!"
        jump consolereina
    else:
        menu:
            "No, I want to see Reina first.(+5 Reina love)":
                $ReinaC.love_up(5)
                jenni "Wait, [player_name]!!"
                jump consolereina
            "Will Reina be ok?(+ 2 Jenni trust)":
                scene 55briana02
                $JenniC.trust_up(2)
                jenni " She'll be fine. She just needs her alone time."
                menu:
                    "I want to go to visit her.(+ 2 Reina Love)":
                        $ReinaC.love_up(2)
                        jump consolereina
                    "If you say so. (+2 Jenni Trust)":
                        $JenniC.trust_up(2)
                        scene 56briana02
                        jenni "I know so."
                        $brianaevent02.status_completed("not completed")
                        jenni "When Reina gets upset, she goes off into her own little world."
                        jenni "Reina isn't the type to hurt herself."
                        scene 57briana02
                        jenni "She just needs time to process the situation."
                        jenni "I'll take you back home."
                        jump jennidropsmcoff
label consolereina:
    scene 58briana02
    main "Reina."
    scene 59briana02
    main "Reina?"
    reina "Hmmm?"
    scene 60briana02
    reina "Oh, it's you."
    scene 61briana02
    reina "I'm sorry you had to hear that."
    scene 62briana02
    reina "I...I'm not sure what to think or do any more."
    reina "It feels like my entire life is a lie."
    scene 63briana02
    reina "I just want you to know that you were never a burden to us. To me."
    reina "Your mother and I were close friends. She would have done the same for me. I know it."
    main "Thanks, Reina. But I don't think I'm the one with the problems."
    scene 64briana02
    reina "No. No, you're not. It's me."
    scene 65briana02
    reina "What should I do, [player_name]?"
    if brianaevent02.status == "completed":
        main "I don't know."
        main "Maybe divorce?"
        scene 66briana02
        reina "Divorce?"
        main "Divorce. Separate. Couples therapy?"
        scene 67briana02
        reina "I-I-I-"
        main "Just think it over, Reina."
        reina "Thanks, [player_name]."
        stop music
        scene 79briana02 with fade
        jenni "There you are. So, how is she?"
        main "She's coping."
        jenni "Reina needs time to think. And she probably won't like my advice."
        main "Which is?"
        scene 80briana02
        jenni "Divorce. She'll just say 'misery loves company'."
        jenni "But I know a dead marriage when I see one."
        jenni "Let's go. I'll drive you home."
        jump jennidropsmcoff
    else:
        menu:
            "I don't know.":
                main "Maybe therapy?"
                main "Or couples counseling."
                scene 68briana02
                reina "Maybe."
                reina "I didn't expect this at all."
                scene 69briana02
                reina "Thanks for checking in on me, [player_name]."
                scene 72briana02
                reina "You're so dependable."
                jump mckissingreinachoice                              
            "Divorce him.(+ 2 Reina Trust)":
                scene 70briana02
                reina " Divorce?"
                $ReinaC.trust_up(2)
                main " Or Separate."
                main "I don't think you two are in love anymore."
                scene 71briana02
                $choices.append(divorcesuggest)
                reina "...."
                reina "I don't know."
                reina "He's everything to me."
                main "I don't think he sees you the same way."
                scene 72briana02
                reina "Yeah. I'll..think about it."
                jump mckissingreinachoice
label mckissingreinachoice:
    scene 73briana02
    "(Reina feels so warm.)"
    "(And her lips..)"
    menu:
        "Kiss her.":
            scene 74briana02
            "(Her lips are so sweet)."
            scene 75briana02
            "(And soft.)"
            show 76briana02 with Pause (3)
            scene 77briana02
            reina "[player_name]?!?!"            
            "(Fuck.)"
            $choices.append(reinakiss)
            scene 78briana02
            main "I'm sorry, Reina."
            "(Fuck, fuck, fuck, what did I do.)"
            main "Jenni is going to drive me home. Good night, Reina."
            scene 79briana02 with fade
            jenni "There you are."
            "(Just act normal, like nothing happened.)"
            scene 80briana02
            jenni "How is she?"
            main "She's uh-she's fine."
            jenni "Well, let's leave her be. I'll drive you home."
            jump jennidropsmcoff         
        "Pull away":
            "(What am I thinking, it's Reina.)"
            main "It's getting late."
            reina "Yeah, it is."
            reina "Give Jenni my thanks for taking you home."
            reina "I'm sorry you can't stay here, [player_name]."
            main "It's ok."
            scene 79briana02 with fade
            jenni "There you are."
            scene 80briana02
            jenni "How is she?"
            main "She's coping."
            jenni "Well, let's leave her be. I'll drive you home."
            jump jennidropsmcoff
label jennidropsmcoff:
    scene 81briana02
    jenni "I'm sorry you had to witness that tonight."
    $brianaevent02.status_completed("not completed")
    jenni "I'm sure Briana was happy you were there for her."
    jenni "I'll call you sometime tomorrow, ok?"
    jenni "Good night, [player_name]."
    jump epilogue01event


   

