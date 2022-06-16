"""
from tkinter import *

root=Tk()
root.geometry("300x300")
root.title("Button Quitter en Tkinter")

b1=Button(root,text="Quitter",command=quit)
b1.place(x=100,y=100)
root.mainloop()

"""

from tkinter import *

root=Tk()
root.geometry("300x300")
root.title("Button Quitter en Tkinter2")

def fin():
    root.quit()


b1=Button(root,text="Quitter",command=fin)
b1.place(x=100,y=100)

root.mainloop()