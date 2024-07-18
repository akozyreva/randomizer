import random
import tkinter as tk

window = tk.Tk()
window.title("Randomizer")
window.geometry('300x200')
greeting = tk.Label(text="Random number generator")
greeting.pack()
button = tk.Button(
    text="Generate",
    width=5,
    height=2,
    bg="black",
    fg="black",
)


def handle_click(event):
    num1 = entry.get()
    num2 = entry2.get()
    print(num1, num2)
    label_generated_number.config(text=f"generated number is: {random.randint(int(num1), int(num2))}")


label = tk.Label(text="1 num")
label.pack()
entry = tk.Entry(fg="white", bg="black", width=5)
entry.pack()
label2 = tk.Label(text="2 num")
label2.pack()
entry2 = tk.Entry(fg="white", bg="black", width=5)
entry2.pack()
label_generated_number = tk.Label(text=f"generated number is:")
label_generated_number.pack()
button.bind("<Button-1>", handle_click)
button.pack()
tk.mainloop()
