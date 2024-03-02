#imports
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
run = True
#runcode
print("Welcome the number wordle")
number = random.randint(0, 100)
while run == True:
    i = input(":")
    if not digits(i):
        print('this is a "number" game')
    elif int(i) > number:
        print("to high")
    elif int(i) < number:
        print("to low")
    else:
        print("correct")
        run=False