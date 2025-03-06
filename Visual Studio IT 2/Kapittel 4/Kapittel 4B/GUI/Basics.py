import tkinter as tk

root = tk.Tk()

# Opprett widgets
tk.Label(root, text='Hva heter du?').pack()
navn = tk.Entry(root, justify=tk.CENTER)
navn.pack()
tk.Button(root, text="Les navn", command=lambda: hilsen.configure(text=f"Hei {navn.get()}!")).pack()
hilsen = tk.Label(root)
hilsen.pack()

root.mainloop()