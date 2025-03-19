'''
Listboks øvelse med en to do list
'''

import tkinter as tk

class App:
    def __init__(self):
        # Opprett et vindu og sett tittel og størrelse
        self.root = tk.Tk()
        self.root.title("Timer")
        self.root.geometry("500x300")

        # Opprett en hovedramme for applikasjonen våres
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.listbox = tk.Listbox(self.frame)
        self.listbox.grid(row=1, column=0, columnspan=2, pady=10)


        # Opprett en knapp og en label
        self.goal = tk.Entry(self.frame, justify=tk.CENTER, width=22) # 22 slik at teksten passer
        self.goal.insert(0, "Skriv inn et mål ")
        self.goal.grid(row=2, column=0)

        self.add = tk.Button(self.frame, text="Add", command=self.insert)
        self.add.grid(row=2, column=1)

        self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete)
        self.delete_button.grid(row=2, column=2, pady=10)

        self.help_button = tk.Button(self.frame, text="Help", command=self.help)
        self.help_button.grid(row=2, column=3, pady=10)

        self.label = tk.Label(self.frame, text="")
        self.label.grid(row=3, column=0, columnspan=4)

    def insert(self):
        if self.listbox.size() < 5:
            self.listbox.insert(tk.END, self.goal.get())
        else:
            self.label.config(text="Focus on the goals you have")

    def delete(self):
        selected_goal_index = self.listbox.curselection()
        if selected_goal_index:
            self.listbox.delete(selected_goal_index)

    def help(self):
        self.label.config(text='''This program was made 
as a way to organize goals.
Using the add button one 
adds the goal they have written.
If the written goal is undesired, 
then simply press it and press delete.
                          ''')
        self.label.grid(row=1, column=2)


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()