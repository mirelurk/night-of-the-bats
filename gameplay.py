#Core gameplay functionality

import gamedata

#flags
locflag = 0

def locinteract(n):
    if n[1]=="right":
        pass
    elif n[1]=="left":
        pass
    elif n[2]=="forward":
        newloc = int(gd.ld[3])
        gd.loc = newloc
    elif n[1]=="back":
        pass
    else:
        print("You can go back, forward, right or left.")

def entry(n):
    if n[0]=="go":
        locinteract(n)
    elif n[0]=="quit":
        gd.quit = 1
    elif n[0]=="inventory":
        #inventory function
        pass
    elif n[0]=="look":
        print(gamedata.locdescrip)
    else:
        pass

