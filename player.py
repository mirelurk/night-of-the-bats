

class Player:
    def __init__(self):
        self.health = 50 #initial health
        self.xp = 0 #starts at 0 xp
        self.loc = 1 #starting location for a new game

    def status(self):
        status = str("Health: "+self.health+"XP: "+self.xp)
        print(status)
