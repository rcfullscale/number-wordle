
import time
import random
def digit (num):
    return ord(num)>=48 and ord(num)<=57
def digits(number):
    for char in number:
        if not digit(char):
            return False
    return True
guess = 1
print("Welcome to the number wordle")
print("Input number you want to be the highest option below")
h = input(":")
if not digits(h):
    print ("This is a number game")
elif h=='':
    print("You must enter a number")
else:
    number = random.randint(0,int(h))
    run = True
    print("Start guessing, this is your first guess")
    while run == True and guess<11:
        print("You are on guess " + str(guess))
        i = input(":")
        if not digits(i):
            print('This is a "number" game')
        elif i=='':
            print('You must enter a number')
        elif int(i) < number and int(i) > 0:
            print("To low")
        elif int(i) > int(h) or int(i) < 0:
            print ("Error number not possible")
        elif int(i) > number and int(i) < int(h):
            print ("To high")
        else:
            print("Correct")
            input("Click enter to exit")
            exit()
        guess += 1