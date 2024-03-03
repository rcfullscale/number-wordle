
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
highest_number = input(": ")
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
            print("there was a letter in your answer")
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