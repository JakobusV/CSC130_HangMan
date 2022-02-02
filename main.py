import tkinter as tk
from graphics import *
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
width -= width/9
height -= height/6

def main():
    root = tk.Tk()

    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen',True)

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(root)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(root)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(root)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(root)

    label = Text(Point(100, 120), 'A face')
    label.draw(root)

    message = Text(Point(root.getWidth()/2, 20), 'Hangman')
    message.draw(root)
    while(True):
        root.getMouse()
    #win.close()

main()