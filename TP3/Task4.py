import threading 
from tkinter import *
import time

fenetre = Tk()
fenetre.configure(width=600,height=400)
fenetre.configure(bg='white')
myCanvas=Canvas(fenetre,width=600,height=700,bg="#91a3bd")
myCanvas.place(x=0,y=0)

global x 
global y 
x = -50
y = -50
def draw(lock):
    global myCanvas
    global x
    global y

    lock.acquire()  
    x = x + 50
    if x % 600 == 0:
        x = 0
        y = y + 50
    if y == 400:
        lock.release()  
        exit(1) 
    if threading.current_thread().name == "t1":
        myCanvas.create_oval(x,y,x+50,y+50,fill="red")
    if threading.current_thread().name == "t2":
        myCanvas.create_oval(x,y,x+50,y+50,fill="yellow")
    if threading.current_thread().name == "t3":
        myCanvas.create_oval(x,y,x+50,y+50,fill="blue")
    
    lock.release()

    
    if threading.current_thread().name == "t1":
        time.sleep(0.25)
        draw(lock)
    if threading.current_thread().name == "t2":
        time.sleep(0.75)
        draw(lock)
    if threading.current_thread().name == "t3":
        time.sleep(0.5)
        draw(lock)

if __name__=="__main__":
    # creating a lock      
    lock = threading.Lock()  
    # creating threads      
    t1 = threading.Thread(target=draw,name='t1', args=(lock,))      
    t2 = threading.Thread(target=draw,name='t2',args=(lock,))  
    t3 = threading.Thread(target=draw,name='t3', args=(lock,))  
    # start threads      
    t1.start()      
    t2.start()
    t3.start()  

fenetre.mainloop()