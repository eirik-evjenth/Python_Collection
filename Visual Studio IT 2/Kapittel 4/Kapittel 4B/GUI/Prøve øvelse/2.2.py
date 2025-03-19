'''
2.2. StopWatch App
A stopwatch with Start, Stop, and Reset buttons. It should display elapsed time.
'''

import tkinter as tk


class App:
    def __init__(self):
        # Opprett et vindu og sett tittel og størrelse
        self.root = tk.Tk()
        self.root.title("Stopwatch")
        self.root.geometry("300x200")

        # Opprett en hovedramme for applikasjonen våres
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Oppretter timeren
        self.timer = tk.Label(self.frame, width=25, pady=3)
        self.timer.grid(row=0, column=0, columnspan=3, pady=13)

        # Start knapp
        self.start = tk.Button(self.frame, text="Start", command=self.start)
        self.start.grid(row=2, column=0)

        # Stop knapp
        self.stop = tk.Button(self.frame, text="Stop", command=self.stop)
        self.stop.grid(row=2, column=1)

        # Restart knapp
        self.stop = tk.Button(self.frame, text="Restart", command=self.restart)
        self.stop.grid(row=2, column=2)


        self.time = 0

    def start(self):
            self.update_timer()

    def update_timer(self):
        self.time += 0.1
        self.timer.configure(text=f"{self.time:.1f} seconds")
        self.update_timer_id = self.root.after(100, self.update_timer)

    def stop(self):
        self.root.after_cancel(self.update_timer_id)

    def restart(self):
         self.time = 0
         self.timer.configure(text=f" 0 seconds")
         self.root.after_cancel(self.update_timer_id)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()