class Vigenere:
    STANDARD = 1
    FULL = 2
    AUTO_KEY = 3
    RUNNING_KEY = 4
    EXTENDED = 5
    _DEFAULT_CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, variant, key=None, filename=None):
        if (variant < 1) and (variant > 5):
            pass  # TODO: throw error (Invalid Variant)
        self._type = variant

        if self._type == Vigenere.RUNNING_KEY:
            if filename is None:
                pass  # TODO: throw error
            self._filename = filename

        else:
            if key is None:
                pass  # TODO: throw error
            if self._type == Vigenere.FULL:
                pass  # TODO: generate sbox based on key
            else:
                self._key = key

    def _encrypt_standard(self, plaintext: str):
        ct = ""
        idx_key = 0

        for c in plaintext:
            if c not in Vigenere._DEFAULT_CHARSET:
                ct += c
                continue

            k = Vigenere._DEFAULT_CHARSET.index(self._key[idx_key])
            c = Vigenere._DEFAULT_CHARSET.index(c)
            ct += Vigenere._DEFAULT_CHARSET[(c + k) % 26]
            idx_key += 1
            idx_key %= len(self._key)

        return ct

    def _encrypt_auto_key(self, plaintext: str):
        ct = ""
        idx_key = 0
        extend = False

        for c in plaintext:
            if c not in Vigenere._DEFAULT_CHARSET:
                ct += c
                continue

            if not extend:
                k = Vigenere._DEFAULT_CHARSET.index(self._key[idx_key])
            else:
                while plaintext[idx_key] not in Vigenere._DEFAULT_CHARSET:
                    idx_key += 1
                k = Vigenere._DEFAULT_CHARSET.index(plaintext[idx_key])

            c = Vigenere._DEFAULT_CHARSET.index(c)
            ct += Vigenere._DEFAULT_CHARSET[(c + k) % 26]

            idx_key += 1
            if not extend:
                if idx_key == len(self._key):
                    extend = True
                    idx_key = 0

        return ct

    def _encrypt_extended(self, plaintext: bytes):
        ct = b""
        idx_key = 0

        for c in plaintext:
            k = self._key[idx_key]
            ct += bytes([(c + k) % 256])
            idx_key += 1
            idx_key %= len(self._key)

        return ct

    def encrypt(self, plaintext):
        if type(plaintext) == str:
            plaintext = plaintext.upper()

        if self._type == Vigenere.STANDARD:
            return self._encrypt_standard(plaintext)
        elif self._type == Vigenere.FULL:
            pass  # TODO
        elif self._type == Vigenere.AUTO_KEY:
            return self._encrypt_auto_key(plaintext)
        elif self._type == Vigenere.RUNNING_KEY:
            pass  # TODO
        elif self._type == Vigenere.EXTENDED:
            return self._encrypt_extended(plaintext)

    def _decrypt_standard(self, ciphertext: str):
        pt = ""
        idx_key = 0

        for c in ciphertext:
            if c not in Vigenere._DEFAULT_CHARSET:
                pt += c
                continue

            k = Vigenere._DEFAULT_CHARSET.index(self._key[idx_key])
            c = Vigenere._DEFAULT_CHARSET.index(c)
            pt += Vigenere._DEFAULT_CHARSET[(c - k) % 26]
            idx_key += 1
            idx_key %= len(self._key)

        return pt

    def _decrypt_auto_key(self, ciphertext: str):
        pt = ""
        idx_key = 0
        extend = False

        for c in ciphertext:
            if c not in Vigenere._DEFAULT_CHARSET:
                pt += c
                continue

            if not extend:
                k = Vigenere._DEFAULT_CHARSET.index(self._key[idx_key])
            else:
                while pt[idx_key] not in Vigenere._DEFAULT_CHARSET:
                    idx_key += 1
                k = Vigenere._DEFAULT_CHARSET.index(pt[idx_key])

            c = Vigenere._DEFAULT_CHARSET.index(c)
            pt += Vigenere._DEFAULT_CHARSET[(c - k) % 26]

            idx_key += 1
            if not extend:
                if idx_key == len(self._key):
                    extend = True
                    idx_key = 0

        return pt

    def _decrypt_extended(self, ciphertext: bytes):
        pt = b""
        idx_key = 0

        for c in ciphertext:
            k = self._key[idx_key]
            pt += bytes([(c - k) % 256])
            idx_key += 1
            idx_key %= len(self._key)

        return pt

    def decrypt(self, ciphertext):
        if self._type == Vigenere.STANDARD:
            return self._decrypt_standard(ciphertext)
        elif self._type == Vigenere.FULL:
            pass  # TODO
        elif self._type == Vigenere.AUTO_KEY:
            return self._decrypt_auto_key(ciphertext)
        elif self._type == Vigenere.RUNNING_KEY:
            pass  # TODO
        elif self._type == Vigenere.EXTENDED:
            return self._decrypt_extended(ciphertext)
