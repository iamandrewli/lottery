import random

lottoNumbers = []
euroNumbers = []
luckyNumbers = []


def lotto():
    for i in range (0,6):
        number = random.randint(1,59)
        while number in lottoNumbers:
            number = random.randint(1,59)
        lottoNumbers.append(number)
    lottoNumbers.sort()
    print("\n")
    print("Today's lottery numbers are: ")
    print(lottoNumbers)
    print("\n")
    again()



def euro():
    for i in range (0,5):
        number = random.randint(1,50)
        while number in euroNumbers:
            number = random.randint(1,50)
        euroNumbers.append(number)
    euroNumbers.sort()
    print("\n")
    #print("Today's Euromillion numbers are: ")
    print(euroNumbers)
    print("\n")
    luckyStars()
    again()


def luckyStars():
    for i in range(0,2):
        starnumber = random.randint(1,12)
        while starnumber in luckyNumbers:
            starnumber = random.randint(1,12)
        luckyNumbers.append(starnumber)
    luckyNumbers.sort()
    print("and your lucky stars are: ")
    print(luckyNumbers)
    print("\n")




def start():
    print "Press 'L' for Lotto or 'E' for Euro"

    userInput = raw_input("> ")

    if userInput == "l":
        lotto()
    elif userInput == "e":
        euro()
    else:
        print "Try again"
        start()


def again():
    print "Do you wanna go again? Y or N?"
    retry = raw_input(">")
    if retry == "y":
        #This clears the list [:] = []
        lottoNumbers [:] = []
        euroNumbers [:] = []
        luckyNumbers [:] = []
        start()
    else:
        exit(0)



#main script starts here.
start()
