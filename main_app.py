from tkinter import *

class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.iconbitmap('C:/Users/Herr Salai/Desktop/Programation/Python/Python projects/Calculator using Tkinter/assets/cal.ico')
        app_width = 357
        app_height = 420
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        master.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        my_label = Label(root, text =f'Width:{screen_width} Height:{screen_height}')
        my_label.pack(pady=20)
        master.config(bg='black')
        master.resizable(False,False)

        self.equation=StringVar()
        self.entry_value=''
        Entry(width=17, bg='tomato', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)
    
        Button(width=11,height=4,text='(',relief='flat',bg="white",command=lambda:self.show('(')).place(x=0 ,y=50)
        Button(width=11,height=4,text=')',relief='flat',bg="white",command=lambda:self.show(')')).place(x=90 ,y=50)
        Button(width=11,height=4,text='%',relief='flat',bg="white",command=lambda:self.show('%')).place(x=180 ,y=50)
        Button(width=11,height=4,text='1',relief='flat',bg="white",command=lambda:self.show(1)).place(x=0 ,y=125)
        Button(width=11,height=4,text='2',relief='flat',bg="white",command=lambda:self.show(2)).place(x=90 ,y=125)
        Button(width=11,height=4,text='3',relief='flat',bg="white",command=lambda:self.show(3)).place(x=180 ,y=125)
        Button(width=11,height=4,text='4',relief='flat',bg="white",command=lambda:self.show(4)).place(x=0 ,y=200)
        Button(width=11,height=4,text='5',relief='flat',bg="white",command=lambda:self.show(5)).place(x=90 ,y=200)
        Button(width=11,height=4,text='6',relief='flat',bg="white",command=lambda:self.show(6)).place(x=180 ,y=200)
        Button(width=11,height=4,text='7',relief='flat',bg="white",command=lambda:self.show(7)).place(x=0 ,y=275)
        Button(width=11,height=4,text='8',relief='flat',bg="white",command=lambda:self.show(8)).place(x=90 ,y=275)
        Button(width=11,height=4,text='9',relief='flat',bg="white",command=lambda:self.show(9)).place(x=180 ,y=275)
        Button(width=11,height=4,text='0',relief='flat',bg="white",command=lambda:self.show(0)).place(x=90 ,y=350)
        Button(width=11,height=4,text='.',relief='flat',bg="white",command=lambda:self.show('.')).place(x=180 ,y=350)
        Button(width=11,height=4,text='+',relief='flat',bg="white",command=lambda:self.show('+')).place(x=270 ,y=275)
        Button(width=11,height=4,text='-',relief='flat',bg="white",command=lambda:self.show('-')).place(x=270 ,y=200)
        Button(width=11,height=4,text='/',relief='flat',bg="white",command=lambda:self.show('/')).place(x=270 ,y=50)
        Button(width=11,height=4,text='*',relief='flat',bg="white",command=lambda:self.show('*')).place(x=270 ,y=125)
        Button(width=11,height=4,text='=',relief='flat',bg="lightblue",command=self.solve).place(x=270 ,y=350)
        Button(width=11,height=4,text='C',relief='flat',command=self.clear).place(x=0 ,y=350)

    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
    
    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)

root=Tk()
calculator=Calculator(root)
root.mainloop()