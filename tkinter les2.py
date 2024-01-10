import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except Exception as e:
        entry_var.set("Error")

root = tk.Tk()
root.title("Rekenmachine")


entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="C", width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)

tk.Button(root, text="=", width=5, height=2, command=calculate_result).grid(row=row_val, column=col_val + 1)

root.mainloop()
