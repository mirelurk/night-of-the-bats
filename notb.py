#Text based adventure game use SQLite as the backend to store data.  
#Need to create an interface with which the player will interact.
#Use the database to store the text files that will appear on the screen.
#Create and store a local file that can be used to load a player's progress.

#def startup():
    #Take in the player's previous data, setting the location, inventory and player status

import sqlite3

import player
import gamedata
from gameplay import entry

locdb=sqlite3.connect('assets/locations.db') #connect to the database
lc = locdb.cursor() #creates the cursor for the location database

player = player.Player()
gd = gamedata.Gamedata()
gd.updateld(1)

def stringparse(s):
    p = s.lower()
    p = p.split()
    return(p)

def locinteract(i):
    #input location id to begin interaction with location
    crcmd = "SELECT * FROM sample WHERE ID LIKE {}"
    fetchloc = lc.execute(crcmd.format(i))
    data = fetchloc.fetchone()
    print(data)
    print(data[2])
    flag = 0
    while flag!=1:
        rawinput = input()
        userinput = stringparse(rawinput)
        if len(userinput)==0:
            print(data[2])
        elif (userinput[0]=="go" and userinput[1]=="left"):
            newloc = int(data[6])
            player.loc = newloc
            flag = 1
        elif userinput[0]=="go" and userinput[1]=="right":
            newloc = int(data[4])
            player.loc = newloc
            flag = 1
        elif userinput[0]=="go" and userinput[1]=="back":
            newloc = int(data[5])
            player.loc = newloc
            flag = 1
        elif userinput[0]=="go" and userinput[1]=="forward":
            newloc = int(data[3])
            player.loc = newloc
            flag = 1
        else:
            print("You can't go that way")


def main():
    #No error checking in this function right now
    rawinput = input()
    userinput = stringparse(rawinput)
    flag = 0
    while flag==0:
        entry(userinput)
        flag = gamedata.quit

main()
