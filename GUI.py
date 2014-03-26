from Tkinter import *

class FunctionWindow():
    def __init__(self):
        self.root = Tk()
        self.ctrl_key = StringVar()
        self.ctrl_key.set(0)
        self.shift_key = StringVar()
        self.shift_key.set(0)

        # function input
        self.func_label = Label(self.root, text="Function Name:")
        self.func_label.grid(sticky=E)
        self.func_input = Entry(self.root)
        self.func_input.grid(row=0, column=1, sticky=W)

        # code input
        self.code_label = Label(self.root, text="Code:")
        self.code_label.grid(sticky=E)
        self.code_input = Text(self.root)
        self.code_input.insert(INSERT, "")
        self.code_input.grid(row=1, column=1)

        # binding options
        ctrl = Checkbutton(self.root, text="ctrl", variable=self.ctrl_key,
                        onvalue="ctrl")
        ctrl.grid(row=4)
        shift = Checkbutton(self.root, text="shift", variable=self.shift_key,
                            onvalue="shift")
        shift.grid(row=5)
        self.bind_label = Label(self.root, text="Bind to key:")
        self.bind_label.grid(sticky=E)
        self.bind_input = Entry(self.root, width=1)
        self.bind_input.grid(row=6, column=1, sticky=W)

        b = Button(self.root, text="get", width=10, command=self.callback)
        b.grid(row=2, column=1)

    def callback(self):
        print self.func_input.get()
        print self.code_input.get(1.0, END).rstrip("\n")
        if self.ctrl_key.get() != "0": print self.ctrl_key.get()
        if self.shift_key.get() != "0": print self.shift_key.get()
        print self.bind_input.get()

    def popup(self):
        mainloop()

if __name__ == "__main__":
    fw = FunctionWindow()
    fw.popup()
