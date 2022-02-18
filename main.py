from graphics import *
from phrase import *

correct_guess = False

guessed_input = "a"

def unique_guess(v):
    for i in list_of_letters_guessed:
        print(i + " " + v)
        if(i == v):
            return False
    return True

input_invalid = False

iter = 0
while iter < 3:
    if unique_guess(guessed_input):
        for b in blank_spaces:
            print(str(b))

            was_guess_correct = b.was_letter_guessed(guessed_input)
            list_of_letters_guessed.append(guessed_input)
            
            if was_guess_correct == True:
                correct_guess = True
    else:
        print("already guessed")
        input_invalid = True

    if input_invalid == False and correct_guess == False:
        lives -= 1
        print(lives)
    
    iter += 1

print(lives)
