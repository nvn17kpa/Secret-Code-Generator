# Secret Code Generator using Caesar Cipher
# Author: Naveena B V
# Date: 17 October 2025
# Description: Encode and decode messages by shifting letters in the alphabet.

def encode_message(message, shift):
    """
    Encodes the input message by shifting each letter forward by 'shift' positions.
    Non-letter characters are left unchanged.
    """
    encoded = ''
    for char in message:
        if char.isupper():
            # Uppercase letter shift
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encoded += new_char
        elif char.islower():
            # Lowercase letter shift
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encoded += new_char
        else:
            # Non-letter character
            encoded += char
    return encoded

def decode_message(message, shift):
    """
    Decodes the input message by shifting each letter backward by 'shift' positions.
    Non-letter characters are left unchanged.
    """
    return encode_message(message, -shift)

def get_shift_input():
    """
    Gets a valid shift value from the user (must be an integer).
    Handles invalid input gracefully.
    """
    while True:
        shift_input = input("Enter shift number (integer): ")
        if shift_input.lstrip('-').isdigit():
            return int(shift_input)
        else:
            print("Invalid input! Please enter a valid integer.")

def menu():
    """
    Provides the user menu for Encode, Decode, or Exit.
    Handles user's choices and calls relevant functions.
    """
    while True:
        print("\nSecret Code Generator Menu:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == '1':
            msg = input("Enter the message to encode: ")
            shift = get_shift_input()
            result = encode_message(msg, shift)
            print("Encoded message:", result)
        elif choice == '2':
            msg = input("Enter the message to decode: ")
            shift = get_shift_input()
            result = decode_message(msg, shift)
            print("Decoded message:", result)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

# Main program execution
if __name__ == "__main__":
    menu()
