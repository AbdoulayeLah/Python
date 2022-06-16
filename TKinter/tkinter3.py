from tkinter import *

#créé la fenetre tkinter
root=Tk()
root.geometry("400x200")
root.title("Mon tkinter")

b1=Button(root,text="Button 1")
b2=Button(root,text="Button 2")
b3=Button(root,text="Button 3")
b4=Button(root,text="Button 4")

b1.place(x=50,y=50,width=100)
b2.place(x=50,y=100,width=100)
b3.place(x=200,y=50,width=100)
b4.place(x=200,y=100,width=100)

root.mainloop()
