from Tkinter import *
fen.Tk()
fen.configure(width="400", height="700", bg="cyan")
toile=Canvas(fen, width="300", height="400", bg="red")
toile.pack()
rectangle = toile.create_rectangle(200, 200, 500, 500, fill="yellow")
arc = toile.create_arc(100, 100, 500, 500, fill="green")
