def encrypt(text, shift):
    """Encrypts the text using Caesar Cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypts the text using Caesar Cipher."""
    return encrypt(text, -shift)

def main():
    print("=== Text Encryption and Decryption ===")
    while True:
        print("\nMenu:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the key value (int): "))
            encrypted = encrypt(text, shift)
            print(f"Encrypted Text: {encrypted}")
        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the key value (int): "))
            decrypted = decrypt(text, shift)
            print(f"Decrypted Text: {decrypted}")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()