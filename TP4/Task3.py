from tkinter import * 
import random

def gridtab(l,pages):
    c=len(pages)
    index=0
    for ligne in range(l):
        for colonne in range(c+1):



            if(ligne==0 and colonne==0): #first button
               Button(
                        Mafenetre, 
                        text='/', 
                        borderwidth=1,
                        font=('times',14,'bold'),
                        width=5,
                        bg='gray'
               ).grid(
                        row=ligne, 
                        column=colonne,
                        sticky=EW
                )  

            elif(ligne==0 and colonne!=0): # first line
                Button(Mafenetre, text=pages[index], borderwidth=1,font=('times',14,'bold'),width=5,bg="gray").grid(row=ligne, column=colonne,sticky=EW)

                #fill the l=pages list 
                listTM.insert(END,'NUM'+str(pages[index])) 
                index += 1


            elif (ligne!=0 and colonne==0): #first column
                Button(Mafenetre, text='line'+str(ligne), borderwidth=1,font=('times',14,'bold'),width=5,bg='gray').grid(row=ligne, column=colonne,sticky=EW)
            else:
                Button(Mafenetre, text='  ', borderwidth=1,font=('times',14,'bold'),width=5).grid(row=ligne, column=colonne,sticky=EW)



#fenetre
fenetre = Tk() 
fenetre.title("TP4")
fenetre.geometry('1400x700')

#grid frame
Mafenetre=Frame(fenetre)
Mafenetre.pack(pady=20)


pages=[random.randint(0,10) for i in range(10)]
lines = int(4)


listTM=Listbox(fenetre,height=10)

listTM.select_set(0)
listTM.place(x=500,y=250)


def PLACE ():
    ind=0
    ligne = 0
    colonne = 1
    for ind in range(10):
        Button(Mafenetre,text=pages[ind], borderwidth=1,font=('times',14,'bold'),width=5).grid(row=ligne+1, column=colonne)
        if ligne==3:
            ligne = -1
            colonne+=1
        ligne +=1

fifo=Button(fenetre,text='PLACE',command=PLACE ,width=10,bg='white',fg='blue')
fifo.config(font=('times',14,'bold'))
fifo.place(x=1000,y=300)





def LRU():
    pass
lru=Button(fenetre,text='LRU',command=LRU ,width=10,bg='white',fg='blue')
lru.config(font=('times',14,'bold'))
lru.place(x=1000,y=350)





def Optimal():
    pass
opt=Button(fenetre,text="Optimal",command=Optimal ,width=10,bg='white',fg='blue')
opt.config(font=('times',14,'bold'))
opt.place(x=1000,y=400)

def RST():
    global listTM
    global pages
    pages=[random.randint(0,10) for i in range(10)]
    listTM.delete(0,END)
    index = 0
    for ligne in range(lines):
        for colonne in range(len(pages)):
            Button(Mafenetre, text='  ', borderwidth=1,font=('times',14,'bold'),width=5).grid(row=ligne+1, column=colonne+1,sticky=EW)
        listTM.insert(END,'NUM'+str(pages[index])) 
        index += 1
    gridtab(lines+1,pages)

rst=Button(fenetre,text='RST',command=RST ,width=10,bg='white',fg='blue')
rst.config(font=('times',14,'bold'))
rst.place(x=1000,y=450)



gridtab(lines+1,pages)
fenetre.mainloop()         