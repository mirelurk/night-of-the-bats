#Text based adventure game use SQLite as the backend to store data.  
#Need to create an interface with which the player will interact.
#Use the database to store the text files that will appear on the screen.
#Create and store a local file that can be used to load a player's progress.

#def startup():
    #Take in the player's previous data, setting the location, inventory and player status

def main():
    flag = 0
    while flag!=1:
        rawinput = input()
        userinput = rawinput.lower()
        userinput = userinput.split()
        if userinput[0]=="quit":
            flag=1
            break
        elif userinput[0]=="go":
            print("Moving character")
        else:
            print("error")
            

main()
