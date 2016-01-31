# Joshua Savon
import random
#guessing game intro
print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number bewteen 1 and 50.')
secretNumber = random.randint(1, 50)

#ask player to guess
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
       print('Your guess is too low.')
    elif guess > secretNumber:
       print('Your guess is too high')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '!You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))