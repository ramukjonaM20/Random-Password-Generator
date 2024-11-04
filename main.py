# Import the PasswordGenerator class from the password_generator module
from password_generator import PasswordGenerator

# Main function for the program
def main():
    # Create an instance of PasswordGenerator to use for password generation
    generator = PasswordGenerator()
    
    # Welcome message for the user
    print("Welcome to the Random Password Generator!")
    
    # User inputs for password criteria
    try:
        # Prompt user to enter desired password length
        length = int(input("Enter the desired password length: "))
    except ValueError:
        # If the input is not a valid integer, display an error and exit
        print("Please enter a valid number for the password length.")
        return

    # Prompt user for character preferences, converting input to boolean
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Attempt to generate the password based on user criteria
    try:
        password = generator.generate_password(
            length=length,  # Length of password
            use_uppercase=use_uppercase, # Include uppercase letters if True
            use_digits=use_digits,  # Include digits if True
            use_symbols=use_symbols  # Include symbols if True
        )
        # Display the generated password to the user
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        # If there is an error with generation (e.g., length too short), display it
        print(f"Error: {e}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
