import random
import time
num=random.randint(10,15)
print("may i ask you for your name")
def intro():
    name= input("enter:may i know your name")
    print(f"nice to meet you {name}\n now we will play a nice game")
def pick():
    attempt=0
    while attempt<5:
        guess=int(input("enter your guess "))
        if guess==num:
            print(f"good job!you guessed the number correctly in{attempt} attempt")
            break
        else:
            attempt=attempt+1
    if(attempt>=5):
        print(f"the actual no. was {num}\n better luck next time.")
play_again="yes"
while play_again=="no" or play_again=="yes":
    intro()
    pick()
    print("do you want to play it again?")
    play_again=input()