class Playfair:
    _DEFAULT_CHARSET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    # check position result
    _SAME_ROW = 1
    _SAME_COL = 2
    _OTHER = 3

    def __init__(self, key: str):
        self._generate_key(''.join(filter(str.isalpha, key.upper())))

    def _generate_key(self, key: str):
        temp_key = []

        for c in key.replace('J', ''):
            if c not in temp_key:
                temp_key.append(c)

        for c in Playfair._DEFAULT_CHARSET:
            if c not in temp_key:
                temp_key.append(c)

        self._key = [temp_key[i:i+5] for i in range(0, len(temp_key), 5)]

    def _get_pos(self, c):
        row, col = 0, 0
        for i in range(5):
            if c in self._key[i]:
                row = i
                break

        for i in range(5):
            if c == self._key[row][i]:
                col = i
                break

        return row, col

    @staticmethod
    def _check_pos(pos1, pos2):
        if pos1[0] == pos2[0]:
            return Playfair._SAME_ROW
        elif pos1[1] == pos2[1]:
            return Playfair._SAME_COL
        else:
            return Playfair._OTHER

    def encrypt(self, plaintext: str):
        plaintext = ''.join(filter(str.isalpha, plaintext.upper())).replace('J', 'I')

        list_msg = []
        temp_msg = ''
        # group message per 2 character
        # append 'X' if same character
        for c in plaintext:
            len_msg = len(temp_msg)
            if len_msg == 1:
                if temp_msg[0] == c:
                    list_msg.append(temp_msg + 'X')
                    temp_msg = ''
            elif len(temp_msg) == 2:
                list_msg.append(temp_msg)
                temp_msg = ''
            temp_msg += c

        # append 'X' if last group not bigram
        if len(temp_msg) % 2 != 0:
            list_msg.append(temp_msg + 'X')

        enc_msg = []

        for msg in list_msg:
            pos1, pos2 = self._get_pos(msg[0]), self._get_pos(msg[1])
            res_pos = self._check_pos(pos1, pos2)

            if res_pos == Playfair._SAME_ROW:
                ct = self._key[pos1[0]][(pos1[1] + 1) % 5]
                ct += self._key[pos2[0]][(pos2[1] + 1) % 5]
                enc_msg.append(ct)
            elif res_pos == Playfair._SAME_COL:
                ct = self._key[(pos1[0] + 1) % 5][pos1[1]]
                ct += self._key[(pos2[0] + 1) % 5][pos2[1]]
                enc_msg.append(ct)
            else:
                ct = self._key[pos1[0]][pos2[1]]
                ct += self._key[pos2[0]][pos1[1]]
                enc_msg.append(ct)

        return ' '.join(enc_msg)

    def decrypt(self, ciphertext: str):
        ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))

        # assume message always even
        list_msg = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]

        plain_msg = []

        for msg in list_msg:
            pos1, pos2 = self._get_pos(msg[0]), self._get_pos(msg[1])
            res_pos = self._check_pos(pos1, pos2)

            if res_pos == Playfair._SAME_ROW:
                ct = self._key[pos1[0]][(pos1[1] - 1) % 5]
                ct += self._key[pos2[0]][(pos2[1] - 1) % 5]
                plain_msg.append(ct)
            elif res_pos == Playfair._SAME_COL:
                ct = self._key[(pos1[0] - 1) % 5][pos1[1]]
                ct += self._key[(pos2[0] - 1) % 5][pos2[1]]
                plain_msg.append(ct)
            else:
                ct = self._key[pos1[0]][pos2[1]]
                ct += self._key[pos2[0]][pos1[1]]
                plain_msg.append(ct)

        return ' '.join(plain_msg)
