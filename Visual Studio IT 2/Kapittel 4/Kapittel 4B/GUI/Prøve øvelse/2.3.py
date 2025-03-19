'''
2.3
Rock paper scissors
'''




import tkinter as tk
import random


class App:
    def __init__(self):
        # Opprett et vindu og sett tittel og størrelse
        self.root = tk.Tk()
        self.root.title("Timer")
        self.root.geometry("300x200")

        # Opprett en hovedramme for applikasjonen våres
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.choices = ["rock", "paper", "scissors"]
        
        self.choices_var = tk.IntVar(value=-1)
        for idx, choice in enumerate(self.choices):
            tk.Radiobutton(self.frame, text=choice, variable=self.choices_var, value=idx, command=self.valg, width=10, anchor="w") \
            .grid(row=idx + 1, column=0)

    def valg(self):
        self.idx_choice = self.choices_var.get()
        if self.idx_choice != -1:
            print(f"You selected: {self.choices[self.idx_choice]}")



    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
