from Tkinter import *
fen=Tk()
fen.configure(width="500", height="600")
bou=Button(fen, text="boutton",bg="red")
bou1=Button(fen, text="cree un boutton",bg="yellow")
bou.pack()
bou1.pack()
clic=0
def click(event):
	global clic
	clic=clic+1

	if clic==1:
		bou.configure(text="Boutton", bg="blue")
	if clic==2
		bou.configure(text="Boutton",bg="yellow")
	if clic==3
		bou.configure(text="Boutton",bg="Magenta")
def clicl2(event);
	global clic2
	clic2=clic2+1
	bou=Button(fen,text="Nouveau boutton", bg="yellow")
bou.bin("<button-1>",clicl2) 
bou1.bind("<Button-1>",click)
fen.mainloop()
