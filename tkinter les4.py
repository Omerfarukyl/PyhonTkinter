import tkinter as tk
from tkinter import ttk
import sqlite3

class RegistratieAdressenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RegistratieAdressen")

        self.conn = sqlite3.connect('adressen.db')
        self.create_table()

        self.label_naam = ttk.Label(root, text="Naam:")
        self.entry_naam = ttk.Entry(root)

        self.label_adres = ttk.Label(root, text="Adres:")
        self.entry_adres = ttk.Entry(root)

        self.button_opslaan = ttk.Button(root, text="Opslaan", command=self.adres_toevoegen)

        self.label_naam.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_naam.grid(row=0, column=1, padx=10, pady=5)

        self.label_adres.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_adres.grid(row=1, column=1, padx=10, pady=5)

        self.button_opslaan.grid(row=2, column=0, columnspan=2, pady=10)

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS adressen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL,
            adres TEXT NOT NULL
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def adres_toevoegen(self):
        naam = self.entry_naam.get()
        adres = self.entry_adres.get()

        if naam and adres:
            query = "INSERT INTO adressen (naam, adres) VALUES (?, ?);"
            self.conn.execute(query, (naam, adres))
            self.conn.commit()
            print("Adres toegevoegd aan de database.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistratieAdressenApp(root)
    root.mainloop()
