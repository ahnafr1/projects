from random import *

def rpsgame():
    global p_move, cpu
    options = ["r", "p", "s"]
    p_move = str(input("Enter what move you want (r,p,s)"))
    cpu = (choice(options))
    if p_move == "r" or p_move == "p" or p_move == "s":
        print (p_move + " vs. " + cpu)
        outcomes()
    else:
        print ("That was not an option. Try again")
        rpsgame()

def outcomes():
    #situations for player inputs rock
    if p_move == "r" and cpu == "r":
        print ("Dang it was tie")
    elif p_move == "r" and cpu == "p":
        print ("Sorry you lost better luck next time")
    elif p_move == "r" and cpu == "s":
        print ("Nice job you won!")

    #situations for player inputs paper
    elif p_move == "p" and cpu == "r":
        print ("Nice job you won!")
    elif p_move == "p" and cpu == "p":
        print ("Dang it was tie")
    elif p_move == "p" and cpu == "s":
        print ("Sorry you lost better luck next time")
        
    #situations for player inputs scissors
    elif p_move == "s" and cpu == "r":
        print ("Sorry you lost better luck next time")
    elif p_move == "s" and cpu == "p":
        print ("Nice job you won!")
    elif p_move == "s" and cpu == "s":
        print ("Dang it was tie")

    else:
        print ("Ummm that was not an option")

while True: #loop the code until user breaks
    print ("Welcome to Ahnaf's Rock Paper Scissors Game!")
    rpsgame()
    while True:
        confirm = input("Do you want to continue? (y/n): ")

        if confirm == "y":
            res = True
            break
        elif confirm == "n":
            res = False
            break
        else:
            True

    if res == False:
        break
