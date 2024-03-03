
import time
import random
guess = 1
#runcode
print("Welcome to the number wordle")
while True:
    print("Input number you want the answer to be below")
    highest_number = input(": ")
    try:
        highest_numberint = int(highest_number)
        break
    except ValueError:
        print("do you have a decimel or letter because they arent allowed")
number = random.randint(0,int(highest_number))
#main
run = True
print("Start guessing, this is your first guess")
while True:
    print("You are on guess " + str(guess))
    while True:
        i_num = input(":")
        try:
            i = int(i_num)
            break
        except ValueError:
            print("do you have a decimel or letter because they arent allowed")
    if i < number:
        print("To low")
    elif i > int(highest_number):
        print ("Error number to high")
    elif i > number:
        print ("To high")
    else:
        print("Correct")
        input("Click enter to exit")
        exit()
    guess += 1