from tkinter import *
import random
from time import sleep
import threading

# -------------------------------------------------------- 
# MAIN WINDOW
# -------------------------------------------------------- 
Mafenetre = Tk()
Mafenetre.geometry('700x500')
Mafenetre.title("Hard disk Manager Simulation")




# -------------------------------------------------------- 
# The List
# -------------------------------------------------------- 
#THE VALUES
global vals
vals=[random.randint(0,99) for i in range(20)]

#THE LIST BOX
listTM=Listbox(Mafenetre,height=20,width=5)
listTM.select_set(0)
listTM.place(y=10,x=50)
for i in range(len(vals)):
    listTM.insert(END,str(vals[i]))


# -------------------------------------------------------- 
# The value
# -------------------------------------------------------- 
Valeur = StringVar()
Valeur.set(50)


# -------------------------------------------------------- 
# UPDATE The Scale TRIGGER FUNCTION
# -------------------------------------------------------- 
def maj(nouvelleValeur):
    print(nouvelleValeur)


# -------------------------------------------------------- 
# The Scale
# -------------------------------------------------------- 
echelle = Scale(Mafenetre,from_=0,to=100,resolution=10,orient=HORIZONTAL,
length=500,width=20,label="Offset",tickinterval=10,variable=Valeur,command=maj)
echelle.place(y=400,x=100)



# -------------------------------------------------------- 
# FIFO BUTTON AND FUNCTION
# -------------------------------------------------------- 
global F_index
F_index = 0

def FIFO():
    global Valeur
    global F_index
    global timer
    if (F_index > len(vals)-1):
        F_index = 0
        return
    Valeur.set(vals[F_index])
    POS.config(text=str(vals[F_index]))
    F_index += 1
    timer = threading.Timer(0.5,FIFO)
    timer.start()
    

fifo=Button(Mafenetre,text='FIFO',command=FIFO ,width=10,bg='pink',fg='black')
fifo.place(x=400,y=100)



# -------------------------------------------------------- 
# ASCENCEUR BUTTON AND FUNCTION
# -------------------------------------------------------- 
def init():
    global sens
    global vals
    global right_list
    global left_list
    global Valeur
    global F_index
    global list
    F_index = 0
    sorted = vals
    sorted.sort()
    for i in range(len(sorted)):
        if sorted[i] >= int(Valeur.get()):
            break

    right_list = sorted[:i]
    right_list = right_list[::-1]
    left_list = sorted[i:]
    list = []

    if sens.get() == 1 : #Direction droite
        list = right_list + left_list
    if sens.get() == 2 : #Direction gauche
        list = left_list + right_list

    ASC()


def ASC():
    global sens
    global Valeur
    global F_index
    global list
    global timer
    if (F_index >= len(list)):
        F_index = 0
        return
    Valeur.set(list[F_index])
    POS.config(text=str(list[F_index]))
    F_index += 1
    timer = threading.Timer(0.5,ASC)
    timer.start()
    

asc=Button(Mafenetre,text='ASCENSEUR',command=init ,width=10,bg='pink',fg='black')
asc.place(x=400,y=150)


# -------------------------------------------------------- 
# RESET BUTTON AND FUNCTION
# -------------------------------------------------------- 
def RESET():
    global vals
    global timer
    vals=[random.randint(0,99) for i in range(20)]
    timer.cancel()
    listTM.delete(0,END)
    Valeur.set(50)
    POS.config(text="")
    for i in range(len(vals)):
        listTM.insert(END,str(vals[i]))





reset=Button(Mafenetre,text='RESET',command=RESET,width=10,bg='pink',fg='black')
reset.place(x=400,y=200)

# -------------------------------------------------------- 
# POSITION LABEL
# -------------------------------------------------------- 
position=Label(Mafenetre,text='Position courante')
position.place(x=370,y=360)

POS=Label(Mafenetre,text='')
POS.place(x=500,y=360)

# -------------------------------------------------------- 
# DROITE ET GAUCHE BUTTON AND VALUE
# -------------------------------------------------------- 
sens = IntVar()
FS=LabelFrame(Mafenetre,text="Sens")
RD = Radiobutton(FS, text="Droite ", variable=sens, value=1)
RD.select()
RD.pack()
RG = Radiobutton(FS, text="Gauche", variable=sens, value=2)
RG.pack()
FS.place(x=400,y=280)

Mafenetre.mainloop()