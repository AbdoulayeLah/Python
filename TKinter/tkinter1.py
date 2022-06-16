from tkinter import *



root=Tk()
root.geometry("300x100")
root.title("Tkinter")

b1=Button(root,text="Button 1")
b2=Button(root,text="Button 2")
b3=Button(root,text="Button 3")
b4=Button(root,text="Button 4")

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)



root.mainloop()



