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
        print("To low")
    elif int(i) > int(h) or int(i) < 0:
        print ("Error number not possible")
    elif int(i) > number and int(i) < int(h):
        print ("To high")
    else:
        print("correct")
        input("click enter to exit")