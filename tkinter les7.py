import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Huiswerkopdracht")

        self.data_source = tk.StringVar()
        self.data_destination = tk.StringVar()

        tk.Label(root, text="Data Source:").grid(row=0, column=0, padx=10, pady=10)
        tk.Radiobutton(root, text="Database", variable=self.data_source, value="Database").grid(row=0, column=1, padx=10, pady=10)
        tk.Radiobutton(root, text="API", variable=self.data_source, value="API").grid(row=0, column=2, padx=10, pady=10)
        tk.Radiobutton(root, text="Bestand", variable=self.data_source, value="Bestand").grid(row=0, column=3, padx=10, pady=10)

        tk.Label(root, text="Data Destination:").grid(row=1, column=0, padx=10, pady=10)
        tk.Radiobutton(root, text="Database", variable=self.data_destination, value="Database").grid(row=1, column=1, padx=10, pady=10)
        tk.Radiobutton(root, text="Bestand", variable=self.data_destination, value="Bestand").grid(row=1, column=2, padx=10, pady=10)

        tk.Label(root, text="Ziektes:").grid(row=2, column=0, padx=10, pady=10)
        self.diseases_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        diseases = ["Oorsuizen", "Hoofdpijn", "Koorts", "Buikpijn"]
        for disease in diseases:
            self.diseases_listbox.insert(tk.END, disease)
        self.diseases_listbox.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(root, text="Artsen:").grid(row=2, column=2, padx=10, pady=10)
        self.doctors_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        doctors = ["Dr. Simone Groen", "Dr. Thomas Blauw", "Dr. Laura Rood"]
        for doctor in doctors:
            self.doctors_listbox.insert(tk.END, doctor)
        self.doctors_listbox.grid(row=2, column=3, padx=10, pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        tk.Button(root, text="Toon keuze", command=self.show_choice).grid(row=4, column=0, columnspan=4, pady=10)

    def show_choice(self):
        selected_disease = self.diseases_listbox.get(tk.ACTIVE)
        selected_doctor = self.doctors_listbox.get(tk.ACTIVE)

        result_text = f"U heeft gekozen voor {selected_doctor} voor een behandeling voor {selected_disease}."
        self.result_label.config(text=result_text)
        messagebox.showinfo("Keuze", result_text)

root = tk.Tk()
app = App(root)

root.mainloop()
