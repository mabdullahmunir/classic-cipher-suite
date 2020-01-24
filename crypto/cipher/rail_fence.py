from itertools import cycle, chain


class RailFence:

    def __init__(self, n_rails: int):
        self._n_rails = n_rails

    def _gen_fence_pattern(self, size: int):
        pattern = cycle(chain(range(self._n_rails), range(self._n_rails-2, 0, -1)))
        return zip(pattern, range(size))

    def encrypt(self, plaintext: str):
        pattern = self._gen_fence_pattern(len(plaintext))
        return ''.join([plaintext[i[1]] for i in sorted(pattern)])

    def decrypt(self, ciphertext: str):
        pattern = self._gen_fence_pattern(len(ciphertext))
        pair_cipher = zip(ciphertext, sorted(pattern))
        return ''.join(
            [pair[0] for pair in sorted(pair_cipher, key=lambda item: item[1][1])]
        )
