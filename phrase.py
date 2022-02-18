from letter import *

list_of_letters_in_word = []

word = getRandomWord(getListOffDifficulty(difficulty_input))

for w in word:
    list_of_letters_in_word.append(w)

print(list_of_letters_in_word)

i=0
while i < len(list_of_letters_in_word):
    blank_space = Blank_Space(list_of_letters_in_word[i], i)
    i +=1