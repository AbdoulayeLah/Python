from tkinter import *

def entrer():
    l1['text']="Bonjour"

def quitter():
    root.quit()


root=Tk()
root.geometry("300x300")
root.title("Message")

#créé un label
l1=Label(root,text="s'affiche ici")
l1.place(x=150,y=0)

b1=Button(root,text="Affichage", command=entrer)
b1.place(x=150,y=50,width=100)

b2=Button(root,text="Quitter", command=quitter)
b2.place(x=150,y=150,width=100)

root.mainloop()