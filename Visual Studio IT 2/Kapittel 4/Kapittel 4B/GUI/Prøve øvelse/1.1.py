import tkinter as tk  
#from tkinter import ttk
import ttkbootstrap as ttk
 
#window
window = ttk.Window(themename = "darkly")
window.title("Demo")
window.geometry("300x150")
 
def convert():
    mile_input = entryInt.get()
    km_output = mile_input * 1.60934
    outputString.set(f"{km_output} km")
 
#title
title_label = ttk.Label(master = window, text = "Miles to kilometers", font = ("Calibri 24 bold"), anchor = "center")
title_label.grid(row=0, column=0)
 
#input field
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
 
entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
input_frame.grid(row=1, column=0)
 
#output
outputString = tk.StringVar()
output_label = ttk.Label(master=window, text="output",
    font=("Calibri 14"), anchor = "w",
     textvariable = outputString)
output_label.grid(row=2, column=0)
#run
window.mainloop()
 