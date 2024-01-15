import tkinter as tk

def toon_selectie():
    ziekte = ziekte_listbox.get(tk.ACTIVE)
    arts = arts_listbox.get(tk.ACTIVE)
    resultaat_label.config(text=f"U heeft gekozen voor {arts} voor een behandeling voor {ziekte}.")

root = tk.Tk()
root.title("Huiswerk 6")


ziekte_listbox = tk.Listbox(root)
ziektes = ["Leukemie", "Hartziekte", "Diabetes", "Hoge bloeddruk"]
for ziekte in ziektes:
    ziekte_listbox.insert(tk.END, ziekte)
ziekte_listbox.pack(pady=10)

arts_listbox = tk.Listbox(root)
artsen = ["Dr. Simone Groen", "Dr. Peter van de burg", "Dr. Linda Rood", "Dr. Jan Geel"]
for arts in artsen:
    arts_listbox.insert(tk.END, arts)
arts_listbox.pack(pady=10)

selectie_button = tk.Button(root, text="Toon Selectie", command=toon_selectie)
selectie_button.pack(pady=10)

resultaat_label = tk.Label(root, text="")
resultaat_label.pack(pady=10)

root.mainloop()
