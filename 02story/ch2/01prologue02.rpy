label prologue02:
    scene black
    camilla "Hello????!"
    play sound "sfx/dooropenclose.ogg"
    show screen eyeopening
    scene 01prologue02
    camilla "[player_name]??"
    stop sound
    hide screen eyeopening
    scene 02prologue02
    camilla "Oh my god."
    scene 03prologue02
    camilla "[player_name], are you ok? Say something!"
    main "Ca-ca-camilla?"
    scene 04prologue02
    camilla "Take slow, deep breaths. I'll call an ambulance."
    scene 05prologue02
    camilla "Yes? There's been a break-in, someone is injured. Please send an ambulance."
    scene 06prologue02
    camilla "I'm staying here with you until help arrives."
    play sound "sfx/Ambulance.ogg"
    scene black
    scene 07prologue02 with fade
    stop sound
    police1 "Can you describe to me what happened?"
    camilla "I was watching television when I noticed a dark skinned man walking around the neighborhood. I had never seen them before."
    police1 "And then?"
    camilla "I heard a loud thud outside and came to investigate. By the time I reached the door, he entered a car and drove off."
    scene 08prologue02
    police1 "Can you describe the vehicle? Were you able to see their license plate?"
    camilla "No, I think it was a black Mazda or Nissan. I couldn't see their license plate. I was too focused on the person inside."
    police1 "Is this person a new resident?"
    scene 09prologue02
    camilla "Yes, he is. I met him earlier this week. Where is the ambulance? He could be bleeding internally."
    police1 "The ambulance is on its way, ma'am. Thank you for your cooperation."
    scene black with fade
    show screen eyeopening
    scene 10prologue02 with fade
    "(I'm in the hospital again.)"
    hide screen eyeopening
    play sound "sfx/dooropenclose.ogg"
    scene 11prologue02
    ernurse "Good afternoon, [player_name]."
    ernurse "It's time for your daily checkup."
    main "Daily? How long have I been here?"
    scene 12prologue02
    ernurse "You were admitted here 4 days ago, [player_name]."
    "(Four days.)"
    scene 13prologue02
    ernurse "You suffered from a severe head concussion along with a fractured wrist."
    ernurse "You've made considerable progress physically but you were having memory problems."
    ernurse "Try moving your legs off of the bed."
    scene 14prologue02
    ernurse "Are you able to feel anything when I do this?"
    scene 15prologue02
    main "Ow! Yes."
    scene 16prologue02
    ernurse "Hmmm."
    main "When will I be able to leave?"
    scene 17prologue02
    ernurse "Today, once I have submitted everything to the doctor on shift."
    ernurse "You will need someone to drive you home, though."
    ernurse "Your phone is on the desk next to your bed."
    scene 18prologue02
    "(Who should I call?)"
    menu:
        "Call Jenni. (Jenni Trust + 3)":
            jenni "Hello?"
            main "Jenni? It's me."
            jenni "[player_name]?  How are you?"
            main "I'm feeling better."
            if prologue02.status == "not completed":
                $JenniC.trust_up(3)
                $choices.append(jennicare)
                jenni "Why are you calling me?"
            else:
                jenni "Why are you calling me?"
            main "The nurse-the nurse said I can leave today."
            jenni "Oh, do you want me to come and pick you up?"
            main "Yes, please."
            jenni "I'll be there in a few minutes."
            scene 19prologue02 with fade
            main "You look different, Jenni."
            scene 20prologue02
            jenni "Do you like it?"
            main "It's different."
            scene 21prologue02
            jenni "I thought I would try something new."
            scene 22prologue02
            jenni "It's the first time I've ever cut my hair this short."
            scene 23prologue02
            jenni "But enough about me. Let's talk about you."
            main "Jenni-"
            scene 24prologue02
            jenni "That attack happened as soon as I left."
            scene 25prologue02
            jenni "I should have made sure you were inside the house safely but I wanted to check up on Reina."
            scene 26prologue02
            $prologue02.status_completed("not completed")
            jenni "At least Camilla was there to help you. I think it was a good thing we visited her store before last night."
            scene 27prologue02
            jenni "I'll go grab a wheelchair and your paperwork. Then we'll be on our way."
            scene 28prologue02
            jenni "I'm back. Let's go."
            scene 29prologue02
            jenni "I bet you're so happy to leave this place. It really can be dreadful."
            stop music
            jump jennievent03
        "Call Reina. (Reina Trust + 3)":
            reina "Hello?"
            main "Reina? It's me."
            reina "[player_name]? You're awake?"
            if prologue02.status == "not completed":
                $ReinaC.trust_up(3)
                $choices.append(reinacare)
                reina "I'm on my way to the hospital."
            else:
                reina "I'm on my way to the hospital."
            scene 30prologue02 with fade
            reina "[player_name]."
            scene 31prologue02
            reina "Once again you're in the hospital."
            reina "I've failed you again."
            main "Reina-"
            scene 32prologue02
            reina "I was so self-absorbed that I didn't care about you."
            reina "I should have been the one to drive you home."
            scene 33prologue02
            reina "Some landlord I am. I can't even keep my tenants safe. How will I be able to sell that house for top dollar?"
            scene 34prologue02
            reina "At least the next door neighbor was there to help."
            scene 35prologue02
            reina "That's in the past now."
            scene 36prologue02
            reina "You can be discharged today. I'll make sure you're safe this time."
            scene 37prologue02
            $prologue02.status_completed("not completed")
            reina "I'll be right back."
            scene 38prologue02
            reina "Let's go home, [player_name]."
            scene 39prologue02
            reina "I'll make sure this won't happen again."
            jump reinaevent03


