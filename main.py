from password_generator import PasswordGenerator

def main():
    generator = PasswordGenerator()
    
    print("Welcome to the Random Password Generator!")
    
    # User inputs for password criteria
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number for the password length.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate the password based on user criteria
    try:
        password = generator.generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_symbols=use_symbols
        )
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
