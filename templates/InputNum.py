import tkinter as tk


class NumInput:
    def __init__(self, text):
        self.label = tk.Label(text=text)
        self.label.pack()
        self.entry = tk.Entry(fg="white", bg="black", width=5)
        self.entry.pack()

    def get_input_value(self):
        return self.entry.get()