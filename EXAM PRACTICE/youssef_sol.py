from tkinter import *
import random
import threading

# -------------------------------------------------------- 
# MAIN WINDOW
# -------------------------------------------------------- 
Mafenetre = Tk()
Mafenetre.geometry('700x500')
Mafenetre.title("SCHEDULING ALGORITHME")
Mafenetre.configure(bg='white')


# -------------------------------------------------------- 
# Canvas
# -------------------------------------------------------- 
myCanvas=Canvas(Mafenetre,width=700,height=500,bg="white")
myCanvas.place(x=0,y=0)

# -------------------------------------------------------- 
# Recantagles
# -------------------------------------------------------- 
green = myCanvas.create_rectangle(100,80,180,160,width=3,fill='#0a5200')
yellow = myCanvas.create_rectangle(200,80,280,160,width=3,fill='#4b5200')
red = myCanvas.create_rectangle(300,80,380,160,width=3,fill='#610800')
blue  = myCanvas.create_rectangle(400,80,480,160,width=3,fill='#002E6D')
white = myCanvas.create_rectangle(500,80,580,160,width=3,fill='#7D7879')


# -------------------------------------------------------- 
# QUANTUM
# -------------------------------------------------------- 
QG = Label(Mafenetre,text='Q VERT:',fg='black',background='white')
QG.place(x=110,y=180)
QY = Label(Mafenetre,text='Q JAUNE:',fg='black',background='white')
QY.place(x=210,y=180)
QR = Label(Mafenetre,text='Q ROUGE:',fg='black',background='white')
QR.place(x=310,y=180)
QB = Label(Mafenetre,text='Q BLEU:',fg='black',background='white')
QB.place(x=410,y=180)
QW = Label(Mafenetre,text='Q BLANC:',fg='black',background='white')
QW.place(x=510,y=180)

# -------------------------------------------------------- 
# LISTE DES PROCESSUS
# --------------------------------------------------------
PROC_LIST = {
    'VERT':{"pri":1024,"Tcpu":0,"val":0},
    'JAUNE':{"pri":110,"Tcpu":0,"val":0},
    'ROUGE':{"pri":3121,"Tcpu":0,"val":0},
    'BLEU':{"pri":335,"Tcpu":0,"val":0},
    'BLANC':{"pri":9548,"Tcpu":0,"val":0}
}
# -------------------------------------------------------- 
# FONCTION allumer le proc et ajouter le quantum
# -------------------------------------------------------- 
def ignite_proc_UI(new,old,q): 
    if old == 'VERT':
        myCanvas.itemconfig(green,fill="#0a5200")
    elif old == 'JAUNE':
        myCanvas.itemconfig(yellow,fill="#4b5200")
    elif old == 'ROUGE':
        myCanvas.itemconfig(red,fill="#610800")
    elif old == 'BLEU':
        myCanvas.itemconfig(blue,fill="#002E6D")
    elif old == 'BLANC':
        myCanvas.itemconfig(white,fill="#7D7879")

    if new == 'VERT':
        myCanvas.itemconfig(green,fill="#00FF61")
        QG.config(text='Q VERT: '+str(int(Q)))
    elif new == 'JAUNE':
        myCanvas.itemconfig(yellow,fill="#FFFF3F")
        QY.config(text='Q JAUNE: '+str(int(Q)))
    elif new == 'ROUGE':
        myCanvas.itemconfig(red,fill="#FF0000")
        QR.config(text='Q ROUGE:'+str(int(Q)))
    elif new == 'BLEU':
        myCanvas.itemconfig(blue,fill="#0000FF")
        QB.config(text='Q BLEU: '+str(int(Q)))
    elif new == 'BLANC':
        myCanvas.itemconfig(white,fill="#FFFFFF")
        QW.config(text='Q BLANC:'+str(int(Q)))
    
    

# -------------------------------------------------------- 
# FONCTION quantum
# -------------------------------------------------------- 
def intquantum():
    global Pelu
    global Q
    global sp
    PeluO = Pelu
    lp = ['VERT','JAUNE','ROUGE','BLEU','BLANC']
    Pelu = 'VERT'
    min = PROC_LIST[Pelu]['val']
    for i in lp[1:]:
        if PROC_LIST[i]['val'] < min:
            Pelu = i
            min = PROC_LIST[Pelu]['val']
        elif PROC_LIST[i]['val'] == min:
            if PROC_LIST[i]['pri'] > PROC_LIST[Pelu]['pri']:
                Pelu = i
                min = PROC_LIST[Pelu]['val']
                
    
    Q = 6*PROC_LIST[Pelu]['pri']/sp
    ignite_proc_UI(Pelu,PeluO,Q)
    timing = threading.Timer(1,timer)
    timing.start()

# -------------------------------------------------------- 
# FONCTION TIMER
# -------------------------------------------------------- 
def timer():
    global Q
    global timing
    PROC_LIST[Pelu]['Tcpu'] += 1
    PROC_LIST[Pelu]['val'] = PROC_LIST[Pelu]['Tcpu'] * 1024  /  PROC_LIST[Pelu]['pri']
    Q = Q-1
    if Q<=0:
        intquantum()
    else:
        timing = threading.Timer(1,timer)
        timing.start()

# -------------------------------------------------------- 
# BOUTON ET FONCTION LANCER
# -------------------------------------------------------- 
def lancer():
    global timing
    global Q
    global Pelu
    global sp
    #election du premier proc
    lp = ['VERT','JAUNE','ROUGE','BLEU','BLANC']
    Pelu = lp[random.randint(0,4)]

    #calcul du somme prio
    sp = 0
    for i in lp:
        sp += PROC_LIST[i]['pri']
    
    #calcul quantum
    Q = 6*PROC_LIST[Pelu]['pri']/sp

    ignite_proc_UI(Pelu,'',Q)

    timing = threading.Timer(1,timer)
    timing.start()

btn = Button(Mafenetre, text="lancer ")
btn.configure(background='white',font=('arial',14),command=lancer)
btn.place(x=300,y=300)


# -------------------------------------------------------- 
# BOUTON ARRETER
# -------------------------------------------------------- 


def arreter():
    global timing
    global Pelu
    global Q
    timing.cancel()
    print("timer stopped")
    ignite_proc_UI('',Pelu,Q)

btn = Button(Mafenetre, text="Arreter")
btn.configure(background='white',font=('arial',14),command=arreter)
btn.place(x=300,y=350)


# -------------------------------------------------------- 
# MAINLOOP
# -------------------------------------------------------- 
Mafenetre.mainloop()