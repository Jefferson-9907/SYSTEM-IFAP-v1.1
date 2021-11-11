import tkinter as tk
from tkinter import ttk


class Checkbox(ttk.Checkbutton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = tk.BooleanVar(self)
        self.configure(variable=self.variable)

    def checked(self):
        return self.variable.get()

    def check(self):
        self.variable.set(True)

    def uncheck(self):
        self.variable.set(False)


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Checkbutton en tkinter")

        # No es necesario crear una variable.
        self.checkbox = Checkbox(self, text="Opción", command=self.check_clicked)
        self.checkbox.place(x=40, y=70)

        self.place(width=300, height=200)

    def check_clicked(self):
        print(self.checkbox.checked())


main_window = tk.Tk()
app = Application(main_window)
app.mainloop()