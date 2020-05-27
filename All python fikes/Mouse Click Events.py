from tkinter import *

root = Tk()

def Left(event):
    print("Left")
def Middle(event):
    print("Middle")
def Right(event):
    print("Right")

frame = Frame(root, width=300, height=300)
frame.bind("<Button-1>", Left)
frame.bind("<Button-3>", Right)
frame.bind("<Button-2>", Middle)

frame.pack()

root.mainloop()