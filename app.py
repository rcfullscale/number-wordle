#imports
import time
import random
run = True
#runcode
print("Welcome the number wordle")
number = random.randint(0, 100)
while run == True:
    i = input(":")
    if int(i) < number:
        print("to low")
    elif int(i) > number:
        print("to high")
    else:
        print("correct")
        run=False