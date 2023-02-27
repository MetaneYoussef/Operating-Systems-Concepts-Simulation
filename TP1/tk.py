from distutils.command.config import config
from tkinter import *
fenetre = Tk()

fenetre.title('Ma prenmiere fenetre !')
fenetre.configure(width=600,height=600)
fenetre.configure(bg='white')
txt1 = Label(fenetre, text='Bonjour a tous !')
txt1.place(x=0,y=0)
txt1.config(fg='red',font=('times',20,'bold'))
txt1.config(text='Bas')
btn1= Button(fenetre,text='Clicker')
btn1.place(x=200,y=200)
btn1.configure(text='OK')

fenetre.mainloop()