label pennyevent01:
    scene black
    penny"Who is it?"
    main "It's me, [player_name]."
    penny"Come in."
    scene 01penny01
    main "That's an interesting collection."
    penny"Yeah."
    scene 03penny01
    penny"Today I'm feeling like Drop Dead Eden."
    main "When did you start skateboarding?"
    scene 02penny01
    main "Penny? Penny?"
    scene 05penny01
    penny"Why did you leave us, [player_name]?"
    penny"You just left one day and never came back!"
    main "I'm sorry, Dad kicked me out. I had no choice."
    scene 07penny01
    penny"But you could have called! Texted! Sent me an email or  a message online!"
    scene 08penny01
    penny"But you didn't do any of that!"
    scene 12penny01
    penny "You just disappeared! Sis and I, we thought-we thought you hated us. That we annoyed you."
    main "Penny, I'm sorry. I had my own issues and problems."
    main "I'll try to make up for it."
    scene 11penny01
    penny"Two years ago. A couple of friends and I were in the city and I saw some skaters. I watched and memorize everything they did."
    penny "So, on my birthday, I asked Mom and Dad for money to buy a skateboard. And that's how I started."
    scene 06penny01
    penny"It beats staying here all day."
    main "It can't be that bad."
    scene 09penny01
    penny"You're not here."
    scene 10penny01
    penny"Mom's on the phone all of the time, coming and going. Dad's never here. Sis is never here. It's just one big empty house. We barely see each other. It's like living with a bunch of strangers."
    main "What about Aunt Jenni?"
    penny"She stays in her room all day watching tv."
    scene 13penny01
    penny"I wish it was like the old days. When we lived in Van Corina."
    penny"We weren't rich, but at least we were happy. And we had lots of fun."
    menu:
        "What did you like the most?":
            penny "Mom taking us to the beach. Playing  games, winning prizes and eating ice cream."
            penny "Now she just sells houses on the beach."
        "What kind of fun?":
            penny"Like going to beach...and when we went camping."
            penny"I miss those times."
    scene 14penny01
    penny "All done."
    penny "Want to see me in action?"
    main  "Sure."
    scene 15penny01
    penny "It's too late to go to the skate park today, but I'm going tomorrow. I'm still learning kickflips, but I can show you a thing or two."
    penny"When I first started, I was tripping over myself all of the time. I used to come home every day with so many bruises, mom would get so mad at me. But then I just got the hang of it."
    scene 16penny01
    penny"It takes my mind off of everything. I get to be who I really am."
    main "And the music?"
    penny"That just comes with the scene. Several guys set up a small DJing booth and play anything. And there's a record store nearby that still sells vinyl records. We should go sometime."
    scene 17penny01
    penny"So are you here to stay?"
    main "Yeah, I'm here."
    penny"No more drugs?"
    main "No more, I'm clean."
    scene 18penny01
    penny"I did some vaping once. But then there were those incidents where people were dying."
    penny"So I stopped before dad found out."
    scene 19penny01
    penny"What did you do?"
    main "Anything. Everything. Whatever I could get my hands on just to feel good."
    penny"Did it? Did it feel good?"
    main "In the beginning. Then it just felt like shit."
    scene 21penny01
    penny "What made you want to come home?"
    main "I saw an ad with Mom's picture on it. Realized it was seven years since I saw her."
    penny "And the rest of us? Did you want to see us too?"
    main "Of course. That's why I'm here."
    scene 20penny01
    $choices.append(pennymeet)
    $pennyevent01.status_completed("not completed")
    penny"Thanks for coming by, [player_name]. I appreciate it."
    main "You're welcome."
    penny"So the skating park?"
    main "I'll stop by sometime."
    jump afterpennyvisit






