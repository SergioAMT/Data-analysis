class PartyAnimal:
    x = 0
    name = ""
    
    def __init__(self, z):
        print('I am constructed')
        self.name = z
        print(self.name, "constructed")
            
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
    
    # def __del__(self):
    #     print('Im destructured', self.x)
        
# an = PartyAnimal('sally')
# jn = PartyAnimal('Jim')
# an.party()
# jn.party()
# an = 42
# an.party() no se ejecuta 
# print('an contains', an)

class FootballFan (PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points ', self.points)
        
q = FootballFan('Carlos')
q.touchdown()
q.party()