from Tkinter import *
import time
fen.Tk()
fen.configure(width="600", height="600", bg="blue")
toile=Canvas(fen, width="500", height="500", bg="blue")
bou1=Bouton(fen,text="Fermer la fenetre", bg="black", fg="yellow",command=fen.destroy)
balle = toile.create_oval(0,0,30,30, fill="red")
rec = toile.create_rectangle(0,0,560,560, fill="green")
rec2 = toile.create_rectangle(0,0,560,460, fill="red")
def initilise():
	x=50
	y=50
	x1=50
	y1=50
	x2=50
	y2=50
	move=1
initilise()
while move=1:
  #balle
	toile.move(balle, x, y)
	pos1=toile.coords(balle)
	if pos1[2]>=600
		x=-x
	if pos1[3]>=600
		y=-y
  #Rectangle
  toile.move(rec, x, y)
  pos2=toile.coords(rec)
	if pos2[2]>=600
		x1=-x1
	if pos2[3]>=600
		y1=-y1
	time.sleep(0.1)
	toile.update()
  #Rectangle2
  toile.move(rec2, x, y)
  pos3=toile.coords(rec)
	if pos3[2]>=600
		x2=-x2
	if pos3[3]>=600
		y2=-y2
	time.sleep(0.1)
	toile.update()
fen.mainloop()
