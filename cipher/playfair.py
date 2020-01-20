class Playfair:
    _DEFAULT_CHARSET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    def __init__(self, key: str):
        self._generate_key(key.upper())

    def _generate_key(self, key: str):
        temp_key = []

        for c in key.replace('J', ''):
            if c not in temp_key:
                temp_key.append(c)

        for c in Playfair._DEFAULT_CHARSET:
            if c not in temp_key:
                temp_key.append(c)

        self._key = [temp_key[i:i+5] for i in range(0, len(temp_key), 5)]

    def encrypt(self, plaintext: str):
        pass

    def decrypt(self, ciphertext: str):
        pass

    def print_key(self):
        for l in self._key:
            print(''.join(l))
