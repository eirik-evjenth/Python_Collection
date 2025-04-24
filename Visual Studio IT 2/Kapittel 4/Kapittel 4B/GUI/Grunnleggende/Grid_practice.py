import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Bildefremviser")
# root.geometry("800x600")

tittel = tk.Label(root, text="Bildefremviser")
tittel.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

bilde1 = Image.open("Mario.png")
bilde2 = Image.open("Mario2.png")
bilde3 = Image.open("Mario3.png")

bilder = [bilde1,bilde2,bilde3]

for i in range(len(bilder)):
    bilder[i] = bilder[i].resize((600, 600), Image.Resampling.LANCZOS)
    bilder[i] = ImageTk.PhotoImage(bilder[i])


bilde_label = tk.Label(root)
bilde_label.grid(row=0, column=0, columnspan=2)


def vis_bilde(index):
    bilde_label.configure(image=bilder[index])
    bilde_label.image = bilder[index]


def neste_bilde():
    global index
    index += 1
    if index >= len(bilder):
        index = 0
    vis_bilde(index)

def forrige_bilde():
    global index
    index -= 1
    if index < 0:
        index = len(bilder) - 1
    vis_bilde(index)

index = 0

vis_bilde(index)

previous = tk.Button(root, text="previous", command=forrige_bilde)
previous.grid(row=2, column=0)

next = tk.Button(root, text="next", command=neste_bilde)
next.grid(row=2, column=1)

root.mainloop()