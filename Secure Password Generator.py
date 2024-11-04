# Import necessary libraries
import tkinter as tk  # For creating the GUI
from tkinter import messagebox  # For showing error and info popups
from tkinter import ttk  # For additional Tkinter widget styling (not used here but can be helpful)
import pyperclip  # For copying text to the clipboard
from password_generator import PasswordGenerator  # Custom password generator class

# Define the main application class
class PasswordGeneratorApp:
    # Initialize the app with the main Tkinter root window
    def __init__(self, root):
        # Create an instance of the PasswordGenerator class
        self.generator = PasswordGenerator()
        self.root = root
        self.root.title("Random Password Generator")  # Set the window title
        self.create_widgets()  # Create all widgets for the UI

    # Method to create all UI widgets
    def create_widgets(self):
        # Password Length
        length_label = tk.Label(self.root, text="Password Length:") # Label for password length input
        length_label.grid(row=0, column=0, padx=5, pady=5)  # Position label
        
        self.length_var = tk.IntVar(value=12)  # Variable to hold password length with default of 12
        length_entry = tk.Entry(self.root, textvariable=self.length_var, width=5)  # Entry box for length input
        length_entry.grid(row=0, column=1, padx=5, pady=5)   # Position entry box

        # Checkbutton for including uppercase letters
        self.uppercase_var = tk.BooleanVar(value=True) # Boolean variable for uppercase option
        uppercase_check = tk.Checkbutton(self.root, text="Include Uppercase", variable=self.uppercase_var)
        uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w")  # Position checkbox

        # Checkbutton for including digits
        self.digits_var = tk.BooleanVar(value=True)  # Boolean variable for digits option
        digits_check = tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var)
        digits_check.grid(row=2, column=0, columnspan=2, sticky="w")  # Position checkbox

        # Checkbutton for including symbols
        self.symbols_var = tk.BooleanVar(value=True) # Boolean variable for symbols option
        symbols_check = tk.Checkbutton(self.root, text="Include Symbols", variable=self.symbols_var)
        symbols_check.grid(row=3, column=0, columnspan=2, sticky="w") # Position checkbox

        # Button to generate password
        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=4, column=0, columnspan=2, pady=10) # Position button

        # Entry box to display generated password
        self.password_output = tk.Entry(self.root, font=("Helvetica", 12), width=30)  # Entry box for output
        self.password_output.grid(row=5, column=0, columnspan=2, pady=5)  # Position entry box

        # Button to copy password to clipboard
        copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=6, column=0, columnspan=2, pady=5)  # Position button

    # Method to generate password based on user options
    def generate_password(self):
        try:
            # Retrieve user preferences and length
            length = self.length_var.get()
            # Generate password based on selected options
            password = self.generator.generate_password(
                length=length,
                use_uppercase=self.uppercase_var.get(),
                use_digits=self.digits_var.get(),
                use_symbols=self.symbols_var.get()
            )
            # Display the generated password in the output entry box
            self.password_output.delete(0, tk.END)   # Clear previous password
            self.password_output.insert(0, password)  # Insert new password
        except ValueError as e:
            # Display error message if generation fails
            messagebox.showerror("Error", str(e))

    # Method to copy password to the clipboard
    def copy_to_clipboard(self):
        password = self.password_output.get()  # Retrieve generated password
        if password:  # Ensure there is a password to copy
            pyperclip.copy(password)  # Copy to clipboard
            messagebox.showinfo("Copied", "Password copied to clipboard!")  # Show confirmation

# Main program execution
if __name__ == "__main__":
    # Check if pyperclip is installed for clipboard support
    try:
        import pyperclip  # Ensure pyperclip is installed for clipboard support
    except ImportError:
        print("Warning: pyperclip module is not installed. Clipboard functionality may not work.")
        
    root = tk.Tk() # Initialize main Tkinter window
    app = PasswordGeneratorApp(root)  # Create the application instance
    root.mainloop() # Run the Tkinter event loop
