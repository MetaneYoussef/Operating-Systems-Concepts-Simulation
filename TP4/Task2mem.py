from tkinter import * 
import random

def gridtab(l,pages):
    c=len(pages)
    index=0

    # -------------------------------------------------------- 
    # FILL THE LIST OF PAGES
    # -------------------------------------------------------- 
    for i in range(c):
        listTM.insert(END,'PAGE'+str(pages[i]))


    # -------------------------------------------------------- 
    # FILL THE GRID
    # -------------------------------------------------------- 
    for ligne in range(l):
        
        for colonne in range(c+1):
            
            if(ligne==0 and colonne==0): 
                # -------------------------------------------------------- 
                # FIRST BUTTON
                # -------------------------------------------------------- 
               Button(Mafenetre, text='/', borderwidth=1,font=('times',14,'bold'),width=5,bg='gray').grid(row=ligne, column=colonne,sticky=EW) 
            
            elif(ligne==0 and colonne!=0): 
                # -------------------------------------------------------- 
                # FIRST LINE
                # -------------------------------------------------------- 
                Button(Mafenetre, text="T "+ str(index), borderwidth=1,font=('times',14,'bold'),width=7,bg="gray").grid(row=ligne, column=colonne,sticky=EW)
                index += 1

            elif (ligne!=0 and colonne==0):
                # -------------------------------------------------------- 
                # FIRST COLUMN
                # --------------------------------------------------------  
                Button(Mafenetre, text='Frame '+str(ligne), borderwidth=1,font=('times',14,'bold'),width=7,bg='gray').grid(row=ligne, column=colonne,sticky=EW)
            
            else:
                # -------------------------------------------------------- 
                # THE REST 
                # --------------------------------------------------------  
                Button(Mafenetre, text='  ', borderwidth=1,font=('times',14,'bold'),width=5).grid(row=ligne, column=colonne,sticky=EW)



# -------------------------------------------------------- 
# MAIN WINDOW
# -------------------------------------------------------- 
fenetre = Tk() 
fenetre.title("TP4")
fenetre.geometry('1400x700')

# -------------------------------------------------------- 
# FRAME OF THE GRID
# -------------------------------------------------------- 
Mafenetre=Frame(fenetre)
Mafenetre.pack(pady=20)


# -------------------------------------------------------- 
# LIST OF PAGES
# -------------------------------------------------------- 
pages=[random.randint(0,9) for i in range(10)]
lines = int(4)
listTM=Listbox(fenetre,height=10)
listTM.select_set(0)
listTM.place(x=500,y=250)

# -------------------------------------------------------- 
# PLACE PAGES IN MEMORY
# -------------------------------------------------------- 
def place_column(frames,temps,NB2COL):# page to be colored (THE CHANGED ONE) (-1 to color all the frames)
    index = 1
    color = 'pink'
    if NB2COL == -1 :
        color = 'red'
    for frame in frames :
        if index == NB2COL:
            Button(Mafenetre, text='Page '+str(frame), borderwidth=1,font=('times',14,'bold'),width=7,bg='red').grid(
            row=index, column=temps,sticky=EW)
        else:
            Button(Mafenetre, text='Page '+str(frame), borderwidth=1,font=('times',14,'bold'),width=7,bg=color).grid(
            row=index, column=temps,sticky=EW)
        index += 1 

# -------------------------------------------------------- 
# PICK THE FIRST 4 PAGES
# -------------------------------------------------------- 
def pick_f(pages):
    frames = []
    i = 0
    while(len(frames)<4):
        if pages[i] in frames :
            i += 1
        else:
            frames.append(pages[i])
            i += 1
    return frames,i
        
# -------------------------------------------------------- 
# FIFO BUTTON AND FUNCTION
# -------------------------------------------------------- 
def FIFO ():
    temps = 1 
    index = 0
    DF = 4
    frames,i = pick_f(pages)
    place_column(frames,temps,-1)
    temps += 1
    for page in pages[i:]:
        if not(page in frames): #page has to be loaded
            frames[index] = page
            place_column(frames,temps,index+1) # page to be colored (THE CHANGED ONE)
            temps += 1
            index += 1 
            DF += 1 
            if index == 4:
                index = 0
        else : 
            place_column(frames,temps,0)
            temps += 1
    txt1.config(text="Le nombre des defaults de page est : "+str(DF))
    txt1.place(x=500,y=450)
             
            
        
            

fifo=Button(fenetre,text='FIFO',command=FIFO ,width=10,bg='white',fg='blue')
fifo.config(font=('times',14,'bold'))
fifo.place(x=1000,y=300)


# -------------------------------------------------------- 
# LRU BUTTON AND FUNCTION
# -------------------------------------------------------- 

def lru_choice(memory,pages):
    max=len(pages)
    for MI,i in enumerate(memory):
        index=len(pages) - pages[::-1].index(i) - 1
        if (index<max):
            max=index
            lruIndex= MI  
    return lruIndex





def LRU():
    temps = 1 
    DF = 4
    frames,i = pick_f(pages)
    place_column(frames,temps,-1)
    temps += 1
    for page in pages[i:]:
        if not(page in frames): #page has to be loaded
            chosen_frame_index =lru_choice(frames,pages[:i+temps-1])
            frames[chosen_frame_index] = page
            place_column(frames,temps,chosen_frame_index+1)
            temps += 1
            DF += 1 
        else : 
            place_column(frames,temps,0)
            temps += 1
    txt1.config(text="Le nombre des defaults de page est : "+str(DF))
    txt1.place(x=500,y=450)
lru=Button(fenetre,text='LRU',command=LRU ,width=10,bg='white',fg='blue')
lru.config(font=('times',14,'bold'))
lru.place(x=1000,y=350)


# -------------------------------------------------------- 
# OPTIMAL BUTTON AND FUNCTION
# -------------------------------------------------------- 

def optimal_choice(frames,pages):
    """if innocent != -3:

        pages.remove(frames[innocent])

    count = [0,0,0,0]
    #        | | | | 
    #frame= [1,2,3,4]
    offset = 0
    for i in range(len(frames)):
        for j in pages : 
            if frames[i] == j :
                count[i] += 1 
    indexed = min(count)
    index = count.index(indexed) + offset
    
    if len(pages)<=2:
        offset += 1
    
    return index"""
    min=0
    offset = 0
    for MI,i in enumerate(frames):
        try:
            index=pages.index(i)
        except:
            index=len(pages)+1
        if (index>min):
            min=index
            OptimalIndex= MI  
    if len(pages)<=1:
        offset += 1
    if len(pages)<=2:
        offset += 2
    return OptimalIndex+offset



def Optimal():
    temps = 1 
    DF = 4
    frames,i = pick_f(pages)
    place_column(frames,temps,-1)
    temps += 1
    for page in pages[i:]:
        if not(page in frames): #page has to be loaded
            chosen_frame_index = optimal_choice(frames,pages[i+temps:])
            frames[chosen_frame_index] = page
            place_column(frames,temps,chosen_frame_index+1)
            temps += 1
            DF += 1 
        else : 
            place_column(frames,temps,0)
            temps += 1
    txt1.config(text="Le nombre des defaults de page est : "+str(DF))
    txt1.place(x=500,y=450)

opt=Button(fenetre,text="Optimal",command=Optimal ,width=10,bg='white',fg='blue')
opt.config(font=('times',14,'bold'))
opt.place(x=1000,y=400)



# -------------------------------------------------------- 
# RESET EVERYTHING BUTTON AND FUNCTION
# -------------------------------------------------------- 
def RST():
    global listTM
    global pages
    txt1.place(x=3000,y=3000)
    # reload new random pages
    pages=[random.randint(0,9) for i in range(10)]
    listTM.delete(0,END)
    
    #empty the colmuns of the grid
    index = 0
    for ligne in range(lines):
        for colonne in range(len(pages)):
            Button(Mafenetre, text='  ', borderwidth=1,font=('times',14,'bold'),width=5).grid(row=ligne+1, column=colonne+1,sticky=EW)
        index += 1
    gridtab(lines+1,pages)

rst=Button(fenetre,text='RST',command=RST ,width=10,bg='white',fg='blue')
rst.config(font=('times',14,'bold'))
rst.place(x=1000,y=450)

txt1 = Label(fenetre,text="Le nombre des defaults de page est : ")
txt1.config(fg='red',font=('arial',16,'bold'),bg='pink')
txt1.place(x=3000,y=3000)
#generate the table for the first time
gridtab(lines+1,pages)
fenetre.mainloop()              