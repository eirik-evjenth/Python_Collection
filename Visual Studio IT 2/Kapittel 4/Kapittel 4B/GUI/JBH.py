import tkinter as tk
from PIL import Image, ImageTk
 
# Opprett hovedvinduet
root = tk.Tk()
root.title("Bildefremviser")
 
# Legg til en tittel
tittel = tk.Label(root, text="Bildefremviser")
tittel.grid(row=0, column=0, columnspan=2, pady=10)
 
# Last inn bildene
bilde1 = Image.open("tkinter.jpg")
bilde2 = Image.open("tkinter.jpg")
bilde3 = Image.open("tkinter.jpg")
 
# Liste over bilder
bilder = [bilde1, bilde2, bilde3]
 
# Endre størrelse på bildene og konverter til PhotoImage
for i in range(len(bilder)):
    bilder[i] = bilder[i].resize((150, 150), Image.Resampling.LANCZOS)
    bilder[i] = ImageTk.PhotoImage(bilder[i])
 
 
 
# Opprett en label for å vise bildene
bilde_label = tk.Label(root)
bilde_label.grid(row=1, column=0, columnspan=2, pady=10)
 
# Funksjon for å vise bildet
def vis_bilde(index):
    bilde_label.configure(image=bilder[index])
    bilde_label.image = bilder[index]  # Behold referansen til bildet
 
# Initialiser bildeindeksen og vis det første bildet
index = 0
vis_bilde(index)
 
# Funksjon for å gå til neste bilde
def neste_bilde():
    global index
    index = (index + 1) % len(bilder)
    vis_bilde(index)
 
# Funksjon for å gå til forrige bilde
def forrige_bilde():
    global index
    index = (index - 1) % len(bilder)
    vis_bilde(index)
 
# Legg til navigasjonsknapper
previous = tk.Button(root, text="Forrige", command=forrige_bilde)
previous.grid(row=2, column=0, pady=10)
 
next = tk.Button(root, text="Neste", command=neste_bilde)
next.grid(row=2, column=1, pady=10)
 
# Start hovedløkken for å holde vinduet åpent
root.mainloop()
 