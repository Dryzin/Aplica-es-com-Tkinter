from tkinter import *

def somar():
    if in1.get().isnumeric() and in2.get().isnumeric():
        lb2['text'] = (int(in1.get()) + int(in2.get()))
    else:
        lb2['text']= 'Valor invalido'

#window
janela = Tk()

#geometria
janela.geometry('400x300+500+500')

#janela.config(bg='')
janela.minsize(width=400, height=180)
janela.maxsize(width=600, height=600)

#widgets
lb1 =Label(janela, text='Calculadora', font='Arial 26')
in1 = Entry(janela, font="Arial 26")
in2 = Entry(janela, font="Arial 26")
bt2 = Button(janela, text="Somar", font="Arial 26", command=somar)
lb3 =Label(janela, text='Resultado', font='Arial 26')
lb2 =Label(janela, text='', font='Arial 26')


#layout
lb1.pack()
in1.pack()
in2.pack()
bt2.pack()
lb3.pack()
lb2.pack()

#run
janela.mainloop()