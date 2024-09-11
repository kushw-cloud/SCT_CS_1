def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            shifted_code = (char_code - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted_code).upper() if is_upper else chr(shifted_code)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just encryption with a negative shift

if __name__ == "__main__":
    mode = input("Choose mode (encrypt/decrypt): ")
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))

    if mode == "encrypt":
        encrypted_text = encrypt(text, shift)
        print("Encrypted text:", encrypted_text)
    elif mode == "decrypt":
        decrypted_text = decrypt(text, shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid mode.")
