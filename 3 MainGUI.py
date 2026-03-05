from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import Weed_Detection_init

def center_window(root, width, height):
    """Centers the window on the screen."""
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws // 2) - (width // 2)
    y = (hs // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

def read_input():
    """Reads input from the text fields and passes them to the detection module."""
    farmer_name = textBox1.get()
    farmer_mobile = textBox2.get()
    print("Farmer Name:", farmer_name)
    print("Farmer Mobile No:", farmer_mobile)
    Weed_Detection_init.initDetection(farmer_mobile, farmer_name)

# Initialize main window
root = Tk()
root.configure(background='#6495ED')
root.title("ONION WEED DETECTION SYSTEM")
center_window(root, 1400, 800)

# Load and resize background image
image = Image.open("model/image2.jpg")
resize_image = image.resize((1600, 1000))
img = ImageTk.PhotoImage(resize_image)

# Create label for the background image
bg_label = Label(root, image=img)
bg_label.image = img  # Keep reference
bg_label.pack()

# Title Label
Label(root, text="ONION WEED DETECTION SYSTEM", font=("Courier", 30, 'bold'), fg='#f00', bg='#6495ED').place(x=400, y=60)

# Labels for input fields
Label(root, text="Farmer Name:", bg='#6495ED', font=("Ariel", 10)).place(x=400, y=205)
Label(root, text="Farmer Mobile No.:", bg='#6495ED', font=("Ariel", 10)).place(x=400, y=265)

# Input fields
textBox1 = tk.Entry(root, width=40)
textBox1.place(x=600, y=200, height=30)
textBox2 = Entry(root, width=40)
textBox2.place(x=600, y=260, height=30)

# Buttons
Button(root, text="Submit", height=1, width=13, font=("Ariel", 10, 'bold'), command=read_input).place(x=530, y=460)
Button(root, text="Exit", height=1, width=13, font=("Ariel", 10, 'bold'), command=root.destroy).place(x=700, y=460)

# Run the Tkinter event loop
root.mainloop()
