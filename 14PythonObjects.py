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
    
    def __del__(self):
        print('Im destructured', self.x)
        
an = PartyAnimal('sally')
an.party()
an.party()

jn = PartyAnimal('Jim')
jn.party()
# an = 42
# an.party() no se ejecuta 
# print('an contains', an)