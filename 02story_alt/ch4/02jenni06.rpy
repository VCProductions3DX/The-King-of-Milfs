label jennievent06:
    scene 01jenni06 with fade
    jenni "Hello?"
    if jennievent05.status=="completed":
        jenni "(He's asleep on the couch.)"
        scene 02jenni06
        jenni "(What are his clothes doing on the floor?)"
        jenni "(Did they?)"
        scene 03jenni06
        jenni "(No, no Reina isn't the kind of woman to have sex with her own son.)"
        jenni "(She's not that dirty.)"
        scene 04jenni06
        jenni "(Just the thought of it disgusts me.)"
        scene 05jenni06
        jenni "(That's just not who she is.)"
        scene 06jenni06
        jenni "(Besides, he's mine, not hers.)"
        jump mcwakesuponcouch
    else:
        scene 03jenni06
        jenni "I'll go grab my bag."
        scene 06jenni06
        jenni "(What happened last night?)"
        jump mcwakesuponcouch
label mcwakesuponcouch:
    scene 07jenni06
    main "Aunt Jenni? What are you doing here?"
    jenni "Good morning [player_name]."
    scene 08jenni06
    jenni "I left this bag underneath the bed."
    jenni "I came by to pick it up - and check on Reina."
    scene 09jenni06
    jenni "Speaking of which, how did things go last night?"
    main "Better than expected. He didn't argue with her- he took the documents and left."
    jenni "That's good to hear. So it's just the waiting game."
    scene 10jenni06
    jenni "Would you like to go home? Or to my apartment?"
    main "I want to go home."
    main "Mom offered me your room."
    scene 11jenni06
    jenni "Did she?"
    main "She said it would be easier to keep an eye on me."
    scene 12jenni06
    jenni "That is true."
    jenni "I'll take you home and you can grab your things."
    scene 14jenni06 with fade
    jenni "It's a shame that it's in the main revitalization district."
    jenni "I wonder what Reina will do with it."
    scene 15jenni06
    main "What are you doing?"
    jenni "Checking for drugs."
    scene 16jenni06
    jenni "Someone has to keep an eye on you."
    main "I'm clean, I haven't done anything."
    scene 17jenni06
    jenni "That's what people who try to hide things say."
    scene 18jenni06
    jenni "I know I can be a bit annoying, but I am your aunt,  [player_name]."
    scene 19jenni06
    jenni "I don't want you to become addicted again and worry your mother."
    scene 20jenni06
    jenni "When I lived in L.A., it was commonplace to see everyone taking pills."
    jenni "There were overdose incidents every week. This shit breaks up families and friends."
    scene 21jenni06
    jenni "I don't want my sister to suffer any more."
    main "I won't go back."
    scene 22jenni06
    jenni "You know you can always stay with me if you don't like it at home."
    jenni "My apartment isn't as nice, but it will be the two of us."
    jenni "And we can have a lot more fun together."
    scene 23jenni06
    "(So that's what this is about.)"
    scene 24jenni06
    jenni "Are you finished?"
    main "Yeah, that's everything."
    scene 25jenni06
    jenni "Do you mind taking more pictures for me? Business has gotten a little slow."
    main "A little?"
    scene 26jenni06
    jenni "Well a lot slower than I thought. I'm afraid my modelling days are numbered."
    jenni "Competition is increasing and I just can't keep up anymore."
    scene 27jenni06
    jenni "I guess I'll have to stop relying on my looks."
    jenni "It's depressing to think about."
    scene 28jenni06
    jenni "Here, take my phone."
    scene 29jenni06
    "(Wow she wasn't kidding, there aren't as many notifications.)"
    scene 30jenni06
    jenni "(I wonder if he still finds me attractive.)"
    scene 31jenni06
    jenni "(He's lost so much weight now.)"
    scene 32jenni06
    jenni "I could use a good fuck.)"
    scene 38jenni06
    jenni "So, how did the photos come out?"
    main "Here-"
    jenni "Hmm..do you think they're good enough?"
    jenni "From a man's point of view?"
    main "They look good."
    scene 39jenni06
    jenni "Are you sure?"
    jenni "Take a few more."
    scene 33jenni06
    "(She's showing everything off.)"
    scene 34jenni06
    "(I don't think she's uploading these photos.)"
    jenni "Make sure you get my best parts."
    scene 39jenni06
    jenni "What about now?"
    scene 40jenni06
    jenni "Hard enough yet?"
    scene 41jenni06
    main "Is this what you wanted?"
    scene 42jenni06
    jenni "I just wanted to have a little fun."
    scene 43jenni06
    jenni "But you decide."
    if reinashowerfuck in choices:
        "(I just fucked Mom,now Aunt Jenni wants me too.)"
        "(The thought of fucking them both makes me hard.)"
        menu:
            "Ask for a blowjob.":
                jump jenniblowjob2
            "Ask for a titjob.":
                jump jennititjob
            "Fuck her as well.":
                jump jennisecondfuck
    else:
        "(I could use some fun after last night.)"
        menu:
            "Ask for a blowjob.":
                jump jenniblowjob2
            "Ask for a titjob.":
                jump jennititjob
            "Fuck her.":
                jump jennisecondfuck
label jenniblowjob2:
    scene jenniblowjob03
    show text "What a nice, long, thick cock." at thoughtsright with Pause(10)
    show text "Reina would be so jealous if she knew." at thoughtsright with Pause(10)
    show text "I hope you like your aunt sucking your cock as much as I do." at thoughtsright with Pause(15)
    scene jenniblowjob05
    show text "Do you like it that much?" at thoughtsbottomright with Pause(15)
    show text "Your cock is so hard inside of my mouth." at thoughtsbottomright with Pause(15)
    show text "I hope you'll fuck my pussy too." at thoughtsbottomright with Pause(15)
    menu:
        "Fuck her.":
            jump jennisecondfuck
        "Face fuck her.":
            jump jennifacial
label jennititjob:
    scene jennititjob
    show text "Do you like how my big tits feel?" at thoughtsleft with Pause(15)
    show text "All nice and warm and soft." at thoughtsleft with Pause(15)
    menu:
        "Fuck her.":
            jump jennisecondfuck
        "Face fuck her.":
            jump jenniblowjob2
        "Cum on her tits.":
            jump jennipearl
label jennisecondfuck:
    scene 44jenni06
    jenni "I knew you wanted to fuck me."
    jenni "You naughty boy."
    scene jennifuck01
    show text "Don't be slow, dear." at thoughtsbottomleft with Pause(5)
    show text "Go faster, I want to really feel you inside of me." at thoughtsbottomleft with Pause(5)
    show text  "Don't be afraid to get rough with me." at thoughtsbottomleft with Pause(5)
    scene jennifuck02
    show text "Ah, that's it. So much better now." at thoughtsleft with Pause(8)
    show text "Fuck me." at thoughtsleft with Pause(8)
    show text "This is exactly what I needed!" at thoughtsleft with Pause(20)
    menu:
        "Creampie her.":
            jump jennicreampie
        "Pull out.":
            jump jennimess

label jennifacial:
    scene jenniblowjob04
    show text "Oh you like it rough!" at thoughtsright with Pause(15)
    show text "You really like fucking your aunt's face, don't you?" at thoughtsright with Pause(15)
    show text "Are you going to cum in my mouth? Are you?" at thoughtsright with Pause(15)
    scene jenniblowjob06
    show text "Flood my mouth with your cum, baby." at thoughtsright with Pause(5)
    scene 48jenni06
    show text "I can't hold it any longer." at thoughtsright with Pause(3)
    scene 47jenni06
    jenni "Mmmm.."
    "(Fuck I'm tired.)"
    jump backtomansion
label jennipearl:
    scene 49jenni06
    jenni "Aww, you made a mess on my tits."
    jenni "Naughty boy."
    "(Fuck I'm tired.)"
    jump backtomansion
label jennicreampie:
    scene 45jenni06
    if jennifuck in choices:
        jenni "You naughty boy."
        $choices.append(jennipregnancy)
        jenni "Cumming inside of me again."
        "(Fuck I'm tired.)"
        jump backtomansion
    else:
        jenni "(He came inside of me!)"
        $choices.append(jennipregnancy)
        jenni "(It's just one time.)" 
        "(Fuck I'm tired.)"
        jump backtomansion
label jennimess:
    scene 46jenni06
    jenni "What a mess!"
    scene 50jenni06
    jenni "This is a lot of cum."
    scene 49jenni06
    jenni "Would you like to see me clean it?"
    scene 47jenni06
    jenni "Mmmm.."
    "(Fuck I'm tired.)"
    jump backtomansion
label backtomansion:
    scene 51jenni06 with fade
    "(That was exhausting.)"
    scene 52jenni06
    jenni "Did you have a nice nap, sleeping beauty?"
    main "What time is it?"
    $jennievent06.status_completed("not completed")
    scene 53jenni06
    jenni "It's after 12."
    jenni "Do you want to stay here for a while?"
    main "No."
    scene 54jenni06
    jenni "Why not?"
    main "There are other things I need to do."
    scene 55jenni06
    jenni "Aww, you really are a caring person."
    scene 56jenni06
    jenni "Ok, let's go back."
    jenni "But call me later or tomorrow. I want to have more fun."
    scene 57jenni06
    "(All she thinks about is herself.)"
    jump freeroamch4