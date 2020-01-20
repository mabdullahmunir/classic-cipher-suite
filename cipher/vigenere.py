class Vigenere:
    STANDARD = 1
    FULL = 2
    AUTO_KEY = 3
    RUNNING_KEY = 4
    EXTENDED = 5
    _DEFAULT_CHARSET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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

    def _encrypt_standard(self, plaintext):
        ct = b""
        idx_key = 0

        for c in plaintext:
            if (c < ord(b'A')) or (c > ord(b'Z')):
                ct += chr(c).encode('ascii')
                continue

            k = self._key[idx_key] - ord(b'A')
            c = c - ord(b'A')
            ct += bytes([Vigenere._DEFAULT_CHARSET[(c + k) % 26]])
            idx_key += 1
            idx_key %= len(self._key)

        return ct

    def _encrypt_auto_key(self, plaintext):
        ct = b""
        idx_key = 0
        extend = False

        for c in plaintext:
            if (c < ord(b'A')) or (c > ord(b'Z')):
                ct += chr(c).encode('ascii')
                continue

            if not extend:
                k = self._key[idx_key]
            else:
                k = plaintext[idx_key]

            k -= ord(b'A')
            c = c - ord(b'A')
            ct += bytes([Vigenere._DEFAULT_CHARSET[(c + k) % 26]])

            idx_key += 1
            if not extend:
                if idx_key == len(self._key):
                    extend = True
                    idx_key = 0

        return ct

    def _encrypt_extended(self, plaintext):
        ct = b""
        idx_key = 0

        for c in plaintext:
            k = self._key[idx_key]
            ct += bytes([(c + k) % 256])
            idx_key += 1
            idx_key %= len(self._key)

        return ct

    def encrypt(self, plaintext):
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

    def _decrypt_standard(self, ciphertext):
        pt = b""
        idx_key = 0

        for c in ciphertext:
            if (c < ord(b'A')) or (c > ord(b'Z')):
                pt += chr(c).encode('ascii')
                continue

            k = self._key[idx_key] - ord(b'A')
            c = c - ord(b'A')
            pt += bytes([Vigenere._DEFAULT_CHARSET[(c - k) % 26]])
            idx_key += 1
            idx_key %= len(self._key)

        return pt

    def _decrypt_auto_key(self, ciphertext):
        pt = b""
        idx_key = 0
        extend = False

        for c in ciphertext:
            if (c < ord(b'A')) or (c > ord(b'Z')):
                pt += chr(c).encode('ascii')
                continue

            if not extend:
                k = self._key[idx_key]
            else:
                k = pt[idx_key]

            k -= ord(b'A')
            c = c - ord(b'A')
            pt += bytes([Vigenere._DEFAULT_CHARSET[(c - k) % 26]])

            idx_key += 1
            if not extend:
                if idx_key == len(self._key):
                    extend = True
                    idx_key = 0

        return pt

    def _decrypt_extended(self, ciphertext):
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
