from tkinter import *

#window
root = Tk()
root.grid_rowconfigure(0,  weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.bind('-', lambda event: dn())
root.bind('+', lambda event: somar())

#geometria
root.geometry('400x180')

#janela.config(bg='')
root.minsize(width=400, height=180)
root.maxsize(width=400, height=180)



def somar():
    if lb1['text'] < 10:
        lb1['text'] = lb1['text']+1


def dn():
    if lb1['text'] > -10:
        lb1['text'] = lb1['text']-1


#widgets
bt1 = Button(root, text='-', font='Arial 24',command=dn)
lb1 = Label(root, text=0, font='Arial 24')
bt2 = Button(root, text='+', font='Arial 24', command=somar)


#layout
bt1.grid(row=0, column=0, sticky=NSEW)

bt2.grid(row=0, column=2, sticky=NSEW)

lb1.grid(row=0, column=1, sticky=NSEW)

#run
root.mainloop()