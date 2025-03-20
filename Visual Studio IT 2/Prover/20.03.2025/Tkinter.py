import tkinter as tk  
from tkinter import ttk
#import ttkbootstrap as ttk
 
#window
# window = ttk.Window(themename = "darkly")  Prøvde ttkbootstrap for å lage det se finere men fungerte ikke



# Window bare lager vinduet med tittel og en grei størrelse
window = tk.Tk()
window.title("Temperaturstyring")
window.geometry("300x300")



# Definerer opp funksjon som adderer temperatur med 0.5 så bruker jeg config å skrive det
def up():
    global temp # Dette er ikke bra med global temp, men det var det letteste som jeg fant, ser stygt men jaja
    temp += 0.5
    temp_labelT.config(text=f"Temperatur: {temp}°C")

# Samme funksjon som over bare med -= 0.5 slik at temperaturen går ned 0.5 
def ned():
    global temp
    temp -= 0.5
    temp_labelT.config(text=f"Temperatur: {temp}°C")


# Her bare tar jeg temperaturen som har blitt endret på og setter den i bunnen
def sett():
    temp_labelB.config(text=f"Temperatur satt til {temp}° C")



# start temperatur satt til 20
temp = 20

 
# av/på, ganske standard med text, fant seagreen1 som lignet på den i oppgaven
av_på = tk.Button(master = window, text="Av/På", bg="SeaGreen1")
av_på.place(x=0, y=0, width=60, height=240) 
# Bruker place funksjonen for alt siden mens jeg øvde for prøven var det lettere for meg å forstå


# Temperatur i midten, temp label TOP, bare for den øvre labelen
temp_labelT = tk.Label(master=window,text=f"Temperatur: {temp}°C",font="Arial 12", 
                      borderwidth=1, relief="solid", bg="white")
# https://www.geeksforgeeks.org/how-to-set-border-of-tkinter-label-widget/ for border

temp_labelT.place(x=70,y=70,height=100,width=160)


# up knap, bare rett frem og henviser til kommandown
up = tk.Button(master=window, text="↑", bg="SeaGreen1", command=up)
up.place(x=240, y=0, width=60, height = 40)


# sett knapp som henviser til sett funksjon
sett = tk.Button(master=window, text="Sett", bg="SeaGreen1", command=sett)
sett.place(x=240, y = 60, height = 120, width=60)


# down knapp, samme som de over, bare ctrl c + ctrl v med litt endringer i placement
up = tk.Button(master=window, text="↓", bg="SeaGreen1", command=ned)
up.place(x=240,y=200,width=60,height=40)


# Label helt på bunnen, bruker samme teknikker som før. Temp label BOTTOM siden den er under.
temp_labelB = tk.Label(master=window,text=f"Temperatur satt til {temp}° C", 
                      font="Arial 12", borderwidth=1, relief="solid", bg="white") 

temp_labelB.place(x=20,y=260,height=20,width=260)



 
# kjører hele funksjonen
window.mainloop()
 