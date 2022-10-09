

class Player:
    def __init__(self):
        self.health = 50 #initial health
        self.xp = 0 #starts at 0 xp
        self.loc = 1 #starting location for a new game
        self.inv = []

    def status(self):
        status = str("Health: "+self.health+"XP: "+self.xp)
        print(status)

    def updatehealth(self, n):
        currhealth = self.health
        self.health = currhealth + n

    def printinv(self):
        for i in self.inv:
            print(i)

    def dropinv(self, item):
        itemi = self.inv.index(item)
        self.inv.pop(itemi)
        return(1)
    
    def addinv(self, item):
        self.inv.append(item)
        return(1)
