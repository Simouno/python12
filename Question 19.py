from Tkinter import *
fen.Tk()
fen.configure(width="600", height="600", bg="black")
toile=Canvas(fen, width="500", height="500", bg="red")
toile.pack()
arc1 = toile.create_arc(300,300,300,300, fill="blue")
arc2 = toile.create_arc(250,250,250,250, fill="black")
arc3 = toile.create_arc(200,200,200,200, fill="blue")
arc4 = toile.create_arc(100,100,100,100, fill="black")
fen.mainloop()
