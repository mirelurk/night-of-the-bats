#Core gameplay functionality

#flags
locflag = 0

def locinteract(n):
    if n[1]=="right":
        pass
    elif n[1]=="left":
        pass
    elif n[1]=="forward":
        return(1)
    elif n[1]=="back":
        pass
    else:
        print("You can go back, forward, right or left.")

def entry(n):
    print(Gamedata.gd.loc)
    if n[0]=="go":
        locinteract(n)
        return(0)
    elif n[0]=="quit":
        return(1)
    elif n[0]=="inventory":
        #inventory function
        return(0)
    elif n[0]=="look":
        print(Gamedata.gd.locdescrip)
        return(0)
    else:
        return(0)

