#imports
import time
import random
import math
import numbers
run = True
#runcode
print("welcome the number wordle")
print("Input highest number")
h = input(":")
number = random.randint(0,int(h))
while run == True:
    i = input(":")
    if int(i) < number and int(i) > 0:
        print("to low")
    if int(i) > int(h) or int(i) < 0:
        print ("Error number not possible")
    elif int(i) > number and int(i) < int(h):
    i = int(i)
    if i < number:
        print("to low")
    elif i > number:
        print("to high")
    else:
        print("correct")
        exit()