# # importing tkinter for gui
# import tkinter as tk
# from turtle import width
# from click import command

# def play():
#     print("Hello mama")
#     # setting attribute
#     window.attributes('-fullscreen', True)
#     window.title("Hangman2")
#     # creating text label to display on window screen
#     label = tk.Label(window, text="Hangman2!")
#     label.pack()
#     window.mainloop()

# def onKeyPress(event):
#     label.insert('end', 'You pressed %s\n' % (event.char, ))

# # creating window
# window = tk.Tk()

# # setting attribute
# window.attributes('-fullscreen', True)
# window.title("Hangman")

# # creating text label to display on window screen
# label = tk.Label(window, text="Hangman!")
# label.pack()

# # creating button
# button = tk.Button(
#     text="Click me!",
#     width=10,
#     height=2,
#     bg="white",
#     fg="black",
#     command=play
# )
# button.pack()

# # creating text box to enter into
# entry = tk.Entry(fg="white", bg="black", width=50, justify="center", font=('Georgia 32'))
# entry.pack()

# window.mainloop()

from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import font
from tkinter.ttk import PanedWindow
import wordBank

def getDifficulty():
    return "easy";

def ballCheck(answer, currentProgress, guess):
    word = currentProgress
    for i in range(len(answer)):
        if (currentProgress[i] == "_"):
            if (answer[i] == guess):
                currentProgress[i] = guess
    return word

progress = "_ _ _ _"
theWord = wordBank.getRandomWord(wordBank.getListOffDifficulty(getDifficulty()))

def onKeyPress(event):
    if (event.char.isalpha()):
        guess = event.char.upper()
        lblGuessChar.config(text=guess)
        results = ballCheck(theWord, progress, guess)
        lblBlanks.config(text=results)

root = tk.Tk()

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)

lblGuessChar = tk.Label(root, text="", font=('', 72))
lblGuessChar.place(relx = 0.5,rely = 0.5, anchor='center')

lblBlanks = tk.Label(root, text=progress, font=('', 60))
lblBlanks.place(relx=0.5, rely=0.8, anchor='center')

pnlPProgress = PanedWindow(root, orient="horizontal")

root.bind('<KeyPress>', onKeyPress)
root.mainloop()

# label = tk.Label(root, background='black', foreground='white', text="You guessed:")
# label.pack()
# lblGuess = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
# lblGuess.pack()