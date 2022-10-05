from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

leftFrame = Frame(root)
rightFrame = Frame(root)
leftFrame.pack( side = LEFT )
rightFrame.pack( side = LEFT )

redbutton = Button(leftFrame, text="Red", fg="red")
redbutton.pack( side = LEFT)

rightFrame = Button(rightFrame, text="green", fg="green")
rightFrame.pack( side = LEFT )

root.mainloop()
