from Tkinter import *
import time
fen.Tk()
fen.configure(width="600", height="600", bg="blue")
toile=Canvas(fen, width="500", height="500", bg="blue")
rec = toile.create_rectangle(0,100,0,30, fill="green")
while 1:
	toile.move(rec, 100, 0)
	pos=toile.coords(rec))
	if pos[1]>=0
		toile.move(rec, 100, 0)
	if pos[1]<=0
		toile.move(rec, -100, 0)
	time.sleep(0.25)
	toile.update()
fen.mainloop()
