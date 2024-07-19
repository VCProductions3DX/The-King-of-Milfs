label jennievent03:
    scene 01jenni03 with fade
    jenni "And we're home."
    scene 02jenni03
    jenni "This is even more spacious than I thought."
    scene 03jenni03
    jenni "The kitchen is nice too- what is that back there?"
    scene 04jenni03
    jenni "It's a swimming pool! But there's no water in it. I wonder if Reina knows about it."
    scene 05jenni03
    jenni "It would certainly be nice to take a dip in the pool. I'll call her when I grab my swimsuit."
    scene 06jenni03
    jenni "I have a little bit of shopping to do, would you like to join me?"
    main "No, thanks."
    jenni "Aww, ok. Stay here and rest a bit."
    scene 07jenni03
    jenni "You're going to tell me everything that happened when I get back."
    main "Jenni-"
    scene 08jenni03
    jenni "There's surveillance cameras in the house now- at least that's what Reina said. I'll be back."
    scene ch2freeroam
    "(Fuck, I didn't expect to see him.)"
    "(How does he know where I live? Am I being followed?)"
    "(Fuck.)"
    scene 09jenni03
    jenni "I'm back."
    main "That's a lot of food."
    scene 10jenni03
    jenni "Silly, my purse and swimsuit is in one of them."
    jenni "Reina gave me the OK to fill the pool."
    jenni "Let's go outside, [player_name]. You need the sunshine."
    scene expression "11jenni03" + JenniSwimsuit
    jenni "This pool is deeper than I thought."
    scene expression "12jenni03" + JenniSwimsuit
    jenni "The water's perfect."
    scene expression "13jenni03" + JenniSwimsuit
    "(She seems to be enjoying herself.)"
    scene expression "15jenni03" + JenniSwimsuit
    jenni "So relaxing."
    scene expression "16jenni03" + JenniSwimsuit
    jenni "The pool's a bit too deep for water therapy."
    scene expression "17jenni03" + JenniSwimsuit
    jenni "But it's perfect for a short swim."
    scene expression "18jenni03" + JenniSwimsuit
    jenni "Once you're feeling better, you should really take a dip into the pool."
    scene 19jenni03 with fade
    jenni "That swim made me really hungry. It's time to start dinner."
    scene 20jenni03
    menu:
        "Do you like cooking, Aunt Jenni?":
            jenni "If I didn't, I wouldn't be cooking right now."
            scene 21jenni03
            jenni "After experiencing the best cooking in the world, I decided to learn how to make my own food."
            scene 22jenni03
            jenni "It brings me a sense of joy. Of calm."
            scene 23jenni03
            jenni "Here you go."
        "Are you the homemaker of the family, Aunt Jenni?":
            jenni "Actually, that was your mother."
            jenni "She was the more responsible sister."
            scene 21jenni03
            jenni "But once I got married, I decided to learn how to be a good wife."
            jenni "And I found I liked cooking more than I thought."
            scene 22jenni03
            jenni "Something just clicked. And I haven't stopped cooking ever since."
            scene 23jenni03
            jenni "Here you go."
    scene 24jenni03
    jenni "Let's see what's on television."
    scene 25jenni03
    jenni "Sci-fi. Boring." 
    main "Are you not eating?"
    scene 26jenni03
    jenni "I'm the type to eat when I'm cooking. Don't worry, there's plenty of leftovers."
    scene 27jenni03
    jenni  "So, are you going to tell me what really happened?"
    main "I was attacked after you left, then Camilla rescued me."
    scene 28jenni03
    jenni "You were attacked {i}here{/i}, at night, after I left. "
    jenni "That's not something that happens in a small town like this."
    if jennievent03.status == "completed":
        main "I don't know."
        main "It was too dark for me to see his face."
        scene 31jenni03
        jenni "Well, thankfully Camilla saw the attacker."
        jenni "I'm sure they will catch the culprit soon."
    else:
        menu:
            "Tell Aunt Jenni the entire story.(Jenni Trust + 3)":
                main "I lived with a drug dealer. He offered me a place to stay when Ethan kicked me out."
                main "I helped him with his business. Made a lot of friends."
                $JenniC.trust_up(3)
                main "One day when I came home, I found his girlfriend on the couch, dead."
                scene 29jenni03
                jenni "She overdosed, didn't she?"
                main "Yeah. The drug dealer didn't want her to do drugs, but she did them behind his back."
                main "He blamed me every time she would get wasted."
                scene 30jenni03
                jenni "So he probably blames you for her death?"
                main "No other reason."
                jenni "But how did he find you? You're far away from the city and you just left rehab."
                main "I don't know."
                scene 31jenni03
                jenni "This is worrying."
                jenni "I'll spend the night here, to keep you safe."
            "Lie.":
                main "I don't know. Maybe I was targeted because I live alone."
                scene 29jenni03
                jenni "There are several people on this street who live by themselves."
                jenni "I don't think it was random, [player_name]."
                jenni "I wish you would trust me more, so I can be able to help you."
                jenni "For Reina's sake."
    main "How is Mom?"
    scene 32jenni03
    jenni "She's depressed, as one would be after realizing her entire marriage is a sham."
    scene 33jenni03
    jenni "She's a different woman now."
    main "And what about Dad?"
    jenni "Ethan hasn't come home since the incident. It's better that way."
    main "Briana and Penny?"
    scene 34jenni03
    jenni "They keep to themselves. They grab whatever I'm cooking, then disappear into their rooms."
    jenni "While I was grabbing my swimsuit, I told them to stop by and visit you when they get a chance."
    show screen eyeclosing
    scene 35jenni03
    jenni "Tired?"
    main "Yeah."
    jenni "I'll clean up and let you sleep for a while."
    main "Thanks Jenni."
    hide screen eyeclosing
    scene 36jenni03 with fade
    show screen eyeopening
    "(Fuck, what time is it?)"
    scene 37jenni03
    jenni "You're awake."
    hide screen eyeopening
    jenni "How are you feeling?"
    main "Sore. I have a fucking headache."
    scene 38jenni03
    jenni "Here."
    main "Over the counter medicine?"
    jenni "The doctor didn't write you a prescription, and I always have some handy."
    main "Thanks."
    scene 39jenni03
    jenni "Is the TV bothering you?"
    main "A little bit.."
    jenni "I'll turn the volume down."
    main "Has anyone stopped by or-"
    scene 40jenni03
    jenni "No, it's just me and you."
    jenni "I didn't notice any strange figures or cars outside."
    jenni "You can relax."
    main "Why are you doing this for me?"
    scene 41jenni03
    jenni "Doing what?"
    main "Everything. You take me shopping, then a haircut, then the beach. Now you're babysitting me."
    scene 42jenni03
    jenni "You really don't remember me? I used to take care of you all of the time when you were a baby."
    jenni "I would watch over you while Reina went to work."
    jenni "It's something that comes naturally to me."
    scene 43jenni03
    jenni "Besides, you remind me of myself."
    main "How?"
    scene 44jenni03
    jenni "Lost. Alone. You need someone to watch your back."
    scene 45jenni03
    jenni "And your front."
    scene 46jenni03
    "(Fuck, I'm hard again.)"
    main "Aunt Jenni, I'm sorry-"
    scene 47jenni03
    jenni "Now, now, don't worry. I can take care of it for you."
    jenni "I won't tell anyone. It'll be our little secret."
    "(Shit, she's really going to do it.)"
    "(I hope no one is watching.)"
    menu:
        "Accept (Jenni Love + 5 )": 
            if jennievent03.status == "not completed":
                scene hj01jenni03
                $choices.append(jennihj)
                $JenniC.love_up(5)
                $jennievent03.status_completed("not completed")
                jenni "Now relax and let me handle the rest."
            else:
                scene hj01jenni03
                jenni "Now relax and let me handle the rest."
            scene jennihandjob 
            jenni "How does that feel? It feels good, doesn't it?"
            jenni "Your aunt's hands going up and down your big cock."
            jenni "I remember when it was so small and tiny and soft."
            jenni "Now it's all big and hard."
            menu:
                "Cum on Jenni's hands.": 
                    jenni "Easy does it."
                    jenni "That's a good boy."
                    jenni "You made quite a mess."
                    scene hj02jenni03
                    main "Fuck. I'm sorry, Aunt Jenni."
                    jenni "Why are you sorry?"
                    scene hj03jenni03
                    jenni "We're family. We take care of each other."
                    jenni "No one has to know."
                    main "Thanks."
                    scene 48jenni03 with fade
                    jenni "I think it's time for you to go to bed."
                    main "Aunt Jenni-"
                    jenni "I'll sleep out here. Do you need help getting off of the couch?"
                    main "I can get up on my own."
                    jenni "Good night, [player_name]. Sleep tight."  
                    jump aishaevent01
                "I can't cum.": 
                    scene bj01jenni03
                    jenni "Poor baby."
                    jenni "You need more stimulation."
                    scene jenniblowjob01
                    "(Her mouth feels good.)"
                    "(She knows how to suck cock.)"
                    scene bj02jenni03
                    main "Fuck!"
                    jenni "Naughty boy."
                    $choices.append(jennibj)
                    scene 48jenni03 with fade
                    jenni "I think it's time for you to go to bed."
                    main "Jenni-"
                    jenni "I'll sleep out here. Do you need any help?"
                    main "I can get up on my own."
                    jenni "Good night, [player_name]. Sleep tight."  
                    jump aishaevent01
        "Refuse.": 
            scene 50jenni03
            jenni "You're making things harder for yourself."
            $choices.append(jennirefuse)
            main "No it's fine, I just need to pee."
            scene 51jenni03
            "(That was awkward.)"
            "(My own aunt offered to jack me off.)"
            "(I think I need to keep my distance from her.)"
            jump aishaevent01

