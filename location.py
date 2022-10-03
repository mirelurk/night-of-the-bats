

class Location:
    def __init__(self):
       self.loc = 1 #current location of the player
       self.ld = 0 #full data from location database
       self.locdescrip = 0 #description line
       self.forward = 0 #id for moving forward
       self.right = 0 #id for moving to the right
       self.back = 0 #id for moving back
       self.left = 0 #id for moving to the left
       self.itemsavail = 0 #items available at the location

    def updateld(self, cmd):
        sqlite3=__import__('sqlite3')
        locdb = sqlite3.connect('assets/locations.db')
        lc = locdb.cursor()
        crcmd = "SELECT * FROM sample WHERE ID LIKE {}"
        fetchloc = lc.execute(crcmd.format(cmd))
        locdata = fetchloc.fetchone()

        self.loc = cmd
        self.ld = locdata
        self.locdescrip = locdata[2]
        self.forward = locdata[3]
        self.right = locdata[4]
        self.back = locdata[5]
        self.left = locdata[6]

    def mvforward(self):
        newloc = self.forward
        self.updateld(newloc)

