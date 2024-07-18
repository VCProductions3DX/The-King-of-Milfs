label pennyevent05:
    scene 01penny05 with fade
    "(Penny's alive.)"
    main "Hey Penny."
    scene 02penny05
    penny "Hey [player_name]."
    main "How are you feeling?"
    scene 04penny05
    penny "..."
    if photosdestroyed in choices:
        main "I saw those photos and I got rid of them."
        scene 05penny05
        penny "But there's still the digital copies."
        main "I got rid of those as well."
        scene 03penny05
        penny "You-you did?"
        main "Yeah. They were used as blackmail against me."
        main "But I beat the shit out of them and destroyed it."
        scene 06penny05
        penny "[player_name]."
        penny "Are you real?"
        main "That's a weird question to ask."

        penny "I don't think any normal guy would delete those photos."
        main "We're not all scumbugs, Penny."

        penny "Still, thank you."
        main "Is something wrong?"
        jump pennyconfesses
    else:
        scene 03penny05
        penny "What happened to those photos?"
        "(Fuck, I should probably lie.)"
        menu:
            "I got rid of them.":
                scene 06penny05
                penny "Really?"
                main "Yeah. No one will ever see them."
                scene 08penny05
                penny "I hope not."
                penny "Thank you, [player_name]."
                jump pennyconfesses
            "They're stashed away.":
                scene 06penny05
                penny "What?"
                main "No one will ever find them."
                penny "You were supposed to delete them, stupid."
                main "They're in your room, Penny."
                scene 07penny05
                penny "Not funny. What about the person who took those photos?"
                penny "They'll take more, won't they?"
                main "No, they got arrested."
                scene 04penny05
                penny "They'll be back."
                penny "Leave me alone."
                jump freeroamch5
    label pennyconfesses:
        scene 09penny05
        penny "I think I'm ready to perform in front of a live audience."
        main "Oh?"
        scene 10penny05
        penny "Yeah, I'm getting better now."
        penny "Here, listen."
        scene 13penny05
        main "Wow, that is better."
        scene 14penny05
        penny "I want to record a few songs and send them out to label companies."
        penny "But I don't want to do it alone."
        penny "Will you help me?"
        menu:
            "Sure.":
                scene 15penny05
                $commitments +=1
                $choices.append(pennydebut)
                penny "Thank you so much!"
                penny "You're the best."
                jump freeroamch5
            "Maybe later.":
                scene 16penny05
                penny "Ok."
                penny "I'll do it on my own."
                jump freeroamch5
       