import tkinter as tk
from tkinter import ttk

naw_data = {
    'Profile1': {'Naam': 'Faruk', 'Adres': 'Zwenkgras', 'Woonplaats': 'Gouda'},
    'Profile2': {'Naam': 'Tom', 'Adres': 'bloemendaal', 'Woonplaats': 'Rotterdam'},
}

def vul_gegevens_in():
    achternaam = achternaam_combobox.get()
    if achternaam in naw_data:
        gegevens = naw_data[achternaam]
        naam_entry.delete(0, tk.END)
        adres_entry.delete(0, tk.END)
        woonplaats_entry.delete(0, tk.END)

        naam_entry.insert(0, gegevens['Naam'])
        adres_entry.insert(0, gegevens['Adres'])
        woonplaats_entry.insert(0, gegevens['Woonplaats'])

root = tk.Tk()
root.title('Les 5 Huiswerk')

achternaam_combobox = ttk.Combobox(root, values=list(naw_data.keys()))
achternaam_combobox.grid(row=0, column=0, padx=10, pady=10)

vul_in_button = tk.Button(root, text='Vul Gegevens In', command=vul_gegevens_in)
vul_in_button.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text='Naam:').grid(row=1, column=0, padx=10, pady=5, sticky='w')
naam_entry = tk.Entry(root)
naam_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text='Adres:').grid(row=2, column=0, padx=10, pady=5, sticky='w')
adres_entry = tk.Entry(root)
adres_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text='Woonplaats:').grid(row=3, column=0, padx=10, pady=5, sticky='w')
woonplaats_entry = tk.Entry(root)
woonplaats_entry.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
