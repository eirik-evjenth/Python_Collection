import tkinter as tk


class App:
    def __init__(self, temp, lys):
        # Opprett et vindu og sett tittel og størrelse
        self.root = tk.Tk()
        self.root.title("Muntlig fagsamtale")
        self.root.geometry("300x400")


        self.button_color = "gray"
        self.temp = temp
        self.lys = lys
        self.on_temp = True
        self.on_lys = True


        # Frame for å plassere ting på
        self.frame = tk.Frame(self.root, width=300, height=400)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.frame_temp = tk.Frame(self.frame, width=300, height=300)
        self.frame_lys = tk.Frame(self.frame, width=300, height=300)


        # Alt for lys

        # Lys bunn knapp
        self.lys = tk.Button(
            master=self.frame, text="Lys", bg=self.button_color, command=self.lys_mode)
        self.lys.place(x=150, y=350, width=150, height=50)



        # Lys konfigurasjon
        # Lysintensitet visning
        self.lys_label = tk.Label(
            master=self.frame_lys,
            text="Lysintensitet satt til 0",
            font="Arial 12",
            borderwidth=1,
            relief="solid",
            bg="white",
        )
        self.lys_label.place(x=20, y=50, width=260, height=30)

        # glider for lys intensitet
        self.lys_slider = tk.Scale(
            master=self.frame_lys, from_=0, to=100, orient=tk.HORIZONTAL, label="Lys intensitet"
        )
        self.lys_slider.place(x=20, y=100, width=260)


        # knapp for å sette lys intensitet
        self.set_lys_button = tk.Button(
            master=self.frame_lys,
            text="Set lys",
            bg=self.button_color,
            command=self.sett_lys,
        )
        self.set_lys_button.place(x=150, y=200, width=100, height=50)


        # knapp for å skru av og på lys
        self.av_på_lys = tk.Button(
            master=self.frame_lys,
            text="Av/På",
            bg=self.button_color,
            command=self.status_lys,
        )
        self.av_på_lys.place(x=50, y=200, width=100, height=50)






        # Alt for temp

        # Temp bunn knapp
        self.temp_button = tk.Button(
            master=self.frame, text="Temp", bg=self.button_color, command=self.temp_mode)
        self.temp_button.place(x=0, y=350, width=150, height=50)


        # Av/På-knapp for temp
        self.av_på_temp = tk.Button(
            master=self.frame_temp, 
            text="Av/På", 
            bg=self.button_color, 
            command=self.status_temp)
        self.av_på_temp.place(x=0, y=0, width=60, height=240)


        # Opp-knapp for temp
        self.up_button = tk.Button(
            master=self.frame_temp, text="↑", bg=self.button_color, command=self.up_temp)
        self.up_button.place(x=240, y=0, width=60, height=40)



        # Sett-knapp for temp
        self.sett_button = tk.Button(
            master=self.frame_temp, text="Sett", bg=self.button_color, command=self.sett_temp)
        self.sett_button.place(x=240, y=60, height=120, width=60)


        # Ned-knapp for temp
        self.down_button = tk.Button(
            master=self.frame_temp, text="↓", bg=self.button_color, command=self.ned_temp)
        self.down_button.place(x=240, y=200, width=60, height=40)


        # Temperaturvisning (øverst)
        self.temp_labelT = tk.Label(
            master=self.frame_temp,
            text=f"Temperatur: {temp}°C",
            font="Arial 12",
            borderwidth=1,
            relief="solid",
            bg="white",
        )
        self.temp_labelT.place(x=70, y=70, height=100, width=160)


        # Temperaturvisning (nederst)
        self.temp_labelB = tk.Label(
            master=self.frame_temp,
            text=f"Temperatur satt til {temp}° C",
            font="Arial 12",
            borderwidth=1,
            relief="solid",
            bg="white",
        )
        self.temp_labelB.place(x=20, y=260, height=20, width=260)






    # Methods for temp
    def up_temp(self):
        self.temp += 0.5
        self.temp_labelT.config(text=f"Temperatur: {self.temp}°C")


    def ned_temp(self):
        self.temp -= 0.5
        self.temp_labelT.config(text=f"Temperatur: {self.temp}°C")


    def sett_temp(self):
        if self.on_temp:
            self.temp_labelB.config(text=f"Temperatur satt til {self.temp}° C")
        else:
            pass

    def status_temp(self):
        if self.on_temp:
            self.temp_labelB.config(text="Temperatur system er slått av")
            self.on_temp = False
        else:
            self.temp_labelB.config(text="Temperatur system er slått på")
            self.on_temp = True




    # Methods for lys
    def sett_lys(self):
        if self.on_lys:
            lys_intensitet = self.lys_slider.get()
            self.lys_label.config(text=f"Lysintensitet satt til {lys_intensitet}")
        else:
            self.lys_label.config(text="Lyssystemet er slått av")



    def status_lys(self):
        if self.on_lys:
            self.lys_label.config(text="Lyssystemet er slått av")
            self.on_lys = False
        else:
            self.lys_label.config(text="Lyssystemet er slått på")
            self.on_lys = True
    





    # Hvilket modus knapper

    def lys_mode(self):
        self.frame_temp.place_forget()  # gjemmer temp frame
        self.frame_lys.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # viser lys frame



    def temp_mode(self):
        self.frame_lys.place_forget()  # gjemmer lys frame
        self.frame_temp.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # viser temp frame





    def run(self):
        # Start hovedløkken for å holde vinduet åpent
        self.root.mainloop()




if __name__ == "__main__":
    app = App(temp=21, lys=0)  # Kan velge start temperatur og lys nivå man vil ha
    app.run()
