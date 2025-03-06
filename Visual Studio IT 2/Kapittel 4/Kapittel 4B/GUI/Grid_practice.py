import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Bildefremviser")

bilde1 = Image.open("tkinter.jpg")
bilde2 = Image.open("tkinter.jpg")
bilde3 = Image.open("tkinter.jpg")

bilder = [bilde1,bilde2,bilde3]

for bilde in bilder:
    bilde = bilde.resize((150,150), Image.Resampling.LANCZOS)
#    bilde = ImageTk.PhotoImage(bilde)


tittel = tk.Label(root, text="Bildefremviser")
 .grid(row=0, column=0, columnspan=2)

bilde_label = tk.Label(frame)
bilde_label.grid(row=0, column=0, columnspan=2)

def vis_bilde(index):
    bilde_label.config(image=bilder[index])

index = 0
vis_bilde(index)

def neste_bilde():
    index += 1
    if index > len(bilder):
        index = 0
    vis_bilde(index)

def forrige_bilde():
    index -= 1
    if index < 0:
        index = len(bilder)
    vis_bilde(index)

previous = tk.Button(root, text="previous", command=forrige_bilde)
previous.grid(row=2, column=0)

next = tk.Button(root, text="next", command=neste_bilde)
next.grid(row=2, column=1)

root.mainloop()