# Simple Number Converter
# Converts a positive decimal integer to binary and hexadecimal

def main():
    try:
        user_input = input("Enter a decimal number: ")
        decimal_number = int(user_input)
        
        if decimal_number < 0:
            print("Please enter a positive decimal integer.")
            return

        binary_result = bin(decimal_number)
        hexadecimal_result = hex(decimal_number)

        print(f"Decimal: {decimal_number}")
        print(f"Binary: {binary_result}")
        print(f"Hexadecimal: {hexadecimal_result}")

    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")

if __name__ == "__main__":
    main()
