import random

print("Welcome to Number Guesser:")

num = random.randrange(100)
chance = 7

print("You have 7 chances to guess the number:")

for i in range(0,chance,1):
    
    guess = int(input("Guess the number between 1 to 100:"))
    
    if num==guess:
        print("Congrats!, You guessed the number in",i+1,attemps)
        
    elif num>guess:
        print("Guess is lower")  
   
    elif num<guess:
        print("Guess is higher")
        
        
else:
    print("Number was:",num,"Better Luck Next Time") 
