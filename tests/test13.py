from tkinter import *
root = Tk()
root.title('Ocean Shield')
root.geometry("1200x800")

text = Text(root)
text.pack(side="left")
sb = Scrollbar(root, command=text.yview)
sb.pack(side="right")
text.configure(yscrollcommand=sb.set)
...
for i in range(100):
    button = Button(text = "test")
    text.window_create("end", window=button)
    text.insert("end", "\n")
text.configure(state="disabled")



mainloop()
