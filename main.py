LETTERS_IN_ALPHABET: int = 26


def main():
    text: str = input("Enter text: ").strip()
    choice: int = int(input("1. Encrypt\n2. Decrypt\n").strip())
    key: int = int(input("Enter key: ").strip())
    result: str = ""

    match choice:
        case 1:
            result = encrypt(text, key)
        case 2:
            result = decrypt(text, key)

    print(result)


def encrypt(text: str, key: int) -> str:
    ciphertext: str = ""

    for letter in text:
        ciphertext += chr(
            (ord(letter) - ord("a") + key) % LETTERS_IN_ALPHABET + ord("a")
        )

    return ciphertext


def decrypt(text: str, key: int) -> str:
    plaintext: str = ""

    for letter in text:
        plaintext += chr(
            (ord(letter) - ord("a") - key) % LETTERS_IN_ALPHABET + ord("a")
        )

    return plaintext


if __name__ == "__main__":
    main()
