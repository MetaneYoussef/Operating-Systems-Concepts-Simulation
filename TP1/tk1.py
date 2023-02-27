from tkinter import *

from matplotlib.pyplot import text
fenetre = Tk()

def DitBonjour():
    texte.place(x=0,y=60)

texte = Label(fenetre,text = 'Bonjour !')

Bouton = Button(fenetre,text='Cliquer',command=DitBonjour)

Bouton.place(x=0,y=0)

fenetre.mainloop()