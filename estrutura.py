from tkinter import *

#criar janela

root = Tk()
root.grid_rowconfigure(0,  weight=1)
root.grid_rowconfigure(1,  weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


#criar os widgets

bt1 = Button(root, text='Bt1')
bt2 = Button(root, text='Bt2')
lb1 = Label(root, text='Lb1')
bt3 = Button(root, text='Bt3')


#organizar os widgets

bt1.grid(row=0, column=0, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)
lb1.grid(row=0, column=1, sticky=NSEW)
bt3.grid(row=1, column=0, columnspan=3, sticky=NSEW)


#executar a janela
root.mainloop()