import tkinter as tk
from tkinter import messagebox

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ziekenhuis Applicatie")

        
        self.home_frame = tk.Frame(root)
        self.login_frame = tk.Frame(root)
        self.register_frame = tk.Frame(root)
        self.empty_frame = tk.Frame(root)

        self.show_frame(self.home_frame)

        tk.Label(self.home_frame, text="Welkom bij het ziekenhuis").pack(pady=10)

        tk.Button(self.home_frame, text="Login", command=lambda: self.show_frame(self.login_frame)).pack()

        tk.Button(self.home_frame, text="Registreren", command=lambda: self.show_frame(self.register_frame)).pack()

        tk.Button(self.home_frame, text="Leeg Formulier", command=lambda: self.show_frame(self.empty_frame)).pack()

        tk.Label(self.login_frame, text="Inloggen").pack(pady=10)
        tk.Label(self.login_frame, text="E-mail:").pack()
        entry_email = tk.Entry(self.login_frame)
        entry_email.pack()
        tk.Label(self.login_frame, text="Wachtwoord:").pack()
        entry_password = tk.Entry(self.login_frame, show="*")
        entry_password.pack()
        tk.Button(self.login_frame, text="Inloggen", command=lambda: self.login(entry_email.get(), entry_password.get())).pack()

        tk.Button(self.login_frame, text="Terug", command=lambda: self.show_frame(self.home_frame)).pack()

        tk.Label(self.register_frame, text="Registreren").pack(pady=10)
        tk.Label(self.register_frame, text="Naam:").pack()
        entry_name = tk.Entry(self.register_frame)
        entry_name.pack()
        tk.Label(self.register_frame, text="Achternaam:").pack()
        entry_lastname = tk.Entry(self.register_frame)
        entry_lastname.pack()
        tk.Label(self.register_frame, text="E-mail:").pack()
        entry_reg_email = tk.Entry(self.register_frame)
        entry_reg_email.pack()
        tk.Label(self.register_frame, text="Wachtwoord:").pack()
        entry_reg_password = tk.Entry(self.register_frame, show="*")
        entry_reg_password.pack()
        tk.Label(self.register_frame, text="Herhaal Wachtwoord:").pack()
        entry_confirm_password = tk.Entry(self.register_frame, show="*")
        entry_confirm_password.pack()
        tk.Button(self.register_frame, text="Opslaan", command=lambda: self.register(entry_name.get(), entry_lastname.get(), entry_reg_email.get(), entry_reg_password.get(), entry_confirm_password.get())).pack()

        tk.Button(self.register_frame, text="Terug", command=lambda: self.show_frame(self.home_frame)).pack()

        tk.Label(self.empty_frame, text="Leeg Formulier").pack(pady=10)

        tk.Button(self.empty_frame, text="Terug", command=lambda: self.show_frame(self.home_frame)).pack()

    def show_frame(self, frame):
        self.home_frame.pack_forget()
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.empty_frame.pack_forget()

        frame.pack()

    def login(self, email, password):
        messagebox.showinfo("Inloggen", f"Ingelogd met:\nE-mail: {email}\nWachtwoord: {password}")

    def register(self, name, lastname, email, password, confirm_password):
        if password == confirm_password:
            messagebox.showinfo("Registreren", f"Geregistreerd met:\nNaam: {name}\nAchternaam: {lastname}\nE-mail: {email}\nWachtwoord: {password}")
        else:
            messagebox.showerror("Fout", "Wachtwoord en herhaal wachtwoord komen niet overeen")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
