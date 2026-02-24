import random
print("Welcome to Guess the Number!")
print("I will think of a number, you try to guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")

    if int(guess) == number:
        print("Correct! You win!")
        isGuessRight = True
    else:
        print("Wrong! Try again.")