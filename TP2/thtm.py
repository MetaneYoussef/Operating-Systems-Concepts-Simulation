import threading 
from tkinter import *
def horloge():
    timer=threading.Timer(5.0,horloge)



def cancel_timer():
    timer.cancel()

fenetre = Tk()
fenetre.configure(width=600,height=300)
fenetre.configure(bg='white')
timer=threading.Timer(5.0,horloge)
timer.start()

# Create a button
btn = Button(fenetre, text="Update", command=cancel_timer)
btn.place(x=250,y=200)

# loop
fenetre.mainloop()