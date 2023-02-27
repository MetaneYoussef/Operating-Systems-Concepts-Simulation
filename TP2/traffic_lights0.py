import time 
from tkinter import *
import threading

color = 'green'

def ignitegreen():
    global color
    myCanvas.itemconfig(green,fill="#1eff00")
    myCanvas.itemconfig(yellow,fill="#4b5200")
    myCanvas.itemconfig(red,fill="#610800")
    color = 'yellow' 
    
def igniteyellow():
    global color
    myCanvas.itemconfig(green,fill="#0a5200")
    myCanvas.itemconfig(yellow,fill="#eaff00")
    myCanvas.itemconfig(red,fill="#610800")
    color='red'

def ignitered():
    global color
    myCanvas.itemconfig(green,fill="#0a5200")
    myCanvas.itemconfig(yellow,fill="#4b5200")
    myCanvas.itemconfig(red,fill="#ff1500")
    color='green'



#fenetre
fenetre=Tk()
fenetre.title("Traffic lights")
fenetre.configure(width=700,height=500)
fenetre.configure(bg='white')


#title
titre=Label(fenetre,text='Timer',fg='Blue',bg='white')
titre.config(font=('times',30,'bold'))
titre.place(x=300,y=30)


#traffic lights
myCanvas=Canvas(fenetre,width=200,height=250,bg="white")
myCanvas.place(x=350,y=150)
green=myCanvas.create_oval(110,10,170,70,width=3,fill='#0a5200')
myCanvas.create_rectangle(100,5,180,80,width=3)
yellow=myCanvas.create_oval(110,90,170,150,width=3,fill='#4b5200')
myCanvas.create_rectangle(100,80,180,160,width=3)
red=myCanvas.create_oval(110,170,170,230,width=3,fill='#610800')
myCanvas.create_rectangle(100,160,180,240,width=3)
titre=Label(fenetre,text='Selectionner un temps !',fg='red',bg='white')
titre.config(font=('times',12,'bold'))


def lancer():
    ignitegreen()
    Timer = threading.Timer(5,tester)
    Timer.start()
    btn3.place_forget()

    btn1.place(x=600,y=200)


#boutton_test
btn3 = Button(fenetre, text="lancer")
btn3.configure(background='white',font=('arial',18,'bold'),command=lancer)
btn3.place(x=600,y=200)




def tester():
    global color
    global timer
    if color !='':
        if color=='green':
            ignitegreen()
        elif color=='yellow':
            igniteyellow()
        elif color=='red' :
            ignitered()
        timer = threading.Timer(int(listTM.get(ACTIVE)),tester)
        timer.start()
    else :
        color='green'

#boutton_test
btn1 = Button(fenetre, text="test")
btn1.configure(background='white',font=('arial',18,'bold'),command=tester)



"""
#btn1.place(x=600,y=200)


# def tester():
#     global color
#     global timer
#     try:
#         time = int(listTM.get(listTM.curselection()))
#     except TclError:
#         titre.place(x=250,y=450)
#     else:
#         titre.place(x=1000,y=1000)
        
#         timer = threading.Timer(time,tester)
#         timer.start()
#         if color == 'green':
#             ignitegreen()
#         elif color == 'yellow':
#             igniteyellow()
#         elif color == 'red':
#             ignitered()
"""

def quit():
    global color
    global timer
    timer.cancel()
    #turnoff
    myCanvas.itemconfig(green,fill="#0a5200")   
    myCanvas.itemconfig(yellow,fill="#4b5200")
    myCanvas.itemconfig(red,fill="#610800")
    color = 'green'

#boutton_quit
btn2 = Button(fenetre, text="quitter",command=quit)
btn2.place(x=600,y=280)
btn2.configure(background='white',font=('arial',18,'bold'))







listTM=Listbox(fenetre)
listTM.insert(1,'5')
listTM.insert(2,'25')
listTM.insert(3,'50')
listTM.insert(4,'75')
listTM.insert(5,'100')
listTM.insert(6,'150')
listTM.insert(7,'200')
listTM.insert(8,'250')
listTM.insert(9,'300')
listTM.select_set(0)
listTM.place(x=100,y=250)

fenetre.mainloop()