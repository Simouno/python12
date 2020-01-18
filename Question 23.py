from Tkinter import *
import time
fen.Tk()
fen.geometry("600x600")
toile=Canvas(fen, width="500", height=="500", bg="black")
toile.pack
balle.toile.create_oval(0,0,100,100, fill="white")
bouge1=1
while bouge==1:
	toile.move(50,50)
	time.sleep(0.5)
	toile.update()
fen.mainloop()
balle2.toile.create_oval(300,300,100,100, fill="white")

balle3.toile.create_oval(500,0,100,100, fill="white")
bouge2=1
while bouge==1:
	toile.move(-50,-50)
	time.sleep(0.5)
	toile.update()
fen.mainloop()
