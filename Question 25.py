from Tkinter import *
import time
fen.Tk()
fen.configure(width="600", height="600", bg="blue")
toile=Canvas(fen, width="500", height="500", bg="blue")
balle = toile.create_oval(0,0,30,30, fill="green")
x=50
y=50
while 1:
	toile.move(rec, x, y)
	pos=toile.coords(balle)
	if pos[2]>=600
		x=-x
	if pos[3]>=600
		y=-y
	time.sleep(0.1)
	toile.update()
fen.mainloop()
