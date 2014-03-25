"""
from Tkinter import *

# create window
root = Tk()

# modify window
root.title("Add Binding")
root.geometry("1000x1000")

# make text string

label = Label(root, text="Message")
label.grid(row=1)

# make text entry box
name_box = Entry(root)
name_box.grid(row=1)

code_box = Entry(root)
code_box.pack()
code_box.focus_set()

def callback():
    print name_box.get()
    print code_box.get()

b = Button(root, text="get", width=10, command=callback)
b.pack()

# run the event loop
root.mainloop()
"""

# Example: File: grid-example-1.py

from Tkinter import *

root = Tk()

w = Label(root, text="Message")
w.grid(sticky=E)
w = Label(root, text="Subtractive:")
w.grid(sticky=E)

w = Label(root, text="Cyan", bg="cyan", height=2)
w.grid(row=1, column=1)
w = Label(root, text="Magenta", bg="magenta", fg="white")
w.grid(row=1, column=2)
w = Label(root, text="Yellow", bg="yellow", height=2)
w.grid(row=1, column=3)

w = Label(root, text="Red", bg="red", fg="white", height=2)
w.grid(row=0, column=1)
w = Label(root, text="Green", bg="green", height=3)
w.grid(row=0, column=2)
w = Label(root, text="Blue", bg="blue", fg="white")
w.grid(row=0, column=3)

mainloop()
