import tkinter as tk
from tkinter import ttk

class RGBColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RGB kleur picker")

        self.red = tk.IntVar(value=0)
        self.green = tk.IntVar(value=0)
        self.blue = tk.IntVar(value=0)

        self.red_slider = ttk.Scale(root, from_=0, to=255, variable=self.red, orient=tk.HORIZONTAL, length=200, command=self.update_color)
        self.green_slider = ttk.Scale(root, from_=0, to=255, variable=self.green, orient=tk.HORIZONTAL, length=200, command=self.update_color)
        self.blue_slider = ttk.Scale(root, from_=0, to=255, variable=self.blue, orient=tk.HORIZONTAL, length=200, command=self.update_color)

        self.color_box = tk.Label(root, text="Kleur", font=('Helvetica', 16), padx=20, pady=10)

        self.set_color_button = ttk.Button(root, text="Set Color", command=self.set_color)

        self.red_slider.grid(row=0, column=0, padx=10, pady=10)
        self.green_slider.grid(row=0, column=1, padx=10, pady=10)
        self.blue_slider.grid(row=0, column=2, padx=10, pady=10)
        self.color_box.grid(row=1, column=0, columnspan=3, pady=10)
        self.set_color_button.grid(row=2, column=0, columnspan=3, pady=10)

    def update_color(self, event=None):
        color = "#{:02X}{:02X}{:02X}".format(self.red.get(), self.green.get(), self.blue.get())
        self.color_box.config(bg=color)

    def set_color(self):
        print("Selected Color: #{:02X}{:02X}{:02X}".format(self.red.get(), self.green.get(), self.blue.get()))

if __name__ == "__main__":
    root = tk.Tk()
    app = RGBColorPickerApp(root)
    root.mainloop()
