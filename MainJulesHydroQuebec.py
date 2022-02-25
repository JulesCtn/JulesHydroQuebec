from tkinter import *
from PIL import ImageTk,Image

#Settings of the window
tab = Tk()
tab.title("Test semaine 2")
tab.geometry('600x400')

#fonction click
def myClick():
    result = entry1.get()
    label2.configure(text=result)

#Creating Label Widget
label1 = Label(tab, text="Entrez une valeur")
label2 = Label(tab, height=2, width=10)
entry1 = Entry(tab, width=10, borderwidth=3)
Buton1 = Button(tab, text="Display entry", command=myClick)

#Creating Δ for Centrale (100x87)
Centrale = PhotoImage(file="Centrale.png")
canvas1 = Canvas(tab,width=100, height=87)
canvas1.create_image(0, 0, anchor=NW, image=Centrale)
#Creating ▭ for Reservoir (100x100)
Reservoir = PhotoImage(file="Reservoir.png")
canvas2 = Canvas(tab,width=100, height=100)
canvas2.create_image(0, 0, anchor=NW, image=Reservoir)


#Showing it onto the screen
label1.grid(row=1, column=2, padx=10,pady=5)
entry1.grid(row=2, column=2, padx=10,pady=5)
Buton1.grid(row=3, column=2)
label2.grid(row=4, column=2, padx=10)

canvas1.grid(row=5, column=2)
canvas2.grid(row=6, column=2)

tab.mainloop()
