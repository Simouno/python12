from Tkinter import *
fen.Tk()
fen.configure(width="500", hight="500")
bou1=Button(fen, text="Boutton 1",bg="yellow")
bou2=Button(fen, text="Boutton 1",bg="yellow")
bou3=Button(fen, text="Boutton 1",bg="yellow")
bou1.pack()
bou2.pack()
bou3.pack()
def 1(event):
	print("1")
def 2(event):
	print("2")
def 3(event):
	print("3")
bou1=bind("<Button-1>",1)
bou2=bind("<Button-1>",2)
bou3=bind("<Button-1>",3)
fen.mainloop()
