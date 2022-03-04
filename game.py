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


def openNewWindow():
    roott = tk.Toplevel(root)
    roott.attributes('-fullscreen',True)
    hp = 5
    bg = tk.PhotoImage(file = "images/"+ str(hp) +".png")
    bg = bg.subsample(2)
    canvas1 = tk.Canvas(roott)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 30, 40, image = bg, anchor = "nw")
    lblGuessChar = tk.Label(roott, text="", font=('', 72))
    lblGuessChar.place(relx = 0.9,rely = 0.95, anchor='s')
    pnlProgress = PanedWindow(canvas1, orient="horizontal")
    # lblCheat = tk.Label(root, text=theWord, font=('', 24))
    # lblCheat.pack()
    drawBlanks()
    newGameBool=False
    roott.bind('<KeyPress>', onKeyPress)
    roott.mainloop()

root = tk.Tk()
root.attributes('-fullscreen',True)
bakgr = tk.PhotoImage(file = "images/"+ str(hp) +".png")
bakgr = bakgr.subsample(2)
canvas1 = tk.Canvas(root)
canvas1['bg'] = 'black'
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 30, 40, image = bakgr, anchor = "nw")

# prompt = tk.Label(root, text="Hangman", fg='orange', bg='green', font=('Helvetica', 72, 'bold'), borderwidth=20, relief='ridge')
# prompt.place(relx=0.5, rely=0.4, anchor='center')
# prompt = tk.Label(root, text="Choose Difficulty", fg='green', bg='#e77feb', font=('', 24), borderwidth=5, relief='ridge')
# prompt.place(relx=0.5, rely=0.55, anchor='center')
# choices = ['Easy', 'Medium', 'Hard']
# variable = tk.StringVar(root)
# variable.set('Medium')
# w = tk.OptionMenu(root, variable, *choices)
# b = tk.Button(root, text="Play!", command=openNewWindow)
# w.place(relx=0.48, rely=0.6, anchor='center')
# b.place(relx=0.53, rely=0.6, anchor='center')

lblGuessChar = tk.Label(root, text="", font=('', 72))
lblGuessChar.place(relx = 0.9,rely = 0.95, anchor='s')
pnlProgress = PanedWindow(canvas1, orient="horizontal")
lblCheat = tk.Label(root, text=theWord, font=('', 24))
lblCheat.pack()
drawBlanks()

newGameBool=False
root.bind('<KeyPress>', onKeyPress)
root.mainloop()

#https://stackoverflow.com/questions/44790449/making-tkinter-wait-untill-button-is-pressed