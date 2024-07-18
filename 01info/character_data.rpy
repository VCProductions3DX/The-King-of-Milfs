#Character Data
init -890 python:
    #Description
    class CharacterList():
        def __init__(self):
            self.characterlist = []

        def add_Character(self,CharacterData):
            self.characterlist.append(CharacterData)

        def remove_Character(self,CharacterData):
            self.characterlist.remove(CharacterData)


    #Character Name; Title; One Sentence Description, Current Trust, Maximum Trust, Current Love, Maximum Love, Hovered Pic, Unhovered Pic
    class CharacterData():
        def __init__(self,name,title,desc,likes, c_trust=0,m_trust=10, c_love=0, m_love=10, a_pic=None,u_pic =None, pic=None):
            self.name= name
            self.title= title
            self.desc = desc
            self.likes = likes
            self.c_trust = c_trust
            self.m_trust = m_trust
            self.c_love=c_love
            self.m_love=m_love
            self.a_pic = a_pic
            self.u_pic = u_pic
            self.pic = pic

        #Trust - (0, 10)
        def trust_up( self,amount):
            if self.c_trust == self.m_trust:
                c_trust +=0
            else:
                self.c_trust += amount
            return self.c_trust

        def trust_down(self,amount):
            if self.c_trust == 0:
                self.c_trust -=0
            else:
                self.c_trust -=amount

        #Love - (0, 10) 
        def love_up( self,amount):
            if self.c_love == self.m_love:
                self.c_love +=0
            else:
                self.c_love += amount
            return self.c_love

    #This describes every major choice in the game
    #Possibly add 2 more modifiers- which character is affected by the decision, and a picture.
    class Choice():
        def __init__(self,desc):
            self.choices = self
            self.desc = desc

    #This is for Replay Mode. If the player wants to repeat or view an event they skipped, they can. 
    #Every Event has a picture, title, and a 1-sentence description as well as if they have completed the event.
    class CharacterEvent():
        def __init__(self,name,status,desc,image=None):
            self.name = name
            self.status = status
            self.desc = desc
            self.image = image
        def status_completed(self,status):
            if self.status == "completed":
                return None
            else:
                self.status = "completed"
        def status_skipped(self,status):
            if self.status == "completed":
                return None
            else:
                self.status = "skipped"

    class EventsContainer():
        def __init__(self):
            self.eventscontainer = []
        def add_Event(self,Event):
            self.eventscontainer.append(Event)
        def remove_event(self,Event):
            self.eventscontrainer.remove(Event)
