import tkinter as tk

from templates.TextLabel import TextLabel


class NumInput:
    def __init__(self, text):
        self.label = TextLabel(text)
        self.entry = tk.Entry(fg="white", bg="black", width=5)
        self.entry.pack()

    def get_input_value(self):
        return self.entry.get()