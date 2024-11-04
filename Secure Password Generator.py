
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip
from password_generator import PasswordGenerator

class PasswordGeneratorApp:
    def __init__(self, root):
        self.generator = PasswordGenerator()
        self.root = root
        self.root.title("Random Password Generator")
        self.create_widgets()

    def create_widgets(self):
        # Password Length
        length_label = tk.Label(self.root, text="Password Length:")
        length_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.length_var = tk.IntVar(value=12)
        length_entry = tk.Entry(self.root, textvariable=self.length_var, width=5)
        length_entry.grid(row=0, column=1, padx=5, pady=5)

        # Character Options
        self.uppercase_var = tk.BooleanVar(value=True)
        uppercase_check = tk.Checkbutton(self.root, text="Include Uppercase", variable=self.uppercase_var)
        uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w")

        self.digits_var = tk.BooleanVar(value=True)
        digits_check = tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var)
        digits_check.grid(row=2, column=0, columnspan=2, sticky="w")

        self.symbols_var = tk.BooleanVar(value=True)
        symbols_check = tk.Checkbutton(self.root, text="Include Symbols", variable=self.symbols_var)
        symbols_check.grid(row=3, column=0, columnspan=2, sticky="w")

        # Generate Button
        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Output Field
        self.password_output = tk.Entry(self.root, font=("Helvetica", 12), width=30)
        self.password_output.grid(row=5, column=0, columnspan=2, pady=5)

        # Copy to Clipboard Button
        copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=6, column=0, columnspan=2, pady=5)

    def generate_password(self):
        try:
            length = self.length_var.get()
            password = self.generator.generate_password(
                length=length,
                use_uppercase=self.uppercase_var.get(),
                use_digits=self.digits_var.get(),
                use_symbols=self.symbols_var.get()
            )
            self.password_output.delete(0, tk.END)
            self.password_output.insert(0, password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        password = self.password_output.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    try:
        import pyperclip  # Ensure pyperclip is installed for clipboard support
    except ImportError:
        print("Warning: pyperclip module is not installed. Clipboard functionality may not work.")
        
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
