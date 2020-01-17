from Tkinter import *
fen.Tk()
fen.title("Alerte!")
fen.configure(width=400,height=400,background=white)
message=Label(fen, text="Cliquer sur le bouton pour fermer la fenetre")
bou=Bouton(fen,text="Fermer", bg="bleu", fg="black", command=fen.destroy)
bou.pack()
