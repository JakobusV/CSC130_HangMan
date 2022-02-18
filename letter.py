from game import *

blank_spaces = []

class Letter():

    def __init__(self, letter, relx, rely):
        self.letter = letter
        self.relx = relx
        self.rely = rely

        self.draw_letter()

        print("letter made")
        
    def draw_letter(self):
        pass
    
class Blank_Space:

    def __init__(self, letter, phrase_index):
        self.letter = letter
        self.phrase_index = phrase_index
        self.relx = 0.1 + (phrase_index * 0.12)
        self.rely = 0.8
        self.guessed = False
        blank_spaces.append(self)

        self.draw_space()

    def __str__(self):
        return "letter: " + str(self.letter) + " index: " + str(self.phrase_index)

    def draw_space(self):
        pass

    def was_letter_guessed(self, guess):
        if guess == self.letter:
            Letter(self.letter, self.relx, self.rely)
            self.guessed = True
            return True
