
class Gamedata:
    def __init__(self):
        self.quit = 0 #flag for quitting the game
        self.loc = 1 #current location of the player
        self.ld = 0
        self.locdescrip = 0
    
    def updateld(self, cmd):
        sqlite3 = __import__('sqlite3')
        locdb=sqlite3.connect('assets/locations.db')
        lc = locdb.cursor()
        crcmd = "SELECT * FROM sample WHERE ID LIKE {}"
        fetchloc = lc.execute(crcmd.format(self.loc))
        locdata = fetchloc.fetchone()
        self.ld = locdata
        self.locdescrip = locdata[2]

