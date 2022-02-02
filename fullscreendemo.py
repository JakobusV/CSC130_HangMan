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

import tkinter as tk
from tkinter import font

def onKeyPress(event):
    if (event.char.isalpha()):
        lblGuessChar.config(text=event.char.upper())

root = tk.Tk()

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)

lblGuessChar = tk.Label(root, text="", font=('', 72))
lblGuessChar.place(relx = 0.5,rely = 0.5,anchor = 'center')

root.bind('<KeyPress>', onKeyPress)
root.mainloop()

# label = tk.Label(root, background='black', foreground='white', text="You guessed:")
# label.pack()
# lblGuess = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
# lblGuess.pack()