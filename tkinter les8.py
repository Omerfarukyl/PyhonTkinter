import tkinter as tk
from tkinter import filedialog

class SimpleEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack(pady=10)

        self.text_widget = tk.Text(root, wrap="word", width=40, height=10)
        self.text_widget.pack(pady=10)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        edit_menu = tk.Menu(menubar, tearoff=0)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
                self.text_entry.delete(0, tk.END)
                self.text_entry.insert(0, file_path)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)
                self.text_entry.delete(0, tk.END)
                self.text_entry.insert(0, file_path)

    def show_about(self):
        about_text = "Simple Text Editor\n\nCreated with Python and Tkinter"
        tk.messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleEditor(root)
    root.mainloop()
