import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Simple GUI Test")
root.geometry("300x150")

# Function to be called when button is clicked
def on_button_click():
    messagebox.showinfo("Info", "Button was clicked!")

# Add a label
label = tk.Label(root, text="Hello, this is a simple GUI test.")
label.pack(pady=10)

# Add a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
