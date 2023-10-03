import random
import time

#Number guessing game

m=random.randint(1,10)
guess=int(input("Enter number from 1-10"))

#print(guess)
while m!=guess:
    if guess<m:
        print("Opss.. The number is lower")
        guess=int(input("Enter the number again"))
    elif guess>m:
        print("Ohoo.. The number is higher")
        guess=int(input("Enter the number again"))
print("BINGO GOT IT..!!")
