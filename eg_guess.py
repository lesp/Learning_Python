#Easygui guessing game

import random, easygui

secret = random.randint(1,99)
guess = 0
tries = 0

easygui.msgbox("Guess a number between 1 and 99, you have 6 tries")

while guess != secret and tries < 6:
    guess = easygui.integerbox("What's your guess?")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("You guessed correctly")
else:
    easygui.msgbox("You have no more guesses left")
    easygui.msgbox("The answer was " + str(secret))
