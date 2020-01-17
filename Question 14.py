from Tkinter import *
fen=Tk()

bou=Button(fen, text="boutton",bg="red")
bou.pack()
clic=0
def click(event):
	global clic
	clic=clic+1

	if clic==1:
		bou.configure(text="Boutton", bg="yellow")
bou.bind("<Button-1>",click)
fen.mainloop()
