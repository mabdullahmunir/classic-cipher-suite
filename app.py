from crypto.cipher import *
from crypto.util import *


msg_key = {
    0: "Insert secret key : ",
    4: "Insert filename : ",
    7: "Insert secret key : \nInsert rail count : ",
}
key = []


def print_main_menu():
    print("Classic Cipher Suite")
    print("Available cipher :")
    print("1. Standard Vigenere Cipher")
    print("2. Full Vigenere Cipher")
    print("3. Auto-key Vigenere Cipher")
    print("4. Running-key Vigenere Cipher")
    print("5. Extended Vigenere Cipher")
    print("6. Playfair Cipher")
    print("7. Super Encryption (Standard Vigenere + Railfence)")


def main():
    try:
        print_main_menu()
        menu = int(input(">> "))

        if (menu > 7) or (menu < 1):
            raise Exception("Invalid cipher")

        splitted_msg = msg_key[menu if menu in msg_key else 0].split('\n')
        for line in splitted_msg:
            temp = input(line)
            key.append(temp)

    except (ValueError, Exception) as e:
        print(e)


if __name__ == '__main__':
    main()
