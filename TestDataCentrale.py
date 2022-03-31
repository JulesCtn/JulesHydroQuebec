from tkinter import *
import tkinter as tk
from tkinter import ttk

from matplotlib.pyplot import text

window = Tk()
#Settings of the main window
window.title("Data Emplacement n")
window.minsize(400, 600)
window.iconbitmap("logo.ico")
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "light")

#Nom
LabelNameCentrale = Label(window, text="Entrez le nom de la Centrale: ")
EntryNameCentrale = ttk.Entry(window)
EntryNameCentrale.insert(0, "Saisissez")

#On/Off Centrale
LabelSwitchCentrale = Label(window, text="Centrale: ")
SwitchCentrale = ttk.Checkbutton(window, text="Off/On", style="Switch.TCheckbutton")

#Nombre turbine
LabelNbTurbine=Label(window,text="Nombre de turbine(s):")
spinbox = ttk.Spinbox(window, from_=1, to=20, increment=1)
spinbox.insert(0, "#Turbines")

#On/off Turbine
LabelSwitchTurbine = Label(window, text="Turbine: ")
SwitchTurbine = ttk.Checkbutton(window, text="Off/On", style="Switch.TCheckbutton")

#Débit turbine
LabelQTurbine = Label(window, text="Entrez le débit turbine: ")
EntryQTurbine = ttk.Entry(window)
EntryQTurbine.insert(0, "Débit")

#ButtonSave = ttk.Button(window, text="Enregistrer")
#ButtonSave.grid(row=x, column=1, padx=5, pady=10, sticky="nsew")  

#Affichage
separator1 = ttk.Separator(window)
separator2 = ttk.Separator(window)

#première ligne
LabelNameCentrale.grid(row=1, column=1, padx=5, pady=(0, 10))#,sticky="ew")  
EntryNameCentrale.grid(row=1, column=2, padx=5, pady=(0, 10))#,sticky="ew")
#deuxième ligne 
LabelSwitchCentrale.grid(row=2, column=1, padx=5, pady=(0, 10))#,sticky="ew")
SwitchCentrale.grid(row=2, column=2, padx=5, pady=(0, 10))
#troisième ligne
LabelNbTurbine.grid(row=3, column=1, padx=5, pady=(0, 10))      
spinbox.grid(row=3, column=2, padx=5, pady=10, sticky="ew") 
#quatrième ligne
LabelSwitchTurbine.grid(row=4, column=1, padx=5, pady=(0, 10))  
SwitchTurbine.grid(row=4, column=2, padx=5, pady=(0, 10))
#cinquième ligne
LabelQTurbine.grid(row=5, column=1, padx=5, pady=(0, 10))       
EntryQTurbine.grid(row=5, column=2, padx=5, pady=(0, 10))
#separation
separator1.grid(row=6, column=1, padx=(20, 10), pady=10,columnspan=2, sticky="ew") 
#sixième ligne


window.mainloop()