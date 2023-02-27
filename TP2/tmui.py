from tkinter import *  
import tm
def update_label():
    result = tm.update_time()
    label1.config(text=result)

fenetre = Tk()
fenetre.configure(width=600,height=300)
fenetre.configure(bg='white')

# Create a label
label1 = Label(fenetre, text=tm.update_time(),bg='white')
label1.config(fg='red',font=('times',20,'bold'))
label1.place(x=225,y=100)

# Create a button
btn = Button(fenetre, text="Update", command=update_label)
btn.place(x=250,y=200)
# loop
fenetre.mainloop()