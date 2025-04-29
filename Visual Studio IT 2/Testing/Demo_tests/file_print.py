            # Bind close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        # Save settings to a file
        with open("instillinger.txt", "w") as file:
            file.write(f"lys insensitet: {self.lys_slider.get()}\n")
            file.write(f"temp: {self.temp}\n")
        
        # Now close the window
        self.root.destroy()s