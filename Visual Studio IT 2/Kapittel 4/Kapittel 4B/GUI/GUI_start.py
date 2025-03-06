import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
tk.Label(root, text="Test", height=50,fg="white", bg="black", font=("Helvetica", 50)).pack()
root["bg"] = "black"
root.mainloop()
