#!/usr/bin/env python

import tkinter as tk

# Initialization
window = tk.Tk()
# Rename window title
window.title("Calculator")

display = tk.Entry(window, bg="#808080", font=("Times", 24, "bold")).grid(row=0, column=2)
one = tk.Button(window, text="1", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=1, column=1)
two = tk.Button(window, text="2", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=1, column=2)
three = tk.Button(window, text="3", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=1, column=3)
four = tk.Button(window, text="4", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=2, column=1)
five = tk.Button(window, text="5", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=2, column=2)
six = tk.Button(window, text="6", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=2, column=3)
seven = tk.Button(window, text="7", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=3, column=1)
eight = tk.Button(window, text="8", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=3, column=2)
nine = tk.Button(window, text="9", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=3, column=3)
zero = tk.Button(window, text="0", bg="#808080", activebackground="#D3D3D3", font=("Times", 24, "bold")).grid(row=4, column=2)

window.mainloop()