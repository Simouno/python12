from Tkinter import *
fen.Tk()
fen.title("Fermer cetter fenetre")
fen.configure(width=500,hight=500,background=white)
bou=Bouton(fen,text="Fermer la fenetre", bg="black", fg="yellow",command=fen.destroy)
bou.pack()


