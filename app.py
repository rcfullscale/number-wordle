#imports
import time
import random
import math
import numbers
run = True
#runcode
print("welcome the number wordle")
number = random.randint(0, 99)
while run == True:
    i = input(":")
    i = int(i)
    if i < number:
        print("to low")
    elif i > number:
        print("to high")
    else:
        print("correct")
        exit()