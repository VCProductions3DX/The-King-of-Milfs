label jennievent01:
    play sound "sfx/HornHonk.ogg"
    scene black
    jenni "[player_name]!"
    stop sound
    scene 01jenni01
    jenni "There you are! Come on! The boutique won't be open all day!"
    scene 02jenni01
    jenni "So this is the cottage Reina made such a fuss about. Small and quaint."
    jenni "Mmmm..maybe I'll buy it myself. Start a couples' vacation rental service. What do you think?"
    scene 03jenni01
    main "I..."
    jenni "Then I would actually have to meet and talk to people. It'll be like my former marriage."
    menu:
        "What was your marriage like? (+2 Jenni Trust)":
            jenni "Parties, Award Shows, More Parties."
            $JennicaC.trust_up(2)
            jenni "Sometimes we would be there for hours. Other times, less than 5 minutes."
            jenni "There were always the same. You enter, say hi to everyone worth saying hi to, get a drink and leave."
            jenni "You couldn't even enjoy the music or food because it was so loud and crowded."
            jenni "And I always had to be at my husband's side- I couldn't go anywhere on my own."
            jenni "So I had to stand there and smile at people I absolutely loathed."
        "Say Nothing":
            jenni "And I don't want to repeat that experience."
            jenni "Still, Reina wants me to move out within a year so she can sell the cottage."
    scene 04jenni01
    jenni "Here we are, Pandora's Boutique."
    scene 05jenni01 with fade
    play music "music/PandorasBoutique.ogg"
    camilla "Hey Jenni, welcome back!"
    if camillaevent01.status == "completed":
        scene 06jenni01
        camilla "Back again for more work?"
        main "No, I'm with her."
        jenni "Wow, just out of rehab and you have a job already. I'm proud of you, [player_name]."
        scene 07jenni01
        camilla "He is good worker, although he is still a bit rough around the edges, looks wise."
        camilla "He gave {i}her{/i} a scare when she entered my store the other day."
        jenni "Who?"
        scene 08jenni01
        camilla "You know who."
        jenni "Oh. Her. Peddling her revitalization plan again?"
        scene 09jenni01
        camilla "She is persistent, but I'm confident it won't get approved by the town council."
        jump swimsuitselection
    else:
        scene 06jenni01
        camilla "Hello again, [player_name]."
        camilla "How are you today?"
        main "Fine."
        scene 10jenni01
        jenni "You two know each other?"
        camilla "He is my next door neighbor, Jenni. Of course I had to introduce myself to him."
        scene 11jenni01
        camilla "By the way, [player_name],my job offer still stands."
        main "Job offer?"
        camilla "I could always use some help and extra muscle around here."
        camilla "Although you could use a haircut."
        scene 12jenni01
        jenni "Are you trying to hoard [player_name] all to yourself?"
        camilla "Maybe."
        jump swimsuitselection
label swimsuitselection:
    scene 13jenni01
    camilla "So Jenni, what are you looking for today?"
    jenni "A swimsuit."
    camilla "What are you looking for? Bikini? One-piece? Vintage?"
    jenni "Oh I- they all sound good, Camilla. Pick a few out for me."
    scene 14jenni01
    camilla "Here, I think these two would fit you well, Jenni."
    scene 15jenni01
    camilla "But I think he should be the final judge."
    main "Me?"
    scene 16jenni01
    camilla "I have to restock other areas of the store."
    camilla "Besides, that's the reason why she brought you here."
    camilla "I'll see you later."
    scene 17jenni01
    jenni "This won't take long. Afterwards, we'll get something to eat."
    scene 18jenni01 with fade
    jenni "What do you think? Do I still have it?"
    main "This feels awkward."
    scene 19jenni01
    jenni "It's just a bikini.  I'm used to men to oogling at me. In fact, that's how I made my money. "
    jenni "Now, whatever inhibitions you have, let go of it. Do I look good in it or not?"
    menu:
        "You do.(+Bikini Choice)":
            scene 20jenni01
            $JenniSwimsuit = "bikini"
            jenni "Ok, so the bikini."
            jenni "Always a classic."
        "Try something else.":
            scene 21jenni01
            jenni "Do I not look good in it?"
            jenni "What should I try?"
            main " A-A-A one piece."
            jenni "A one-piece. Ok, I'll try it."
            scene 22jenni01 with fade
            jenni "Well, what do you think?"
            scene 23jenni01
            jenni "Which one is it?"
            menu:
                "I prefer the bikini (+Bikini Choice)":
                    scene 24jenni01
                    $JenniSwimsuit = "bikini"
                    jenni "So indecisive."
                    jenni "The bikini it is."
                "I like that swimsuit better (+One Piece Choice)":
                    scene 25jenni01
                    $JenniSwimsuit = "onepiece"
                    jenni "A one-piece it is."
    scene 26jenni01
    jenni "Well that's everything."
    camilla "So, which one did you pick?"
    jenni "The [JenniSwimsuit]."
    camilla "Good choice."
    camilla "Your total is 35.82."
    scene 27jenni01
    camilla "Come by next week, Jenni. We're having a sale."
    jenni "You are?"
    camilla "A clearance sale. You might find something you like."
    jenni "Oh I certainly will."
    scene 28jenni01
    camilla "You stop by as well."
    camilla "Don't keep me waiting."
    jenni "Bye Camilla."
    camilla "Bye, Jenni."
    stop music
    scene 29jenni01 with fade
    jenni "Now it's your turn."
    main "What?"
    if camillaevent01.status == "completed":
        jenni "Camilla is right-you {i}do{/i} look a little rough around the edges."
        jenni "We can't have you scaring the local politicians, can we?"
        jenni "Time to treat you to a haircut."
    else:
        jenni "Camilla is right- you're in dire need of a haircut."
    jenni  "There's a salon nearby. "
    scene 30jenni01
    hairdresser "Jenni! Your appointment isn't today. Why are you here? "
    jenni "Oh, it's not me today. I brought him here."
    hairdresser " Oh my, so much hair."
    jenni "If you can clean him up a bit and make him more professional looking."
    hairdresser "Sit in the chair,please."
    scene 31jenni01
    hairdresser "Hmmm..."
    scene 32jenni01 with flash
    hairdresser "Ta-da!"
    scene 33jenni01
    jenni "That looks so much better."
    scene 34jenni01
    jenni " You are a miracle worker."
    hairdresser "Thank you."
    hairdresser "I'll see you next week. I have a new hairstyle planned for you."
    jenni "I can't wait."
    scene 35jenni01
    jenni" Up for a snack?"
    main "Yeah, I'm a bit hungry."
    jenni "There's a bakery over here. It has the most delicious tarts. I'm salivating just thinking of them. "
    scene 36jenni01
    cashier" Hello, welcome to Sweet Treats and Eats! How may I help you?"
    jenni "Hmmm...What should we have today?"
    scene 37jenni01
    jenni "You decide: either the Lemon Bar, the Apple Pie, or the Strawberry Cobbler."
    scene 38jenni01
    menu:
        "Lemon Bar":
            $JenniBakery = "lemonbar"
            jenni "Good choice."
            jenni "The Lemon Bar, please."
            cashier "Two?"
            jenni "Yes."
            cashier "Here you go. Have a nice day."
        "Apple Pie":
            $JenniBakery = "applepie"
            jenni "My favorite!"
            jenni "Two slices of Apple Pie, please."
            cashier "Coming right up."
            cashier "Here you go, have a nice day."
        "Strawberry Cobbler":
            $JenniBakery = "strawberrytart"
            jenni "Hmm..Strawberry."
            jenni "That's new."
            jenni "Two piece of  Strawberry Cobbler, please."
            cashier "Coming right up."
            cashier "Here you go, have a nice day."
    scene expression "39jenni01" + JenniBakery
    jenni "Mm, this is good."
    scene 40jenni01
    jenni " Have you talked to either Briana or Penny yet?"
    if jennievent01.status=="completed":
        main "Yeah, I have."
        scene 41jenni01
        jenni "How are they?"
        main "Penny is mostly at the skatepark."
        main "She was angry at me at first, but she invited me to go skating with her."
        main "Briana has changed at a lot since I left home."
        main "She's calmer and more easygoing. She used to be the angry one."
        main "She also seems to be a bit nervous, like she's hiding a big secret."
        jenni "Hmm, I wonder what that may be."
    else:
        menu:
            "I've talked to both of them.(Jenni Trust + 2)" if brianaevent01.status=="completed" and pennyevent01.status=="completed":
                scene 42jenni01
                jenni "How are they?"
                main "Penny is mostly at the skatepark."
                $JenniC.trust_up(2)
                main "She was angry at me at first, but she invited me to go skating with her."
                main "Briana has changed at a lot since I left home."
                main "She's calmer and more easygoing. She used to be the angry one."
                main "She also seems to be a bit nervous, like she's hiding a big secret."
                jenni "Hmm, I wonder what that may be."
            "I've talked to just Penny.(Jenni Trust + 1)"if pennyevent01.status == "completed":
                main " Yeah, I've talked to Penny."
                scene 42jenni01
                jenni " How is she? For Reina's sake?"
                $JenniC.trust_up(1)
                main " She's fine. She's mostly at the skatepark, like you said."
                main " She's really into the skating thing."
                jenni " Anything else? Does she have a boyfriend or girlfriend?"
                main " Not that I know of."
                jenni " That's a relief. I'll tell Reina."
                jenni "Still, you should visit Briana. She is excited to see you."
            "I've talked to just Briana.(Jenni Trust + 1)"if brianaevent01.status== "completed":
                main " I met Briana."
                main " She's changed a lot since I left home."
                scene 42jenni01
                jenni " How so?"
                $JenniC.trust_up(1)
                main " She's calmer. More easygoing. Before she used to be so angry all of the time."
                main " Boxing really changed her."
                jenni " Reina used to tell me that Briana would get into a lot of trouble in school."
                main " She punched anyone who made fun of her. Including me."
                main " Though..she did appear a bit nervous. Like she's hiding something."
                jenni " I wonder what. I wonder if being a pro boxer has affected her mentally."
                jenni "Still, you should visit Penny sometime."
                jenni "She would love to see you."
            "I haven't talked to either one of them.":
                main " No, not yet. I haven't talked to anyone yet."
                scene 42jenni01
                jenni " You should. They really want to see you."
                jenni "Especially Briana, she has been dying to see you."
    scene 43jenni01
    jenni "Do you think about it?"
    main "Think about what?"
    jenni "You know what."
    scene 44jenni01
    jenni "Don't go back. Don't go looking for it."
    jenni "If you care about Reina...don't."
    main "I'm not."
    scene 45jenni01
    jenni "You want to hear something?"
    jenni "When you were in the hospital, Reina called me. She was in tears, saying that she 'let Anna down'."
    scene 46jenni01
    jenni "Reina's never called me for anything."
    jenni "It gave me a different perspective on my life."
    scene 47jenni01
    jenni "Before I just wanted to life free and have fun."
    jenni "Now I want to know what it's like to take care of someone."
    main "Like a baby?"
    jenni "Yeah."
    scene 48jenni01
    jenni "What about you? Has that thought ever crossed your mind?"
    menu:
        "Yeah, I do.":
            main "I just haven't found the right person."
            jenni "I'm sure one day you will."
            scene 49jenni01
            jenni "Look at me, talking to a young person about starting a family."
            jenni "My biological clock must be ticking."
            jenni "Except it's broken."
            jenni "It's not impossible for me to have kids, just a very, very low chance."
            jenni "I suppose if I don't have any kids within the next year,I'll just adopt like Reina did."
        "Not really.":
            scene 49jenni01
            jenni "You're still young."
            jenni "And a man. You don't have a biological clock like we do."
    scene 50jenni01
    jenni "That was delicious."
    jenni "We still have the whole afternoon together."
    jenni "Let's go to the beach, shall we?"
    jenni "I'll go change into my swimsuit."
    scene 51jenni01
    jenni "Let's go!"
    jump jennievent02





