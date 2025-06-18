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

# Feature B
import random

pattern = []

def show_pattern():
    global pattern
    pattern = [random.randint(0, 3) for _ in range(3)]
    delay = 1000
    for i, index in enumerate(pattern):
        root.after(i * delay, lambda idx=index: flash_button(idx))

def flash_button(index):
    btn = buttons[index]
    original = btn.cget("bg")
    btn.config(bg="white")
    root.after(500, lambda: btn.config(bg=original))

show_pattern()

# Feature C
user_pattern = []

def on_click(index):
    user_pattern.append(index)
    if user_pattern == pattern[:len(user_pattern)]:
        if len(user_pattern) == len(pattern):
            print("Correct sequence!")
    else:
        print("Wrong sequence!")
        user_pattern.clear()

# Assign click event
for i, btn in enumerate(buttons):
    btn.config(command=lambda idx=i: on_click(idx))


# Feature D
pattern_length = tk.IntVar(value=3)

def start_game():
    global pattern
    user_pattern.clear()
    pattern.clear()
    pattern.extend([random.randint(0, 3) for _ in range(pattern_length.get())])
    show_pattern()

length_label = tk.Label(root, text="Pattern size:")
length_label.grid(row=1, column=0, columnspan=1)
length_entry = tk.Entry(root, textvariable=pattern_length)
length_entry.grid(row=1, column=1, columnspan=1)

start_btn = tk.Button(root, text="Start", command=start_game)
start_btn.grid(row=1, column=2, columnspan=2)
