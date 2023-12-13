form tkinter import TK, Entry, Butto, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation=StringVar()
        self

root=TK()
root.mainloop()