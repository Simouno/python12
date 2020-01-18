from Tkinter import *
import time
fen.Tk()
fen.configure(width="600", height="600", bg="blue")
toile=Canvas(fen, width="500", height="500", bg="blue")
balle = toile.create_oval(0,0,30,30, fill="red")
rec = toile.create_rectangle(0,0,560,560, fill="green")
x=50
y=50
x1=50
y2=50
while 1:
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
		x=-x
	if pos2[3]>=600
		y=-y
	time.sleep(0.1)
	toile.update()
fen.mainloop()
