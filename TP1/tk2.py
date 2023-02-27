from tkinter import *

from setuptools import Command

fenetre = Tk()


def SayBoom():
    txt1.place(x=650,y=300)
    btn1.place(x=600,y=300)
    txt2.place(x=150,y=15)
    btn2.place(x=530,y=125)
def revert():
    txt2.place(x=600,y=600)
    btn2.place(x=600,y=600)
    txt1.place(x=10,y=10)
    btn1.place(x=230,y=75)


fenetre.title('Attention DANGER !')
fenetre.configure(width=600,height=150,bg='pink')
txt1 = Label(fenetre,text='Ne surtout pas appuyer sur le bouton ...')
txt1.config(fg='red',font=('arial',20,'bold'),bg='pink')
txt2 = Label(fenetre,text='BOOM !!')
txt2.config(font=('arial',70,'bold'),bg='pink')
btn1 = Button(fenetre,text='Bouton',padx=2,pady=2,command=SayBoom)
btn1.configure(background='red',font=('arial',20,'bold'))
btn2 = Button(fenetre,text='Desamocer',command=revert)
btn2.configure(background='green')
txt1.place(x=10,y=10)
btn1.place(x=230,y=75)

    
    




fenetre.mainloop()