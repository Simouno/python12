from Tkinter import *
fen.Tk()
fen.configure(width="400", height="700", bg="cyan")
toile=Canvas(fen, width="300", height="400", bg="blue")
toile.pack()
toile.create_rectangle(width="200", height="500")
toile.create_arc(width="100", height="400")
