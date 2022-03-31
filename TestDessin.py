from tkinter import *

master = Tk()
#Settings of the main window
master.title("System Production")
master.geometry('800x600')
master.minsize(800, 600)
master.iconbitmap("logo.ico")
#Theme azure
master.tk.call("source", "azure.tcl")
master.tk.call("set_theme", "light")
#Global variable
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
    
#Fonction click pour clear dessin
def myClear():
    global Delta
    Delta=Delta-100
    canvas.create_rectangle(Delta,0,Delta+100,100,fill="grey99",outline="grey99")

#Creation du bouton pour Δ + ▭
Buton1 = Button(master, text="Add Centrale + Reservoir", command=myCentraleReservoir)
Buton2 = Button(master, text="Add Centrale", command=myCentrale)
Buton3 = Button(master, text="Add Reservoir", command=myReservoir)
Buton4 = Button(master, text="Clear", command=myClear)

#Canvas creation des dessins
canvas = Canvas(master, height=100, width=2000)
canvas.create_line(3,3,3,100,fill="black",width=2)

#Showing it onto the screen
Buton1.grid(row=1, column=1)
Buton2.grid(row=2, column=1)
Buton3.grid(row=3, column=1)
Buton4.grid(row=4, column=1)
canvas.grid(row=2 , column=2) # canva dessin

master.mainloop()
