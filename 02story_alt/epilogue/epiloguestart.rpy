label epiloguestart:
    if photosreleased in choices:
        jump ruinedending
    else:
        jump notruined

label notruined:
    scene 01epilogue with fade
    "Good evening, Sierra Beach, here is the top stories for you this evening."
    if ethanfindsout in choices:
        "Breaking news, City Councilwoman Miyuki Hayashibara has announced that she will no longer be running for Mayor for Sierra Beach."
        "This leads questions about the future of the Sierra Beach Revitalization Project, which Hayashibara personally championed."
    elif camillarunsforoffice in choices:
        "Lifelong Sierra Beach Resident Camilla Turner has announced that she will be running for Mayor."
        "Turner will be facing off against City Councilwoman Miyuki Hayashibara this fall. Their first debate is next week."
    else:
        "Mayoral candidate Miyuki Hayashibara will be hosting another Town Hall meeting this Thursday to discuss the Sierra Beach Revitalization Project."
        "Here, residents can see which neighborhoods will be rezoned if the Project passes on the ballot."
    "In other news."
    if drugdealerarrest in choices:
        "Charges has been filed against John Rodriguez regarding the case of a missing girl that died of an overdose. He is being held without bond."
    else:
        "Authorities are still looking for suspects in regards to the missing girl who washed up dead in the Sierra River Basin."
    "Now for the weather- expect clear, sunny skies for the rest of the week."
    jump afterthenews

label afterthenews:
    "(Another day clean and sober.)"
    "(The start of my new life.)"
    if commitments >=2:
        "(Hmm, maybe Dr. Rose has a point about my relationships.)"
        "(I don't want to let anyone down.)"
        "(What should I do?)"
        menu:
            "(I'll prioritize one over all of the others.)":
                jump pickcommitment
            "(Find a way to make it all work.)":
                jump kingending
    elif commitments == 1:
        "(I have something important to do.)"
        jump pickcommitment
    else:
        jump kingorpeasant


label pickcommitment:
    menu:
        "(Marry Sabrina.)" if sabrinamarriage in choices:
            jump sabrinaending
        "(Vacation with Camilla.)" if camillavacation in choices:
            jump camillaending
        "(Go hiking with Briana.)" if brianarelationship in choices:
            jump brianaending
        "(Help Penny record an album.)" if pennycareer in choices:
            jump pennyending
        "(Move with Aunt Jenni.)" if jennimove in choices:
            jump jenniending
        "(Help Mom.)" if reinarelationship in choices:
            jump reinaending
            
label kingorpeasant:
    "(I don't have any obligations.)"
    "(I don't have to stay here if I don't want to.)"
    menu:
        "Abandon them all.":
            jump badendingstart
        "Stay here and help them out.":
            jump kingending


label endingscreen:
    scene theend with Pause (15)
    return