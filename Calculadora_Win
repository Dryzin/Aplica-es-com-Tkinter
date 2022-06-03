from tkinter import *


def entrada(valor):
    lb1["text"] += valor

def limpar():
    lb1["text"] = ""

def r ():
    x=eval(lb1['text'])
    lb1['text'] = str(x)


#criar janela
root = Tk()

#window
root.grid_rowconfigure(0,  weight=1)
#root.grid_rowconfigure(1,  weight=1)
root.grid_rowconfigure(2,  weight=1)
root.grid_rowconfigure(3,  weight=1)
root.grid_rowconfigure(4,  weight=1)
root.grid_rowconfigure(5,  weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

#geometria
root.geometry('220x400')

#janela.config(bg='')
root.minsize(width=300, height=100)
root.maxsize(width=600, height=600)


#criar os widgets

lb1 = Label(root, text='', font='Arial 18')
bt1 = Button(root, text='7', command= lambda: entrada('7'), activebackground= '#9E9CA6')
bt2 = Button(root, text='8',command= lambda: entrada('8'), activebackground= '#9E9CA6')
bt3 = Button(root, text='9',command= lambda: entrada('9'), activebackground= '#9E9CA6')
bt4 = Button(root, text='x',command= lambda: entrada('*'), activebackground= '#9E9CA6')
bt5 = Button(root, text='4',command= lambda: entrada('4'), activebackground= '#9E9CA6')
bt6 = Button(root, text='5',command= lambda: entrada('5'), activebackground= '#9E9CA6')
bt7 = Button(root, text='6',command= lambda: entrada('6'), activebackground= '#9E9CA6')
bt8 = Button(root, text='-',command= lambda: entrada('-'), activebackground= '#9E9CA6')
bt9 = Button(root, text='1',command= lambda: entrada('1'), activebackground= '#9E9CA6')
bt10 = Button(root, text='2',command= lambda: entrada('2'), activebackground= '#9E9CA6')
bt11 = Button(root, text='3',command= lambda: entrada('3'), activebackground= '#9E9CA6')
bt12 = Button(root, text='+',command= lambda: entrada('+'), activebackground= '#9E9CA6')
bt13 = Button(root, text='÷',command= lambda: entrada('/'), activebackground= '#9E9CA6')
bt14 = Button(root, text='0',command= lambda: entrada('0'), activebackground= '#9E9CA6')
bt15 = Button(root, text=',',command= lambda: entrada('.'), activebackground= '#9E9CA6')
bt16 = Button(root, text='C',command= limpar)
bt20 = Button(root, text='=',command= lambda: r())

#organizar os widgets

lb1.grid(row=0, column=0, columnspan= 5)

bt16.grid(row=1, column=0, sticky= NSEW)

bt1.grid(row=2, column=0, sticky= NSEW)
bt2.grid(row=2, column=1, sticky= NSEW)
bt3.grid(row=2, column=2, sticky= NSEW)
bt4.grid(row=2, column=3, sticky= NSEW)
bt5.grid(row=3, column=0, sticky= NSEW)
bt6.grid(row=3, column=1, sticky= NSEW)
bt7.grid(row=3, column=2, sticky= NSEW)
bt8.grid(row=3, column=3, sticky= NSEW)
bt9.grid(row=4, column=0, sticky= NSEW)
bt10.grid(row=4, column=1, sticky= NSEW)
bt11.grid(row=4, column=2, sticky= NSEW)
bt12.grid(row=4, column=3, sticky= NSEW)
bt20.grid(row=5, column=2, sticky= NSEW)
bt13.grid(row=5, column=3, sticky= NSEW)
bt14.grid(row=5, column=1, sticky= NSEW)
bt15.grid(row=5, column=0, sticky= NSEW)

#executar a janela
root.mainloop()