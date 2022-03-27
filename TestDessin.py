from tkinter import *
from turtle import color, width
from PIL import ImageTk,Image

master = Tk()
#Settings of the main window
master.title("System Production")
master.geometry('800x600')
master.minsize(800, 600)
master.iconbitmap("logo.ico")

global Delta
Delta = 0

#Fonction click pour | + Δ + ▭ + |   
def myCentraleReservoir():
    global Delta
    canvas.create_line(Delta,50,Delta+25,50,fill="black",width=2) # |
    Delta=Delta+25
    canvas.create_rectangle(Delta,25,Delta+25,75,fill="royalblue", outline="black",width=2) # ▭ reservoir (x1, y1, x2, y2)
    Delta=Delta+25
    canvas.create_polygon(Delta,25,Delta,75,Delta+25,50,fill="royalblue",outline="black", width=2)# Δ Centrale (x1, y1, x2, y2, x3, y3)
    Delta=Delta+25
    canvas.create_line(Delta,50,Delta+25,50,fill="black",width=2) # |
    Delta=Delta+25
    
#Fonction click pour | + Δ + |
def myCentrale():
    global Delta
    canvas.create_line(Delta,50,Delta+25,50,fill="black",width=2) # |
    Delta=Delta+25
    canvas.create_polygon(Delta,25,Delta,75,Delta+50,50,fill="royalblue",outline="black", width=2)# Δ Centrale (x1, y1, x2, y2, x3, y3)
    Delta=Delta+50
    canvas.create_line(Delta,50,Delta+25,50,fill="black",width=2) # |
    Delta=Delta+25

#Fonction click pour | + ▭ + |
def myReservoir():
    global Delta
    canvas.create_line(Delta,50,Delta+25,50,fill="black",width=2) # |
    Delta=Delta+25
    canvas.create_rectangle(Delta,25,Delta+50,75,fill="royalblue", outline="black",width=2) # ▭ reservoir (x1, y1, x2, y2)
    Delta=Delta+50
    canvas.create_line(Delta,50,Delta+25,50,fill="black",width=2) # |
    Delta=Delta+25
    
#Fonction click pour clear dessin (dessin d'un grand carré de la même couleur que le fond (grey94))
def myClear():
    global Delta
    Delta=Delta-100
    canvas.create_rectangle(Delta,Delta,Delta+100,100,fill="grey94",outline="grey94")
    canvas.create_line(Delta,Delta,Delta,100,fill="black",width=2)
    canvas.create_line(Delta+5,Delta,Delta+5,100,fill="black",width=2)
    canvas.create_line(Delta+10,Delta,Delta+10,100,fill="black",width=2)
    canvas.create_line(Delta+15,Delta,Delta+15,100,fill="black",width=2)

#Creation du bouton pour Δ + ▭
Buton1 = Button(master, text="Add Centrale + Reservoir", command=myCentraleReservoir)
Buton2 = Button(master, text="Add Centrale", command=myCentrale)
Buton3 = Button(master, text="Add Reservoir", command=myReservoir)
Buton4 = Button(master, text="Clear", command=myClear)

#Canvas creation des dessins
canvas = Canvas(master, height=100, width=500)
canvas.create_line(3,3,3,100,fill="black",width=2)
#canvas.create_rectangle(0, 0, 600, 600, fill="grey") # le fond pour mieu comprendre le canvas (x1, y1, x2, y2)

#Showing it onto the screen
Buton1.grid(row=1, column=1)
Buton2.grid(row=2, column=1)
Buton3.grid(row=3, column=1)
Buton4.grid(row=4, column=1)
canvas.grid(row=2 , column=2) # canva dessin

master.mainloop()
