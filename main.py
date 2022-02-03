from graphics import *
from letter import *

correct_guess = False

blank_space = Blank_Space("h", 0)
blank_space = Blank_Space("e", 1)
blank_space = Blank_Space("l", 2)
blank_space = Blank_Space("l", 3)
blank_space = Blank_Space("o", 4)

for b in blank_spaces:
    print(str(b))
    was_guess_correct = b.was_letter_guessed("l")
    if was_guess_correct == True:
        correct_guess = True

if correct_guess == False:
    lives -= 1
    print("incorrect")

print(correct_guess)
