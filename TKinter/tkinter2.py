from tkinter import *

root=Tk()
root.geometry("400x200")
root.title("Tkinter")

b1=Button(root,text="Button 1" , width=20)
b2=Button(root,text="Button 2" , width=20)
b3=Button(root,text="Button 3" , width=20)
b4=Button(root,text="Button 4", width=20)


b1.grid(row=0,column=0,padx=10,pady=10)
b2.grid(row=0,column=1,padx=10,pady=10)
b3.grid(row=1,column=0,padx=10,pady=10)
b4.grid(row=1,column=1,padx=10,pady=10)





root.mainloop()