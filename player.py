

class Player:
    def __init__(self, health, xp):
        self.health = 50 #initial health
        self.xp = 0 #starts at 0 xp

    def status(self):
        status = str("Health: "+self.health+"XP: "+self.xp)
        print(status)
