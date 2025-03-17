import tkinter as tk  # Import the Tkinter library

def start_drag(event):  
    # Store the initial position of the widget when dragging starts
    event.widget.startX = event.x  # Store initial X position
    event.widget.startY = event.y  # Store initial Y position

def on_drag(event):  
    # Update widget position as it's dragged
    widget = event.widget  # Get reference to the dragged widget
    x = widget.winfo_x() - widget.startX + event.x  
    y = widget.winfo_y() - widget.startY + event.y  
    widget.place(x=x, y=y)  # Move the widget

root = tk.Tk()  # Create the main window
root.title("Drag and Drop")  # Set window title
root.geometry("600x450")  # Set window size
root.configure(background='white')  # Set window background color

# Create a label that can be dragged
label = tk.Label(root, text="Drag Me", bg="black", fg="white", padx= 5, pady=5)  
label.place(x=30, y=30)  # Place the label at initial position

# Bind mouse events to the label for dragging functionality
label.bind("<ButtonPress-1>", start_drag)  # Detect mouse press to start dragging
label.bind("<B1-Motion>", on_drag)  # Move label while dragging

root.mainloop()  # Run the Tkinter event loop