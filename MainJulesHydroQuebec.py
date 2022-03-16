from tkinter import *
from turtle import color
from PIL import ImageTk,Image

master = Tk()
#Settings of the main window
master.title("System Production")
master.geometry('1280x720')
master.minsize(1280, 720)
master.iconbitmap("logo.ico")

#Fonction click
def myClick():
    result = entry1.get()
    label2.configure(text=result)

#Creating Label Widget
label1 = Label(master, text="Entrez une valeur")
label2 = Label(master, height=2, width=10)
entry1 = Entry(master, width=10, borderwidth=3)
Buton1 = Button(master, text="Display entry", command=myClick)

#Creating Δ for Centrale image(100x87)
Centrale = PhotoImage(file="Centrale.png")
canvas1 = Canvas(master,width=100, height=87)
canvas1.create_rectangle(0, 0, 500, 500, fill="grey")
canvas1.create_image(0, 0, anchor=NW, image=Centrale)
#Creating ▭ for Reservoir image(100x76)
Reservoir = PhotoImage(file="Reservoir.png")
canvas2 = Canvas(master,width=100, height=76)
canvas2.create_image(0, 0, anchor=NW, image=Reservoir)
#Creating Δ + ▭ for CentraleReservoir image(100x100)
CentraleReservoir = PhotoImage(file="CentraleReservoir.png")
canvas3 = Canvas(master,width=100, height=100)
canvas3.create_image(0, 0, anchor=NW, image=CentraleReservoir)
#Creating | for Liaison image(100x80)
Liaison = PhotoImage(file="Liaison.png")
canvas4 = Canvas(master,width=100, height=80)
canvas4.create_image(0, 0, anchor=NW, image=Liaison)

#Canvas creation // autre solution 
canvas = Canvas(master, height=100, width=500)
canvas.create_rectangle(0, 0, 600, 600, fill="grey") # le fond pour mieu comprendre le canvas (x1, y1, x2, y2)
canvas.create_rectangle(0, 25, 25, 75, fill="magenta", outline="black", width=2) # ▭ reservoir
canvas.create_polygon(25, 25, 25, 75, 50, 50, fill="magenta",outline="black", width=2)# Δ Centrale (x1, y1, x2, y2, x3, y3)
canvas.create_line(50,50,75,50,fill="black",width=2) # |
canvas.create_polygon(75, 25, 75, 75, 100, 50, fill="magenta",outline="black", width=2)# Δ


#Showing it onto the screen
label1.grid(row=1, column=2, padx=10,pady=5)
entry1.grid(row=2, column=2, padx=10,pady=5)
Buton1.grid(row=3, column=2)
label2.grid(row=4, column=2, padx=10)


canvas1.grid(row=5, column=2) #    Δ
canvas2.grid(row=6, column=2) #    ▭
canvas4.grid(row=7, column=2) #    |
canvas3.grid(row=8, column=2) #  ▭ + Δ
canvas.grid(row=9 , column=2) # canva dessin

master.mainloop()
