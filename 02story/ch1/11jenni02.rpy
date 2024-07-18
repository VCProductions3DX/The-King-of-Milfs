label jennievent02:
    scene 02jenni02 with fade
    jenni "Everyone is at school or work, so the beach will be all ours today."
    scene 03jenni02
    jenni "This is my kind of beach."
    jenni "Time to take this off."
    scene expression "04jenni02" + JenniSwimsuit
    "(Wow, Jenni looks amazing.)"
    jenni "It's such a nice, sunny day!"
    scene expression "05jenni02" + JenniSwimsuit
    jenni "I'm going to get my feet wet."
    scene expression "06jenni02" + JenniSwimsuit
    jenni "[player_name],come dip your toes in the water- it's not too cold!"
    scene expression "07jenni02" + JenniSwimsuit
    jenni "Tricked you! But it still feels good, doesn't it!"
    scene expression "08jenni02" + JenniSwimsuit
    jenni "Ekk! You're getting my hair wet!"
    scene expression "09jenni02" + JenniSwimsuit
    jenni "Ok, ok, that's enough."
    scene expression "11jenni02" + JenniSwimsuit
    jenni "So, how are you adjusting to the sober life?"
    main " Ok, I guess."
    scene expression "10jenni02" + JenniSwimsuit
    jenni "What do you think of Sierra Beach?"
    jenni "It's a little too quiet for me, personally."
    main "Same."
    scene expression "12jenni02" + JenniSwimsuit
    jenni "Have you talked to any of your old friends?"
    jenni "Before you left?"
    "(She's asking too many questions. This is irriating.)"
    main "No."
    scene expression "14jenni02" + JenniSwimsuit
    jenni "One last question."
    scene expression "15jenni02" + JenniSwimsuit
    jenni "Did you at least have a girlfriend?"
    main "No, Jenni. No more questions, please."
    $jennievent02.status_completed("not completed")
    scene expression "16jenni02" + JenniSwimsuit
    jenni "I'll stop the interrogations, then."
    jenni "But I want you to do something for me."
    main "What is it?"
    jenni "Take a few pictures of me before the crowd arrives."
    jenni "Sure."
    scene expression "jennimontage1" + JenniSwimsuit with Pause (3)
    scene expression "jennimontage2" + JenniSwimsuit with Pause (3)
    scene expression "jennimontage3" + JenniSwimsuit with Pause (3)
    scene expression "jennimontage4" + JenniSwimsuit with Pause (3)
    scene expression "jennimontage5" + JenniSwimsuit with Pause (3)
    scene expression "17jenni02" + JenniSwimsuit
    jenni "Let me see."
    jenni " Oh nice. Maybe photography is in your future."
    scene expression "18jenni02" + JenniSwimsuit
    jenni "[player_name]."
    main "Yes?"
    jenni "Do you mind taking a picture of my backside? Upclose?"
    main "What??"
    jenni "There's something that is bothering me in these photos."
    main "But why do you need me to take a picture?"
    jenni "It's important. Just one picture. I need to be sure of it."
    main "I.."
    jenni "And make sure you zoom in."
    scene expression "19jenni02" + JenniSwimsuit
    jenni "We don't have all day. Take it."
    scene expression "20jenni02" + JenniSwimsuit
    jenni "See? Was that so hard?"
    scene expression "21jenni02" + JenniSwimsuit
    jenni "Oh..my god.."
    main "What is it?"
    jenni "I can't believe I gained that much weight."
    jenni "Looks like I'll have to cut back on the sweets again."
    menu:
        "You look great to me,Jenni.(+ 2 Jenni Love)":
            scene expression "22jenni02" + JenniSwimsuit
            jenni " Oh you!"
            $JenniC.love_up(2)
            jenni " This is serious."
            jenni " I can't wear something like this if my thighs look like that!"
        "Same.(+2 Jenni Trust)":
            scene expression "23jenni02" + JenniSwimsuit
            jenni " Hahaha!"
            $JenniC.trust_up(2)
            jenni " But you have a good reason- you were in rehab."
            jenni " Weight gain is normal."
            jenni " This is not."
    scene expression "24jenni02" + JenniSwimsuit
    jenni " Well, no one will get see these pictures."
    scene expression "25jenni02" + JenniSwimsuit
    jenni "Just one selfie will do."
    scene expression "26jenni02" + JenniSwimsuit
    jenni " I'm heading back home. I'll talk to you later, ok?"
    jenni " Take care, [player_name]."
    stop music
    jump brianaevent02








