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

        #Top label
        self.text = "Pick something"
        self.label = tk.Label(self.frame, text=self.text)
        self.label.grid(row=0, column=0)
        
        self.choices_var = tk.IntVar(value=-1)
        for idx, choice in enumerate(self.choices):
            tk.Radiobutton(self.frame, text=choice, variable=self.choices_var, value=idx, command=self.valg, width=10, anchor="w") \
            .grid(row=idx + 1, column=0)

        self.computer_choice = None



    def valg(self):
        self.idx_choice = self.choices_var.get()
        if self.idx_choice != -1:
            # print(f"You selected: {self.choices[self.idx_choice]}")
            self.computer_choice = random.choice(self.choices)
            # print(f"Computer selected: {self.computer_choice}")
            if self.choices[self.idx_choice] == self.computer_choice:
                self.text = "Draw"
            elif (self.choices[self.idx_choice] == "rock" and self.computer_choice == "scissors") or \
                 (self.choices[self.idx_choice] == "scissors" and self.computer_choice == "paper") or \
                 (self.choices[self.idx_choice] == "paper" and self.computer_choice == "rock"):
                self.text = "You win!"
            else:
                self.text = "You lose!"
            self.label.config(text=self.text)


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
