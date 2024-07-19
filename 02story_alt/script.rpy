#Main Characters
define main = Character ("[player_name]", color="#fff")
define narrator = Character(color="#fff")
define reina = Character("Mom",image= "reina")
define briana = Character ("Briana", image="briana")
define penny = Character ("Penny", image="penny")
define jenni = Character ("Aunt Jenni ", image="jenni")
define ethan = Character ("Dad", image="ethan")

#Side Characters
define aisha = Character ("Aisha", image="aisha")
define rose = Character ("Dr. Rose", image="rose")
define camilla = Character("Camilla", image="camilla")
define sabrina = Character ("Sabrina",image= "sabrina")
define maxine = Character ("Maxine", image="maxine")
define miyuki = Character ("Miyuki", image="miyuki")

#NPCs
define unwoman = Character ("Unknown Woman", color="#fff")
define unman = Character ("Unknown Man", color="#fff")
define police1 = Character ("Police Man", color="#fff")
define police2 = Character ("Police Woman", color="#fff")
define erdoctor = Character ("ER Doctor", color="#fff")
define ernurse = Character ("ER Nurse", color="#fff")
define cashier = Character ("Cashier", color="#fff")
define referee = Character ("Referee", color="#fff")
define interviewer = Character ("Interviewer", color="#fff")
define opponent = Character ("Opponent", color="#fff")
define receptionist = Character ("Receptionist", color="#fff")
define hairdresser = Character ("Hair Stylist", color="#fff")
define musicclerk = Character ("Music Store Associate", color = "#fff")
define announcer1 = Character("Commentator One", color = "#fff")
define announcer2 = Character("Commentator Two", color= "#fff")

default ReinaC = CharacterData("Reina", "Your mother","A well-known real estate agent who sells luxury homes to the wealthy, Reina often neglects her own family for riches.","Wine", c_trust=0, m_trust=10,c_love=0, m_love=10, a_pic="gui/characters/Reina_a.webp",u_pic ="gui/characters/Reina_u.webp",pic="gui/characters/Reina_Profile.webp")
default JenniC = CharacterData("Aunt Jenni", "Your aunt","A former model, Jenni is recovering from her first divorce." ,"Sweets", c_trust=0, m_trust=10,c_love=0, m_love=10, a_pic="gui/characters/Jenni_a.webp",u_pic ="gui/characters/Jenni_u.webp",pic="gui/characters/Jenni_profile.webp")
default BrianaC = CharacterData("Briana", "The Boxing Champ","A three-time boxing champion, Briana is a sweet girl who wants to forge her own path in life." ,"Outdoors",c_trust=0, m_trust=10,c_love=0, m_love=10,a_pic="gui/characters/Briana_a.webp",u_pic ="gui/characters/Briana_u.webp",pic="gui/characters/Briana_Profile.webp")
default PennyC = CharacterData("Penny", "The Skater Girl","As the youngest sibling, Penny feels overshadowed by her older sister. She spends most of her time at the skatepark." ,"Rock Music", c_trust=0, m_trust=10,c_love=0, m_love=10,a_pic="gui/characters/Penny_a.webp",u_pic ="gui/characters/Penny_u.webp",pic="gui/characters/Penny_Profile.webp")
default DrRoseC = CharacterData("Dr. Rose", "Your Therapist","Dr. Rose is considered one of the best therapists in Sierra Beach. Her approach to therapy makes her favorite among the residents.", "Chocolate",c_trust=0, m_trust=10,c_love=0, m_love=10,a_pic="gui/characters/Rose_a.webp",u_pic ="gui/characters/Rose_u.webp",pic="gui/characters/Rose_Profile.webp")
default CamillaC = CharacterData("Camilla", "Pandora's Boutique Owner","The owner of a high-end women's boutique, Camilla is nice woman despite her statuely appearance." ,"Expensive Jewelry",c_trust=0, m_trust=10,c_love=0, m_love=10, a_pic="gui/characters/Camilla_a.webp",u_pic ="gui/characters/Camilla_u.webp",pic="gui/characters/Camilla_Profile.webp")
default AishaC = CharacterData("Aisha", "Briana's Trainer","A former star athlete, Aisha is Briana's Trainer and studying to become a licensed physical therapist." ,"Animals",c_trust=0, m_trust=10,c_love=0, m_love=10, a_pic="gui/characters/Aisha_a.webp",u_pic ="gui/characters/Aisha_u.webp",pic="gui/characters/Aisha_Profile.webp")
default SabrinaC = CharacterData("Sabrina", "Owner of Sierra Games and Fun","Sabrina's family moved to Sierra Beach 4 years ago. Sabrina runs the only game store in town, and soon the only arcade in town." ,"Video Games",c_trust=0, m_trust=10,c_love=0, m_love=10,a_pic="gui/characters/Sabrina_a.webp",u_pic ="gui/characters/Sabrina_u.webp",pic="gui/characters/Sabrina_Profile.webp")
default MiyukiC = CharacterData("Miyuki", "City Councilwoman","A long time resident of Sierra Beach, Miyuki is currently running for Mayor. But she has a few skeletons in her closet."  ,"Sweets",c_trust=0, m_trust=10,c_love=0, m_love=10,a_pic="gui/characters/Miyuki_a.webp",u_pic ="gui/characters/Miyuki_u.webp",pic="gui/characters/Miyuki_Profile.webp")

default selectedCharacter = ReinaC
# The game starts here.
label start:

    stop music
    scene black
    call screen consentscreen

label playerentername:
    hide text
    $ player_name = renpy.input("Enter Name Here")
    $ player_name = player_name.strip()
    if player_name == "":
        $player_name = "Alex"
        jump prologue
    else:
        jump prologue

return
