import tkinter as tk
import random

# Define the Tvers class
class Tvers:
    def __init__(self, root):
        self.root = root
        self.root.title("Tvers")  # Set the window title
        self.root.geometry("600x400")  # Set the window size
        self.color = "white"  # Background color

        self.correct_word = "HELLO"  # The correct word to guess
        self.letters = list(self.correct_word)  # Convert the word to a list of letters
        random.shuffle(self.letters)  # Shuffle the letters

        # Create a canvas to draw on
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg=self.color)
        self.canvas.pack()

        self.boxes = []  # List to store the boxes
        self.letter_labels = []  # List to store the letter labels

        self.create_boxes()  # Create the boxes
        self.create_letters()  # Create the letter labels

    # Method to create the boxes
    def create_boxes(self):
        for i in range(len(self.correct_word)):
            box = self.canvas.create_rectangle(100 + i*80, 50, 150 + i*80, 110, fill=self.color)
            self.boxes.append(box)

    # Method to create the letter labels
    def create_letters(self):
        for i, letter in enumerate(self.letters):
            label = tk.Label(self.root, text=letter, font=("Arial", 24), bg=self.color)
            label.place(x=100 + i*80, y=300)
            label.bind("<Button-1>", self.on_drag_start)  # Bind left mouse button click to start dragging
            label.bind("<B1-Motion>", self.on_drag_motion)  # Bind mouse motion with left button held to dragging
            label.bind("<ButtonRelease-1>", self.on_drag_release)  # Bind left mouse button release to stop dragging
            self.letter_labels.append(label)

    # Method to handle the start of dragging
    def on_drag_start(self, event):
        widget = event.widget
        widget.lift()  # Bring the widget to the front
        self._drag_data = {"x": event.x, "y": event.y}  # Store the initial position

    # Method to handle the dragging motion
    def on_drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - self._drag_data["x"] + event.x
        y = widget.winfo_y() - self._drag_data["y"] + event.y
        widget.place(x=x, y=y)  # Move the widget to the new position

    # Method to handle the end of dragging
    def on_drag_release(self, event):
        widget = event.widget
        x, y = widget.winfo_x(), widget.winfo_y()
        for i, box in enumerate(self.boxes):
            box_coords = self.canvas.coords(box)
            # Check if the widget is inside a box
            if box_coords[0] < x < box_coords[2] and box_coords[1] < y < box_coords[3]:
                # Check if the letter is correct
                if self.correct_word[i] == widget.cget("text"):
                    self.canvas.itemconfig(box, fill="green")  # Change box color to green
                    widget.config(bg="green")  # Change label background to green
                else:
                    self.canvas.itemconfig(box, fill="red")  # Change box color to red
                    widget.config(bg="red")  # Change label background to red
                widget.place(x=box_coords[0] + 10, y=box_coords[1] + 10)  # Place the widget inside the box


# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="white")
    game = Tvers(root)
    root.mainloop()
