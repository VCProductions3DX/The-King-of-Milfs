label pennyevent05:
    scene 01penny05
    main "Hey Penny."
    penny "Hey [player_name]."
    scene 02penny05
    penny "They want to keep me here for a few weeks."
    main "How are you feeling?"
    scene 03penny05
    penny "..."
    if photosdestroyed in choices:
        main "I saw those photos and I got rid of them."
        scene 04penny05
        penny "But there's still the digital copies."
        main "I got rid of those as well."
        scene 05penny05
        penny "You-you did?"
        main "Yeah. They were used as blackmail against me."
        main "But I beat the shit out of them and destroyed it."
        scene 06penny05
        penny "[player_name]."
        penny "Are you real?"
        main "That's a weird question to ask."
        scene 07penny05
        penny "I don't think any normal guy would delete those photos."
        main "We're not all scumbugs, Penny."
        scene 08penny05
        penny "Still, thank you."
        main "Is something wrong?"
        jump pennyconfesses
    else:
        scene 09penny05
        penny "What happened to those photos?"
        "(Fuck, I should probably lie.)"
        menu:
            "I got rid of them.":
                scene 10penny05
                penny "Really?"
                main "Yeah. No one will ever see them."
                scene 11penny05
                penny "I hope not."
                penny "Thank you, [player_name]."
                jump pennyconfesses
            "They're stashed away.":
                scene 12penny05
                penny "What?"
                main "No one will ever find them."
                scene 13penny05
                penny "You were supposed to delete them, stupid."
                main "They're in your room, Penny."
                scene 14penny05
                penny "Not funny. What about the person who took those photos?"
                penny "They'll take more, won't they?"
                main "No, they got arrested."
                scene 15penny05
                penny "They'll be back."
                penny "Leave me alone."
                jump freeroamch5
    label pennyconfesses:
        penny "I think I'm ready to perform in front of a live audience."
        main "Oh?"
        penny "Yeah, I'm getting better now."
        main "Wow, that is better."
        penny "I want to record a few songs and send them out to label companies."
        penny "But I don't want to do it alone."
        penny "Will you help me?"
        menu:
            "Sure.":
                penny "Thank you so much!"
                penny "You're the best."
                jump freeroamch5
            "Maybe later.":
                penny "Ok."
                penny "I'll do it on my own."
                jump freeroamch5
       