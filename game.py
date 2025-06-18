# Feature A
import tkinter as tk

root = tk.Tk()
root.title("Coin Toss Simulator")

colors = ["red", "blue", "green", "yellow"]
buttons = []

for i, color in enumerate(colors):
    btn = tk.Button(root, bg=color, width=10, height=5)
    btn.grid(row=0, column=i, padx=10, pady=10)
    buttons.append(btn)

root.mainloop()
