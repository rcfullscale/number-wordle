
import time
import random
# check each character if it's a number
def digit (num):
    return ord(num)>=48 and ord(num)<=57
# check the whole number at once for non-number characters
def digits(number):
    for char in number:
        if not digit(char):
            return False
    return True
guess = 1
#runcode
print("Welcome to the number wordle")
print("Input number you want the answer to be below")
h = input(": ")
number = random.randint(0,int(h))
#main
run = True
print("Start guessing, this is your first guess")
while True:
    print("You are on guess " + str(guess))
    i = input(":")
    if int(i) < number:
        print("To low")
    elif int(i) > int(h) or int(i) < 0:
        print ("Error number not possible")
    elif int(i) > number:
        print ("To high")
    else:
        print("Correct")
        input("Click enter to exit")
        exit()
    guess += 1