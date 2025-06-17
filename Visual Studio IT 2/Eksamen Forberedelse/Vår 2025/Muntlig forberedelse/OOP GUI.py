import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv

class Bestilling:
    def __init__(self, kunde, film, sete):
        self.kunde = kunde
        self.film = film
        self.sete = sete
        self.tidspunkt = datetime.now().strftime("%d.%m.%Y %H:%M")

    def __str__(self):
        return f"{self.kunde} har bestilt {self.film} på sete {self.sete} kl {self.tidspunkt}"

    def lagre_til_csv(self, filnavn):
        with open(filnavn, "a", newline="") as fil:
            writer = csv.writer(fil)
            writer.writerow([self.kunde, self.film, self.sete, self.tidspunkt])



# --- GUI-funksjon ---
def opprett_bestilling():
    kunde = navn_entry.get()
    film = film_entry.get()
    sete = sete_entry.get()

    if not kunde or not film or not sete:
        messagebox.showerror("Feil", "Alle felt må fylles ut")
        return None

    b = Bestilling(kunde, film, sete)
    b.lagre_til_csv("bestillinger.csv")
    listebox.insert(tk.END, str(b))

    navn_entry.delete(0, tk.END)
    film_entry.delete(0, tk.END)
    sete_entry.delete(0, tk.END)


# --- GUI-oppsett ---
root = tk.Tk()
root.title("Kinobestilling")

tk.Label(root, text="Navn:").grid(row=0, column=0)
navn_entry = tk.Entry(root)
navn_entry.grid(row=0, column=1)

tk.Label(root, text="Film:").grid(row=1, column=0)
film_entry = tk.Entry(root)
film_entry.grid(row=1, column=1)

tk.Label(root, text="Sete:").grid(row=2, column=0)
sete_entry = tk.Entry(root)
sete_entry.grid(row=2, column=1)

bestill_btn = tk.Button(root, text="Bestill billett", command=opprett_bestilling)
bestill_btn.grid(row=3, column=0, columnspan=2, pady=5)

tk.Label(root, text="Kvitteringer:").grid(row=4, column=0, columnspan=2)
listebox = tk.Listbox(root, width=50)
listebox.grid(row=5, column=0, columnspan=2)

root.mainloop()
