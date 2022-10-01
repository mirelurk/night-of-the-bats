#Text based adventure game use SQLite as the backend to store data.  
#Need to create an interface with which the player will interact.
#Use the database to store the text files that will appear on the screen.
#Create and store a local file that can be used to load a player's progress.

#def startup():
    #Take in the player's previous data, setting the location, inventory and player status

import sqlite3

import player

player = player.Player()

def stringparse(s):
    p = s.lower()
    p = p.split()
    return(p)


def main():
    flag = 0
    while flag!=1:
        rawinput = input()
        userinput = stringparse(rawinput)
        #print(userinput)
        if len(userinput)==0:
            print("blank")
        elif userinput[0]=="quit":
            flag=1
            break
        elif userinput[0]=="go":
            currloc = player.loc
            player.loc = currloc+1
            print(player.loc)
        else:
            print("error")
            

main()
