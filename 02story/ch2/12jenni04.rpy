label jennievent04:
    scene 01jenni04 with fade
    jenni "Wakey-wakey, [player_name]."
    main "Jenni? What are you doing here?"
    scene 02jenni04
    jenni "I came to visit you, of course."
    if jennicare in choices:
        scene 04jenni04
        jenni "I'm still responsible for you, even if you are feeling better."
        main "I'm feeling better, I don't need your personal help Jenni."
        if jennihj in choices:
            jenni "Are you still thinking about what happened?"
            jenni "Let's just keep that our little secret."
        else:
            jenni "But I do know what you need, [player_name]."
    else:
        scene 03jenni04
        main "You changed your hair."
        jenni "I did, it's my first time with short hair."
    scene 05jenni04
    jenni "You need sunshine and fresh air! Being in this cottage all of the time isn't good for you."
    main "Are you dragging me to the beach again?"
    scene 07jenni04
    jenni "Not quite."
    scene 09jenni04 with fade
    main "We're at the beach again."
    scene 08jenni04
    jenni "It's a park."
    jenni "The breeze feels so nice."
    scene 10jenni04
    main "Is that why we're here?"
    jenni "No. I needed to get out of the house myself."
    scene 11jenni04
    main "What are you thinking about?"
    jenni "My life."
    scene 12jenni04
    jenni "Up until now, I've always had someone to take care of me."
    jenni "Someone to look after me."
    scene 13jenni04
    jenni "But now I'm on my own."
    "No husband, no agency, nothing."
    main "You have your sister."
    scene 14jenni04
    jenni "Yes, but she has a family and her own life."
    jenni "I can't leech off of her forever."
    jenni "I will have to move out on my own."
    scene 15jenni04
    "(She looks depressed.)"
    scene 26jenni04
    jenni "I'm going to dip my toes into the water. Hold my phone for me."
    scene 28jenni04
    "(Wow Jenni's popular.)"
    scene 29jenni04
    if jennievent04.status == "completed":
        scene 30jenni04
        "(Woah.)"
        scene jselfieedited
        "(I thought Jenni was an actual model. Not this type of model.)"
    else:
        menu:
            "Click the gallery.":
                scene 30jenni04
                "(Woah.)"
                scene jselfieedited
                "(I thought Jenni was an actual model. Not this type of model.)"
            "Don't click the gallery.(Jenni Trust + 2)":
                $JenniC.trust_up(2)
                "(I won't go through her phone.)"
    scene 31jenni04
    jenni "Are you going through my phone?"
    main "No- but you seem to be pretty lonely."
    scene 34jenni04
    jenni "I'm lonely but I'm not {i}that{/i} lonely."
    main "1000 unread messages sound like loneliness to me."
    scene 35jenni04
    jenni "Ok, you got me."
    jenni "You won't tell Reina, will you?"
    scene 36jenni04
    $jennievent04.status_completed("not completed")
    jenni "I didn't get a huge alimony from my divorce."
    jenni "If I did, I wouldn't have moved back home."
    scene 37jenni04
    jenni "So I have earn a bit of money. I'm not under any contract that prohibits me from doing it, so I am."
    main "Why hide it?"
    jenni "Reina will kick me out if she found out that I'm selling myself on the internet."
    main "Are you actually doing porn?"
    scene 38jenni04
    jenni "No!"
    jenni "Most of those messages are fans asking for more content. "
    jenni "They want personalized photos and videos of me saying their name and talking dirty to them."
    main "That sounds like a lot of work."
    scene 39jenni04
    jenni "It is. Others just want me to have sex on camera."
    jenni "But that's a line I don't want to cross."
    main "Why not?"
    scene 40jenni04
    jenni "First I have to find someone I can trust, and then I have to buy a bunch of equipment."
    jenni "And I can't do it in Reina's home. Not with the girls around."
    menu: 
        "Offer to help.":
            main "You can use the cottage if you want."
            scene 41jenni04
            jenni "No! That's even worse!"
            if jennihj in choices:
                main "You've done it before."
                scene 42jenni04
                jenni "That was at night, no one was watching."
                jenni "Are you trying to blackmail me?"
                menu:
                    "No, I genuinely want to help.":
                        scene 43jenni04
                        $JenniC.love_up(2)
                        jenni "I will think about it."
                        jenni "I just need a place of my own."
                        jump townhallmeetingdiscovery
                    "It's your secret.":
                        scene 44jenni04
                        $JenniC.trust_up(2)
                        jenni "Fuck."
                        jenni "Ok, ok, you can help, just-I need a place, ok?"
                        jump townhallmeetingdiscovery
        "Good luck with that.":
            scene 45jenni04
            jenni "Some consolation you offer."
            jenni "But it isn't your concern, after all."
            jump townhallmeetingdiscovery
label townhallmeetingdiscovery:
    scene 46jenni04
    jenni "It's time to go back home."
    scene 47jenni04 with fade
    jenni "Hmm, what's this?"
    jenni "Oh dear."
    main "What is it?"
    scene 48jenni04
    jenni "It's a town hall meeting. It's for a new development project."
    jenni "I don't think Reina's going to like this."
    main "Why?"
    scene 49jenni04
    jenni "They want to rezone this street from residential to commercial."
    main "Is that a problem?"
    scene 50jenni04
    jenni "Yeah. They're going to demolish all of the houses on this street."
    jump epilogue02event

