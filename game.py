from cgitb import text
from glob import glob
import tkinter as tk
from tkinter import font
from tkinter.ttk import PanedWindow
from unicodedata import name
import wordBank, sys

newGameBool = True
allLabels = []
progress = {}
theWord = wordBank.getRandomWord(wordBank.getListOffDifficulty(sys.argv[1])).lower()
hp = 5
canvas1 = None
gameover = False

for letter in theWord:
    progress[letter] = False
print(progress)

def ballCheck(guess):
    for letter in theWord:
        if (guess == letter):
            progress[letter] = letter
            return True

def drawBlanks():
    if (newGameBool):
        spacing = 0.1
        for letter in theWord:
            lbl = tk.Label(canvas1, text="_", font=('', 64))
            lbl.place(relx = spacing,rely = 0.95, anchor='s')
            allLabels.append(lbl);
            spacing += 0.08
    else:
        currentLabel = 0
        for letter in theWord:
            LabelText = "_"
            if(progress[letter]):
                LabelText = letter.upper()
            allLabels[currentLabel].config(text=LabelText)
            currentLabel += 1


def onKeyPress(event):
    global gameover
    if not gameover:
        if (event.char.isalpha()):
            guess = event.char.lower()
            global lblGuessChar
            lblGuessChar.config(text=guess.upper())
            iscorrect = ballCheck(guess)
            drawBlanks()
            if (not iscorrect):
                global hp, bg
                hp = hp - 1
                bg.config(file = "images/"+ str(hp) +".png")
                bg = bg.subsample(2)
                canvas1.create_image( 30, 40, image = bg, anchor = "nw")
                if hp == 0:
                    gameover = True
                    lblCheat = tk.Label(root, text=theWord.upper(), font=('', 32, "bold"), bg="black", fg="red")
                    lblCheat.pack()

root = tk.Tk()
root.attributes('-fullscreen',True)
bg = tk.PhotoImage(file = "images/"+ str(hp) +".png")
bg = bg.subsample(2)
canvas1 = tk.Canvas(root)
canvas1['bg'] = 'black'
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 30, 40, image = bg, anchor = "nw")

lblGuessChar = tk.Label(root, text="", font=('', 72))
lblGuessChar.place(relx = 0.9,rely = 0.95, anchor='s')
pnlProgress = PanedWindow(canvas1, orient="horizontal")
# lblCheat = tk.Label(root, text=theWord, font=('', 24))
# lblCheat.pack()
drawBlanks()

newGameBool=False
root.bind('<KeyPress>', onKeyPress)
root.configure(bg="black")
root.mainloop()