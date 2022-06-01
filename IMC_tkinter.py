from tkinter import *


#criar janela

root = Tk()
root.grid_rowconfigure(0,  weight=0)
root.grid_columnconfigure(0, weight=1)


#geometria
root.geometry('380x250')

# Max e Min da Janela
root.minsize(width=400, height=200)
root.maxsize(width=600, height=200)


def imc():
   if in1.get().replace('.','',1).isdigit() and in2.get().replace('.','',1).isdigit():
      r = float(in2.get()) / (float(in1.get()) * float(in1.get()))

      if r < 18.5:
         lb3['text'] = 'Peso Baixo'

      if r > 18.5 and r < 24.9:
         lb3['text'] = 'Peso Normal'

      if r > 25.0 and r < 29.9:
         lb3['text'] = 'Sobrepeso'

      if r > 30.0 and r < 34.9:
         lb3['text'] = 'Obesidade 1'

      if r > 35.0 and r < 39.9:
         lb3['text'] = 'Obesidade 2'

      if r > 40.0:
         lb3['text'] = 'Obesidade Mórbida'
         
   else :
      lb3['text'] = 'Valor invalido'

#criar os widgets
lb1 = Label(root, text='Altura (m)')
in1 = Entry(root, font="Arial 26")
lb2 = Label(root, text='Peso (Kg)')
in2 = Entry(root, font="Arial 26")
bt1 = Button(root, text='IMC', command=imc)
lb3 = Label(root, text= "Status", font="Arial 16")

#organizar os widgets
lb1.grid(row=0, column=0, sticky=NSEW)
in1.grid(row=1, column=0, sticky=NSEW)

lb2.grid(row=2, column=0, sticky=NSEW)
in2.grid(row=3, column=0, sticky=NSEW)

bt1.grid(row=4, column=0, sticky=NSEW)

lb3.grid(row=5, column=0, sticky=NSEW)


#executar a janela
root.mainloop()