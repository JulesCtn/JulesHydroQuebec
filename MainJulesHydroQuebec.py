from tkinter import *
from PIL import ImageTk,Image

#Settings of the window
tab = Tk()
tab.title("Test semaine 2")
tab.geometry('400x200')

#fonction click
def myClick():
    result = entry1.get()
    label2.configure(text=result)

#Creating Label Widget
label1 = Label(tab, text="Entrez une valeur")
label2 = Label(tab, height=2, width=10)
entry1 = Entry(tab, width=10, borderwidth=3)
myButon = Button(tab, text="Display entry", command=myClick)

#Creating Δ for Centrale
photo = PhotoImage(file="Centrale.png")
canvas = Canvas(tab,width=350, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)

#Showing it onto the screen
label1.grid(row=0, column=0, padx=10)
label2.grid(row=1, column=0, padx=10)
entry1.grid(row=0, column=1, padx=10)
myButon.grid(row=0, column=2)

canvas.grid(row=2, column=1)

tab.mainloop()
