#imports
import time
import random
import math
import numbers
run = True
#runcode
print("welcome the number wordle")
number = random.randint(0, 98)
while run == True:
    i = input(":")
    if int(i) < number:
        print("to low")
    elif int(i) > number:
        print("to high")
    else:
        print("correct")
        exit()