#Text based adventure game use SQLite as the backend to store data.  
#Need to create an interface with which the player will interact.
#Use the database to store the text files that will appear on the screen.
#Create and store a local file that can be used to load a player's progress.

#def startup():
    #Take in the player's previous data, setting the location, inventory and player status

import sqlite3

import player
import gamedata
import location
from gameplay import locinteract

locdb=sqlite3.connect('assets/locations.db') #connect to the database
lc = locdb.cursor() #creates the cursor for the location database

player = player.Player()
loc = location.Location()
loc.updateld(1)

def stringparse(s):
    p = s.lower()
    p = p.split()
    return(p)


def main():
    #No error checking in this function right now
    flag = 0
    while flag==0:
        rawinput = input(">")
        ui = stringparse(rawinput)
        if ui[0]=="go":
            if ui[1]=="forward":
                if loc.forward==0:
                    print("You can't go that way.")
                else:
                    loc.mvforward()
                    print(loc.locdescrip)
            elif ui[1]=="back":
                if loc.back==0:
                    print("You can't go that way.")
                else:
                    loc.mvback()
                    print(loc.locdescrip)
            elif ui[1]=="left":
                if loc.left==0:
                    print("You can't go that way.")
                else:
                    loc.mvleft()
                    print(loc.locdescrip)
            elif ui[1]=="right":
                if loc.right==0:
                    print("You can't go that way.")
                else:
                    loc.mvright()
                    print(loc.locdescrip)
            else:
                print("You can't go forward, back, left or right.")
        elif ui[0]=="quit":
            flag = 1
        elif ui[0]=="inventory":
            inventory()
        elif ui[0]=="look":
            print(loc.locdescrip)
        else:
            continue

main()
