import random

lotto_numbers = []
euro_numbers = []
lucky_numbers = []


def lotto():
    for i in range (0,6):
        number = random.randint(1,59)
        while number in lotto_numbers:
            number = random.randint(1,59)
        lotto_numbers.append(number)
    lotto_numbers.sort()
    print("\n")
    print("Today's lottery numbers are: ")
    print(lotto_numbers)
    print("\n")
    again()



def euro():
    for i in range (0,5):
        number = random.randint(1,50)
        while number in euro_numbers:
            number = random.randint(1,50)
        euro_numbers.append(number)
    euro_numbers.sort()
    print("\n")
    #print("Today's Euromillion numbers are: ")
    print(euro_numbers)
    print("\n")
    luckyStars()
    again()


def luckyStars():
    for i in range(0,2):
        starnumber = random.randint(1,12)
        while starnumber in lucky_numbers:
            starnumber = random.randint(1,12)
        lucky_numbers.append(starnumber)
    lucky_numbers.sort()
    print("and your lucky stars are: ")
    print(lucky_numbers)
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
        lotto_numbers [:] = []
        euro_numbers [:] = []
        lucky_numbers [:] = []
        start()
    else:
        exit(0)



#main script starts here.
start()
