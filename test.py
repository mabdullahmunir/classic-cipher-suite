from crypto.cipher import *


def main():
    msg = 'temui ibu nanti malam'

    # Test Vigenere Standard
    suite = Vigenere(Vigenere.STANDARD, key="PIZZA")
    h = suite.encrypt(msg)
    print(h)
    h = suite.decrypt(h)
    print(h, '\n')

    # Test Vigenere Auto Key
    suite = Vigenere(Vigenere.AUTO_KEY, key="KILT")
    h = suite.encrypt(msg)
    print(h)
    h = suite.decrypt(h)
    print(h, '\n')

    # Test Vigenere Extended
    suite = Vigenere(Vigenere.EXTENDED, key=b"KILT")
    h = suite.encrypt(msg.encode('utf-8'))
    print(h)
    h = suite.decrypt(h)
    print(h.decode('utf-8'), '\n')

    # Test Playfair Cipher
    suite = Playfair('JALAN GANESHA SEPULUH')
    h = suite.encrypt(msg)
    print(h)
    h = suite.decrypt(h)
    print(h, '\n')

    # Test RailFence Cipher
    suite = RailFence(3)
    h = suite.encrypt('WEAREDISCOVEREDFLEEATONCE')
    print(h)
    h = suite.decrypt(h)
    print(h, '\n')


if __name__ == '__main__':
    main()
