import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Bericht", "Oke ! ")

def main():
    root = tk.Tk()
    root.title("KNOP/BUTTON")

    label = tk.Label(root, text="Welkom mijn eerste gemaakte knop!")
    label.pack(pady=10)

    button = tk.Button(root, text="Klik hier", command=show_message)
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
