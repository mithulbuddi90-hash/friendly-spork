import random
playing = True
number = str(random.randint(0,9))
print("Welcome to the Number Guessing Game!")
print("I will generate a random number between 0 and 9, and you have to guess it. one digit at a time.")
print("The game ends when you get 1 hero!")
while playing:
    guess = input("Give me your best guess: \n")
    if number == guess:
        print("You guessed it right!")
        print("the number was: ",  number)
        break
    else:
        print("Your guess is wrong, try again!")
        
      
