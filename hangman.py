disp = ['''
        +---+
        0   |
       /|\  |
       / \  |
           === ''','''
        +---+
        0   |
       /|\  |
       /    |
           === ''','''
        +---+
        0   |
       /|\  |
            |
           === ''','''
        +---+
        0   |
       /|   |
            |
           === ''','''
        +---+
        0   |
        |   |
            |
           === ''','''
        +---+
        0   |
            |
            |
           === '''
        ]
def word_inp():
    word = list((input("Player 1 enter your word: ")))
    
    for i in word:
        p_1.append(i)
    return p_1

def term_clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def p_2_view():
    word_inp()
    term_clear()
    i = 0
    while i < len(p_1):
        if p_1[i] == " ":
            p_2.append(" ")
        elif isinstance(p_1[i], str):
            p_2.append("_")
        i += 1
    print (p_2)

def guesser():
    global trys
    trys = 6
    count = 0
    while count < trys and p_2 != p_1:  
        attempt = str(input("Guesss a letter: "))
        if attempt in p_1:
            x = 0
            while x < len(p_1):
                if attempt == p_1[x]:
                    p_2[x] = attempt
                    term_clear()
                    print ("Trys left: ",trys)
                    print (p_2)
                    break
                else:
                    x += 1
        else:
            trys -= 1
            term_clear()
            print ("You have ", trys, " trys left")
            print (disp[trys],"\n")
            print (p_2)
    return

def result():
    guesser()
    if p_2 == p_1:
        print ("You won nice job!")
    if trys == 0:
        term_clear()
        print (disp[0])
        print ("Sorry you lose. The word was:\n ",p_1)

while True: #loop the code until user breaks
    p_1 = []
    p_2 = []
    p_2_view()
    result()
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
