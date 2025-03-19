

import tkinter as tk


class App:
    def __init__(self):
        # Opprett et vindu og sett tittel og størrelse
        self.root = tk.Tk()
        self.root.title("Timer")
        self.root.geometry("300x200")

        # Opprett en hovedramme for applikasjonen våres
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Opprett en knapp og en label
        self.time = tk.Entry(self.frame, justify=tk.CENTER,width=22) # 22 slik at teksten passer
        self.time.insert(0, "Skriv inn antall sekunder ")
        self.time.grid(row=1, column=0)

        self.timer = tk.Label(self.frame, width=25, bg="grey", fg="black", pady=3)
        self.timer.grid(row=0, column=0, columnspan=2, pady=13)

        self.start = tk.Button(self.frame, text="Start", command=self.start_countdown)
        self.start.grid(row=1, column=1)

        self.remaining_time = 0

    def start_countdown(self):
        try:
            self.remaining_time = int(self.time.get())
            self.update_timer()
        except ValueError:
            self.timer.configure(text="Invalid input!")

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer.configure(text=f"{self.remaining_time} seconds remaining")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer.configure(text="Time's up!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()