from tkinter import *

# Réglages de la fenêtre master
master = Tk()
master.title("UQAC - Système de Production")
master.iconbitmap("images/logo.ico")
master.geometry('1280x720')
master.minsize(1280, 720)
master.config(background="#4065A4")

# Chemin des images GUI
image_centrale = PhotoImage(file="images/Centrale.png")
image_reservoir = PhotoImage(file="images/Reservoir.png")
image_add_centrale = PhotoImage(file="Theme/light/add-button.png")

def show_centrale():
    test = ImageTk.PhotoImage(image_centrale)

# Creer la frame/boîte principale
frame = Frame(master, background="#000000")

# Creer le bouton pour ajouter une centrale
button_add_centrale = Button(frame, image=image_add_centrale, command=show_centrale).pack(side=TOP)


# Afficher la frame/boîte
frame.pack(expand=YES)

# Creation d'une barre de menu
menu_bar = Menu(master)
# Creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quitter", command=master.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
# Configurer la fenêtre pour ajouter la barre menu
master.config(menu=menu_bar)

master.mainloop()
