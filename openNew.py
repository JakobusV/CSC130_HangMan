from tkinter import *
from tkinter import ttk
import os
from playsound import playsound
import soundcenter
from soundcenter import play_sound_file

# playsound('sounds/main.mp3')


win = Tk()
win.geometry("560x320")

def start_window():
    dif = variable.get().lower()

    #This is cool check this out, we can put arguments in the shell command to start the file with the difficulty
    if ("hard" == dif):
        os.system('python game.py hard')
    elif ("medium" == dif):
        os.system('python game.py medium')
    else:
        os.system('python game.py easy')

Label(win, text= "Hangman", fg='orange', bg='green', font=('Helvetica', 72, 'bold'), borderwidth=20, relief='ridge').pack(pady=10)
Label(win, text="Choose Difficulty", fg='green', bg='#e77feb', font=('', 24), borderwidth=5, relief='ridge').pack(pady=5)
choices = ['Easy', 'Medium', 'Hard']
variable = StringVar(win)
variable.set(choices[0])
option_menu = OptionMenu(win, variable, *choices).pack(pady=5)
ttk.Button(win, text="Play!", command=start_window).pack()

win.mainloop()