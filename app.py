from cipher import *


def main():
    msg = input()
    p = Playfair('test')
    p.print_key()
    # suite = Vigenere(Vigenere.AUTO_KEY, key=b"KILT")
    # h = suite.encrypt(msg.encode('ascii'))
    # print(h)
    # h = suite.decrypt(h)
    # print(h.decode('ascii'))


if __name__ == '__main__':
    main()
