from tkinter import *
# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title("grille widget")
for ligne in range(5):
    for colonne in range(5):
        Button(Mafenetre, text='L%s-C%s' % (ligne, colonne),borderwidth=1).grid(row=ligne, column=colonne)
Mafenetre.mainloop()