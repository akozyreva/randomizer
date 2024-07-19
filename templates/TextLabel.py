import tkinter as tk


class TextLabel:
    def __init__(self, text):
        self.label = tk.Label(text=text)
        self.label.pack()

    def update_value(self, value):
        self.label.config(text=value)