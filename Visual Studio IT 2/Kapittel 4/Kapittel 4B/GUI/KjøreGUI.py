import tkinter as tk

def SkrivUt():
    answer.configure(text=f"Hewwo")

root = tk.Tk()

tk.Label(root, text='OwO').pack()
statement = tk.Entry(root, justify=tk.CENTER)
statement.pack()
tk.Button(root, text="Heyyy", command=SkrivUt).pack()
answer = tk.Label(root)
answer.pack()

root.mainloop()