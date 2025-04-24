import tkinter as tk            # font er en submodul, 
from tkinter import font        # som ikke kan kalles direkte med tk.
from PIL import Image, ImageTk  # husk pip install Pillow
from pathlib import Path

# Funksjon for å vise hilsen basert på inndata
def skriv_ut():
    hilsen.configure(text=f"Hallo {navn.get()}!")

# Opprett et vindu
root = tk.Tk()

# Sett standard font for alle widgets i applikasjonen
root.option_add("*Font", "Arial 20")

# Endre tekst på tittellinjen
root.title("Inndata/Utdata")


bilde = Image.open("Mario.png") # Alternativ til linje over
bilde = bilde.resize((150, 150), Image.Resampling.LANCZOS)
bilde = ImageTk.PhotoImage(bilde)
tk.Label(root, image=bilde).grid(row=0, column=0, padx=5, pady=5)

# Lag en ramme for høyre del
frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=0, column=1, padx=5, pady=15)

arrow = tk.Label(frame, text="←----------", font=("Arial", 24), fg="black")
arrow.grid(row=0, column=0, padx=5, pady=13)

tk.Button(frame, text="Mario", width=10) \
    .grid(row=0, column=1, padx=5)

hilsen = tk.Label(frame, width=25, fg="white", pady=3)
hilsen.grid(row=1, column=0, columnspan=2, pady=13)

root.mainloop()
