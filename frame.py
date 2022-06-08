from tkinter import *

#criar janela

root = Tk()
fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)




root.grid_rowconfigure(0,  weight=1)
root.grid_rowconfigure(1,  weight=1)
root.grid_rowconfigure(2,  weight=1)
root.grid_rowconfigure(3,  weight=1)
root.grid_rowconfigure(4,  weight=1)
root.grid_rowconfigure(5,  weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

#---
fr1.grid_rowconfigure(0,  weight=1)
fr1.grid_rowconfigure(1,  weight=1)
fr1.grid_rowconfigure(2,  weight=1)
fr1.grid_rowconfigure(3,  weight=1)
fr1.grid_rowconfigure(4,  weight=1)
fr1.grid_rowconfigure(5,  weight=1)

fr1.grid_columnconfigure(0, weight=1)
fr1.grid_columnconfigure(1, weight=1)
fr1.grid_columnconfigure(2, weight=1)

#---
fr2.grid_rowconfigure(0,  weight=1)
fr2.grid_rowconfigure(1,  weight=1)
fr2.grid_rowconfigure(2,  weight=1)
fr2.grid_rowconfigure(3,  weight=1)
fr2.grid_rowconfigure(4,  weight=1)
fr2.grid_rowconfigure(5,  weight=1)

fr2.grid_columnconfigure(0, weight=1)
fr2.grid_columnconfigure(1, weight=1)
fr2.grid_columnconfigure(2, weight=1)

#---

fr3.grid_rowconfigure(0,  weight=1)
fr3.grid_rowconfigure(1,  weight=1)
fr3.grid_rowconfigure(2,  weight=1)
fr3.grid_rowconfigure(3,  weight=1)
fr3.grid_rowconfigure(4,  weight=1)
fr3.grid_rowconfigure(5,  weight=1)

fr3.grid_columnconfigure(0, weight=1)
fr3.grid_columnconfigure(1, weight=1)
fr3.grid_columnconfigure(2, weight=1)


#geometria
root.geometry('800x300')

#root.minsize(width=800, height=300)
#root.maxsize(width=1000, height=400)


#root.configure(background= "white")
root.title("Atividade Frame")

#criar os widgets

#---Frame 1---

lb1 = Label(fr1, text='Dados Pessoais', font="Calibri 20")

lb2 = Label(fr1, text='Nome:', font="Calibri 16")
in1 = Entry(fr1, font="Arial 16")

lb3 = Label(fr1, text='Telefone:', font="Calibri 16")
in2 = Entry(fr1, font="Arial 16")

lb4 = Label(fr1, text='CPF:', font="Calibri 16")
in3 = Entry(fr1, font="Arial 16")

lb5 = Label(fr1, text='Idade:', font="Calibri 16")
in4 = Entry(fr1, font="Arial 16")

#---Frame 2---

lb_1 = Label(fr2, text='Endereço', font="Calibri 20")

lb_2 = Label(fr2, text='Rua:', font="Calibri 16")
in_1 = Entry(fr2, font="Arial 16")

lb_3 = Label(fr2, text='Bairro:', font="Calibri 16")
in_2 = Entry(fr2, font="Arial 16")

lb_4 = Label(fr2, text='Cidade:', font="Calibri 16")
in_3 = Entry(fr2, font="Arial 16")

lb_5 = Label(fr2, text='Número:', font="Calibri 16")
in_4 = Entry(fr2, font="Arial 16")

#---Frame 3---

bt1 = Button(fr3, text="Salvar", font="Arial 16")
bt2 = Button(fr3, text="Limpar Dados", font="Arial 16")


#---Configuração do Frame---

fr1.grid(row=0, column=0)
fr2.grid(row=0, column=1, pady=46)
fr3.grid(row=1, column=0, sticky=EW)

#organizar os widgets

#---Frame 1---

lb1.grid(row=0, column=0, sticky=NSEW)

lb2.grid(row=2, column=0, sticky=NSEW)
in1.grid(row=2, column=1, sticky=NSEW)

lb3.grid(row=3, column=0, sticky=NSEW)
in2.grid(row=3, column=1, sticky=NSEW)

lb4.grid(row=4, column=0, sticky=NSEW)
in3.grid(row=4, column=1, sticky=NSEW)

lb5.grid(row=5, column=0, sticky=NSEW)
in4.grid(row=5, column=1, sticky=NSEW)

#---Frame 2---

lb_1.grid(row=0, column=1, sticky=NSEW)

lb_2.grid(row=2, column=1, sticky=NSEW)
in_1.grid(row=2, column=2, sticky=NSEW)

lb_3.grid(row=3, column=1, sticky=NSEW)
in_2.grid(row=3, column=2, sticky=NSEW)

lb_4.grid(row=4, column=1, sticky=NSEW)
in_3.grid(row=4, column=2, sticky=NSEW)

lb_5.grid(row=5, column=1, sticky=NSEW)
in_4.grid(row=5, column=2, sticky=NSEW)

#---Frame 3---

bt1.grid(row=1, column=0, sticky=NSEW)
bt2.grid(row=1, column=1, sticky=NSEW)


#executar a janela
root.mainloop()