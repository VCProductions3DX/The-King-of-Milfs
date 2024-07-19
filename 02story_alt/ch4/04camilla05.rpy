label camillaevent05:
    scene 01camilla05 with fade
    "(I wonder how Camilla is doing.)"
    "(I should visit her.)"
    scene 02camilla05
    main "Camilla?"
    scene 03camilla05
    camilla "[player_name]."
    camilla "What brings you here?"
    main "I wanted to see how you were doing."
    scene 04camilla05
    camilla "You are so sweet."
    camilla "Come inside."
    scene 05camilla05
    "(This place is a mess.)"
    if camillaclosesstore in choices:
        jump camillajourneytalk
    else:
        jump camillapoliticstalk

    label camillajourneytalk:
        scene 06camilla05
        main "Do you need any help cleaning?"
        camilla "Oh, all this? No. This is all going to a storage container."
        scene 07camilla05
        camilla "It's mostly housewares anyway. Pots, pans, curtains, blinds."
        camilla "Stuff I still hold onto."
        scene 08camilla05
        main "Are you selling this house?"
        camilla "Yeah, I am. Well, I did anyway."
        main "To whom?"
        camilla "To Reina."
        scene 09camilla05
        camilla "I wanted to get rid of the house as soon as possible, so why not."
        camilla "I'm sure she'll get more money from that bitch than I will."
        scene 10camilla05
        camilla "I can't believe it."
        camilla "I'm leaving Sierra Beach for good."
        main "Where will you go?"
        scene 11camilla05
        camilla "Alaska first. Then maybe Hawaii. Australia, New Zealand. That's all I've got so far."
        camilla "There's a whole world out there, so a lot of places to go."
        scene 12camilla05
        camilla "But it will be kind of lonely going by myself."
        camilla "I could always use a companion."
        menu:
            "Do I get to go for free?":
                scene 13camilla05
                camilla "Of course, dear."
                scene 14camilla05
                camilla "I'll pay for everything."
                scene 15camilla05
                camilla "I just need a warm body to keep me warm."
                scene 16camilla05
                camilla "What do you say? A whirlwind trip with an older woman?"
                menu:
                    "Count me in.":
                        scene 17camilla05
                        camilla "Now we're talking."
                        scene 18camilla05
                        $choices.append(camillavacation)
                        $commitments +=1
                        camilla "I will be finished in 2 weeks."
                        camilla "That's more than enough time to say goodbye to everyone."
                        main "Thanks, Camilla."
                        scene 19camilla05
                        camilla "I can't wait to have you all to myself."
                        scene 20camilla05
                        camilla "In fact, I want some right now." 
                        main "Now?"
                        scene 21camilla05
                        camilla "Now."
                        jump camillasecondfuck
                    "It's not possible right now.":
                        main "I have a lot going on. Especially with my family."
                        scene 22camilla05
                        camilla "A family man. I admire that."
                        camilla "Well, it doesn't have to right away. We can keep in touch, right?"
                        main "Right."
                        scene 23camilla05
                        camilla "Do you think we can have a little fun now?"
                        camilla "For old times' sake? "
                        menu:
                            "Sure.":
                                jump camillasecondfuck
                            "No thanks.":
                                scene 24camilla05
                                camilla "Aww. Thanks for everything, [player_name]."
                                main "Thanks for looking out for me ,Camilla. I mean it."
                                scene 25camilla05
                                camilla "Goodbye."
                                jump freeroamch4
                    "I'll pass.":
                        scene 26camilla05
                        camilla "I understand."
                        camilla "There's someone else more important in your life, is there?"
                        main "Yeah."
                        scene 27camilla05
                        camilla "Be there for her."
                        camilla "Don't take her granted."
                        main "I won't. Thanks for all of the help, Camilla."
                        scene 28camilla05
                        camilla "Thank you for everything, [player_name]."
                        scene 25camilla05
                        camilla "Goodbye"
                        jump freeroamch4
            "I'm kind of busy.":
                scene 29camilla05
                camilla "Family matters?"
                main "Yeah."
                camilla "I understand."
                camilla "But maybe someday in the future?"
                main "Maybe."
                camilla "Are you free now?"
                menu:
                    "Yeah.":
                        scene 32camilla05
                        camilla "Let's have some fun. Now."
                        jump camillasecondfuck
                    "No.":
                        scene 25camilla05
                        camilla "I understand."
                        camilla "Thank you for everything, [player_name]."
                        main "Thanks, Camilla."
                        camilla "Goodbye."
                        jump freeroamch4  
            "No thanks.":
                scene 35camilla05
                camilla "So that's it."
                camilla "It was fun while it lasted."
                main "Thank you, Camilla for everything."
                camilla "You don't want to have any more fun?"
                menu:
                    "No thanks.":
                        scene 36camilla05
                        camilla "Okay."
                        scene 25camilla05
                        camilla "Goodbye, [player_name]."
                        jump freeroamch4
                    "Sure.":
                        scene 37camilla05
                        camilla "Follow me."
                        jump camillasecondfuck
    label camillapoliticstalk:
        scene 38camilla05
        main "What's all this?"
        camilla "Billboards, posters, and mail-in ads."
        main "Wow, you're well prepared."
        scene 39camilla05
        camilla "I'm competing against her."
        camilla "She won't be an easy opponent."
        if miyukiblackmail in choices:
            main "I have some information that might help you."
            scene 40camilla05
            camilla "What?"
            main "She's a talkative one."
            scene 41camilla05
            camilla "How do you know that?"
            main "She hired me to work for her."
            scene 42camilla05
            camilla "And you did this knowing how I felt?"
            main "Do you want the information or not?"
            scene 43camilla05
            camilla "Of course I do."
            main "The contractor for the project is her boyfriend."
            scene 44camilla05
            camilla "What's so special about her boyfriend?"
            camilla "Other than the fact he's her boyfriend."
            main "Her boyfriend is...Reina's husband, Ethan."
            scene 45camilla05
            camilla "What? That Ethan? I.."
            camilla "Do tell me more."
            scene 46camilla05
            main "She doesn't like his plans, so she also have other contractors competing for the job."
            camilla "Is she fucking them too?"
            main "I guess."
            scene 47camilla05
            camilla "Thank you, [player_name]."
            camilla "I'm going to have her investigated."
            camilla "Would you like a little reward?"
            menu:
                "No thanks.":
                    main "I just thought I would tell you."
                    scene 41camilla05
                    camilla "Aww, you are a sweartheart."
                    camilla "This is where we part ways, [player_name]."
                    camilla "But thank you. This is important to me and Sierra Beach."
                    main "Thanks for helping me, Camilla."
                    camilla "You're welcome."
                    scene 25camilla05
                    camilla "Goodbye."
                    jump freeroamch4
                "Sure.":
                    scene 51camilla05
                    camilla "I'll make it worth your time."
                    camilla "Follow me."
                    jump camillasecondfuck
        else:
            main "I'm sure she has some dirt on her."
            scene 52camilla05
            camilla "Hmmm? Like what?"
            main "Maybe she's taking bribes or a hidden past."
            scene 53camilla05
            camilla "We all have hidden pasts, [player_name]."
            camilla "Yourself included."
            camilla "But she does strike me as the kind to receive bribes."
            camilla "I need to do some investigating."
            scene 54camilla05
            camilla "Thank you for everything, [player_name]."
            main "Thanks, Camilla."
            scene 25camilla05
            camilla "I'll see you around."
            jump freeroamch4
    label camillasecondfuck:
        camilla "Let's get you nice and hard."
        scene camillabj03 with Pause(10)
        "(Camilla gives the best blowjobs.)"
        "(Just her big soft tits make it better.)"

        camilla "Easy now."
        scene camillafuck02
        "(Fuck, I have a front view.)"
        "(Wish I could squeeze them.)"
        
        scene camillafuck04
        camilla "You like my big tits, don't you?"
        #
        scene 51camilla05 with fade
        camilla "Hmmm, that felt so good."
        scene 52camilla05
        camilla "Where were you hiding my whole life?"
        main "In an alley, selling drugs."
        scene 53camilla05
        camilla "The last place to look for a good time."
        main "It was my first."
        scene 54camilla05
        camilla "Look how that turned out for you."
        scene 55camilla05
        camilla "At least you were given a second chance."
        scene 56camilla05
        camilla "There are many who don't get that chance."
        camilla "They're fucked for life."
        scene 57camilla05
        camilla "Don't waste your opportunities, [player_name]."
        main "I won't."
        scene 58camilla05
        camilla "You won't get any more."


        jump freeroamch4