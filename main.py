import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number: 
        guess= int(input("Guess a number netween 1 and {x}:"))
        if guess< random_number:
            print("Sorry, try again")
        elif guess >random_number:
            print("Sorry,too high")
            
    print(f"Kudos, you have guessed {random_number} correctly")
        
guess(10)
        