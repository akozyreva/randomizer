import tkinter as tk

from templates.TextLabel import TextLabel


def validate_entry(text):
    # see for validation:
    # https: // pythonassets.com / posts / textbox - entry - validation - in -tk - tkinter /  #:~:text=When%20the%20result%20of%20validate_entry,or%20text%20passed%20as%20argument.&text=Let's%20clarify%20this%20that%20looks,%22key%22%20means%20text%20input.
    return text.isdecimal()


class NumInput:
    def __init__(self, text, window):
        self.label = TextLabel(text)
        self.entry = tk.Entry(fg="white", bg="black", width=5,
                              validate="key",
                              validatecommand=(window.register(validate_entry), "%S"))
        self.entry.pack()

    def get_input_value(self):
        return self.entry.get()
