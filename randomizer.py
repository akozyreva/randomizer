import random
import tkinter as tk

from templates.InputNum import NumInput

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
    num1 = num_input1.get_input_value()
    num2 = num_input2.get_input_value()
    print(num1, num2)
    label_generated_number.config(text=f"generated number is: {random.randint(int(num1), int(num2))}")


num_input1 = NumInput("1 num")
num_input2 = NumInput("2 num")
label_generated_number = tk.Label(text=f"generated number is:")
label_generated_number.pack()
button.bind("<Button-1>", handle_click)
button.pack()
tk.mainloop()
