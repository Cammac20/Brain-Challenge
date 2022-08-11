# Brain Challenge

# imports the time module
import time

# creates a username variable
un = input("Welcome to Brain Challenge, what would you like your username to be? ")

# creates a password variable
pw = input("Okay, " + un + " what would you like your password to be? ")

# creates a repeat password variable
while True:
    rpw = input("Repeat password. ")
    if (rpw == pw):
        break

input("Okay, let's get started. MAKE SURE to capitalize names correctly. Press enter to start. ")


qOne = input("For your first Brain Challenge, how many letters are in the alphebet? ")

if qOne == '11':
    print("Correct! ")

else:
    print("Incorrect, the anwser is 11.")
    exit()

time.sleep(3)
qTwo = input("Next, what is the capital of Texas? ")

if qTwo == 'Austin':
    print("Correct again!")

else:
    print("Incorrect, the anwser is Austin.")
    exit()

time.sleep(3)
qThree = input("Okay now, what year was The Declaration of Independance signed? ")

if qThree == '1776':
    print("Correct once again!")

else:
    print("Incorrect, the anwser is 1776")
    exit()

time.sleep(3)
qFour = input("Two more to go, who invented gravity? ")

if 'God' in qFour:
    print("Correct! Man you are on a roll. ")

else:
    print("Nope, the anwser is God.")
    time.sleep(2)
    exit()

time.sleep(3)
qFive = input("Last question, what was the anwser to the first question? ")

if qFive == '11':
    print("Congratulations! You have beat my game.")

else:
    print("Incorrect, the anwser was 11. Man you were so close...")
    exit()

time.sleep(3)

yon = input("Would you like to play another game y or n?")

if 'n' in yon:
    print("Ok, have a good day.")
    time.sleep(2)
    exit()

time.sleep(3)

input("Okay, press enter to begin.")

time.sleep(3)

qSix = input("what is the slope of this linear equation? y=-4x+5 ")

if '-4' in qSix:
    print("Correct! the anwser is -4")

else:
    print("No the anwser is -4")
    time.sleep(2)
    exit()

time.sleep(3)

qSeven = input("H0w m4ny num6ers are 1n th1s s3ntenc3? ")

if '7' in qSeven:
    print("Correct again!")

else:
    print("Nope, the anwser is 7")
    time.sleep(2)
    exit()

time.sleep(3)

qEight = input("How many legs does a tarantula have? ")

if '8' in qEight:
    print("Correct, man i gotta make these harder.")

else:
    print("Nope the anwser is 8, man you made it so far.")
    time.sleep(2)
    exit()

time.sleep(3)

qNine = input("2 more left. Who invented the lightbulb? ")

if 'Thomas' in qNine:
    print("Correct! One more to go!")

else:
    print("Oh Noooo, sooo close. The anwser was Thomas Edison")
    exit()

time.sleep(3)

qTen = input("Last Question! What is the smallest country in the world? ")

if 'vatican' in qTen:
    print("CONGRATULATIONS! YOU HAVE WON MY GAME!")
    time.sleep(2)
    
else:
    print("Oh noooo sooo close. The anwser is Vatican City.")
    time.sleep(2)
    exit()

print("I hope you have enjoyed playing Brain Challenge, Have a great day!")